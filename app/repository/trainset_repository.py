

from dataclasses import dataclass
from sqlalchemy import select, text

from repository.connection_manager import ConnectionManager
from models.trainset import Trainset
from repository.base_respoitory import BaseRepository, exception_handler_decorator
import oracledb

@dataclass
class TrainsetRepository(BaseRepository[Trainset]):
    def __init__(self, connection_manager: ConnectionManager):
        super().__init__(Trainset, connection_manager)

    # SQL queries as class constants for better readability
    _SET_ACTIVE_SQL = text("""
        UPDATE trainset
        SET is_active = CASE
            WHEN id = :trainset_id THEN TRUE
            ELSE FALSE
        END
        WHERE base_model_inst_id = :model_id
    """)

    _DUPLICATE_CONTENT_SQL = text("""
        INSERT INTO trainset_contents (
            trainset_id,
            acronym_id,
            traindata_id,
            role
        )
        SELECT
            :new_trainset_id,
            acronym_id,
            traindata_id,
            role
        FROM
            trainset_contents
        WHERE
            trainset_id = :trainset_id
    """)

    _DUPLICATE_ACRONYM_DATA_SQL = text("""
        INSERT INTO acronyms_traindata (
            acronym_id,
            provided_by,
            generated_bytrainset_id,
            text_en,
            text_fr,
            reason,
            create_dt
        )
        SELECT
            acronym_id,
            provided_by,
            :new_trainset_id,
            text_en,
            text_fr,
            reason,
            CURRENT_DATE  -- Set to current date
        FROM
            acronyms_traindata
        WHERE
            generated_bytrainset_id = :trainset_id
    """)

    _DUPLICATE_MODEL_SQL = text("""
        INSERT INTO models (
            name,
            version,
            created_by,
            checkpoint,
            score,
            department,
            status,
        )
        SELECT
            name,
            version,
            created_by,
            checkpoint,
            score,
            department,
            status
        FROM
            models
        WHERE
            id = :model_id
    """)    

    @exception_handler_decorator
    async def set_active_by_id(
        self, model_id: int, trainset_id: int
    ) -> Trainset:
        async with self.connection_manager.get_session() as session:
            await session.execute(
                self._SET_ACTIVE_SQL,
                {'trainset_id': trainset_id, 'model_id': model_id}
            )

            statement = select(Trainset).filter(Trainset.id == trainset_id)
            result = await session.execute(statement)
            return result.scalar()

    @exception_handler_decorator
    async def duplicate_by_id(self, trainset_id: int, version) -> Trainset:
        async with self.connection_manager.get_session() as session:

            # Get the trainset to duplicate
            trainset = await session.get(Trainset, trainset_id)

            if not trainset:
                raise ValueError(f"Trainset with id {trainset_id} not found")

            # Duplicate the trainset
            # Note: create_dt, is_active, are not copied
            new_trainset = Trainset(
                last_run=trainset.last_run,
                base_model_inst_id=trainset.base_model_inst_id,
                new_model_inst_id=trainset.new_model_inst_id,
                description=trainset.description,
                version=version,
                created_by=trainset.created_by,
            )

            session.add(new_trainset)
            await session.flush()
            await session.refresh(new_trainset)

            await session.execute(
                self._DUPLICATE_CONTENT_SQL,
                {'trainset_id': trainset_id, 'new_trainset_id': new_trainset.id}
            )

            await session.execute(
                self._DUPLICATE_ACRONYM_DATA_SQL,
                {'trainset_id': trainset_id, 'new_trainset_id': new_trainset.id}
            )

            return new_trainset

    @exception_handler_decorator
    async def get_by_base_model_id(self, model_id: int) -> [Trainset]:
        async with self.connection_manager.get_session() as session:
            statement = select(
                        Trainset
                        ).filter(
                            Trainset.base_model_inst_id == model_id
                        ).order_by(Trainset.create_dt.desc())
            result = await session.execute(statement)
            return result.scalars().all()
