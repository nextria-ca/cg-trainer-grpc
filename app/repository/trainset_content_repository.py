

from dataclasses import dataclass

from repository.connection_manager import ConnectionManager
from models.trainset_contents import TrainsetContent
from repository.base_respoitory import BaseRepository


@dataclass
class TrainsetContentRepository(BaseRepository[TrainsetContent]):
    def __init__(self, connection_manager: ConnectionManager):
        super().__init__(TrainsetContent, connection_manager)
