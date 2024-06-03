from utils.database import db_instance
from core.repositories.base_repository import BaseRepository
from core.models import CorrelationalInterface

class CorrelationalInterfaceRepository(BaseRepository):
    
    def __init__(self):
        super.__init__(db_instance.get_collection("CorrelationalInterface"))
        
    def insert(self,correlational_interface):
        return self.collection.insert_one(correlational_interface.to_dict())
    
    def find_by_id(self,_id):
        CorrelationalInterfaceData = self.collection.find_one({"_id":_id})
        return CorrelationalInterface(CorrelationalInterfaceData) if CorrelationalInterfaceData else None