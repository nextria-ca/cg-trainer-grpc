from dataclasses import dataclass

from sqlalchemy import select
from repository.connection_manager import ConnectionManager
from models.acronyms import Acronym
from models.trainset_contents import TrainsetContent
from repository.base_respoitory import BaseRepository, exception_handler_decorator


@dataclass
class AcronymRepository(BaseRepository[Acronym]):
    def __init__(self, connection_manager: ConnectionManager):
        super().__init__(Acronym, connection_manager)

    @exception_handler_decorator
    async def find_by_trainset_id(self, trainset_id: int) -> list[Acronym]:
        async with self.connection_manager.get_session() as session:
            statement = (
                select(Acronym)
                .select_from(Acronym)
                .join(
                    TrainsetContent,
                    Acronym.id == TrainsetContent.acronym_id
                )
                .filter(TrainsetContent.trainset_id == trainset_id)
            )
            result = await session.execute(statement)
            return result.scalars().all()

    @exception_handler_decorator
    async def delete(self, id: int, trainset_id) -> None:
        """Delete a record."""
        async with self.connection_manager.get_session() as session:

            if trainset_id is None:
                raise ValueError(
                    f"Acronym with id {id} is in use and trainset_id is not provided"
                )
            references_statement = (
                select(TrainsetContent)
                .where(TrainsetContent.acronym_id == id)
                .where(TrainsetContent.trainset_id == trainset_id)
            )

            result = await session.execute(references_statement)
            trainset_content = result.scalars().all()

            for content in trainset_content:
                content.acronym_id = None
                await session.flush()
                await session.refresh(content)

            is_orphan_statement = (
                select(TrainsetContent)
                .where(TrainsetContent.acronym_id == id)
            )

            result = await session.execute(is_orphan_statement)
            orphan = result.scalars().all()
            if len(orphan) == 0:
                db_obj = await session.get(self.clazz, id)
                if db_obj is None:
                    raise ValueError(f"Acronym with id {id} not found")
                await session.delete(db_obj)
                await session.flush()
