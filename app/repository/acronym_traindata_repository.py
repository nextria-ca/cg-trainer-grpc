

from dataclasses import dataclass


from repository.connection_manager import ConnectionManager
from models.acronyms_traindata import AcronymTrainData
from repository.base_respoitory import BaseRepository

@dataclass
class AcronymTrainDataRepository(BaseRepository[AcronymTrainData]):
    def __init__(self, connection_manager: ConnectionManager):
        super().__init__(AcronymTrainData, connection_manager)
