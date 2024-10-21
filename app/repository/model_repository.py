

from dataclasses import dataclass

from repository.connection_manager import ConnectionManager
from models.models import Model
from models.trainset import Trainset
from repository.base_respoitory import BaseRepository, exception_handler_decorator
from sqlalchemy import select


@dataclass
class ModelRepository(BaseRepository[Model]):
    def __init__(self, connection_manager: ConnectionManager):
        super().__init__(Model, connection_manager)

    @exception_handler_decorator
    async def delete(self, id: int, trainset_id) -> None:

        async with self.connection_manager.get_session() as session:
            if trainset_id is None:
                raise ValueError(
                    f"Model with id {id} is in use and trainset_id is not provided"
                )
            references_statement = (
                select(Trainset)
                .where(Trainset.base_model_inst_id == id)
                .where(Trainset.id == trainset_id)
            )

            result = await session.execute(references_statement)
            trainset = result.scalars().all()

            for content in trainset:
                content.base_model_inst_id = None
                await session.flush()
                await session.refresh(content)

            is_orphan_statement = (
                select(Trainset)
                .where(Trainset.base_model_inst_id == id)
            )

            result = await session.execute(is_orphan_statement)
            orphan = result.scalar()

            if orphan is None:
                db_obj = await session.get(self.clazz, id)
                if db_obj is None:
                    raise ValueError(f"Model with id {id} not found")
                await session.delete(db_obj)
                await session.flush()
