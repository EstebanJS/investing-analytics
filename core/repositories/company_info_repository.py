from utils.database import db_instance
from core.repositories.base_repository import BaseRepository
from core.models.company_info import CompanyInfo

class CompanyInfoRepository(BaseRepository):
    
    def __init__(self):
        super.__init__(db_instance.get_collection("CompanyInfo"))
        
    def insert(self,company_info):
        return self.collection.insert_one(company_info.to_dict())
    
    def find_by_id(self,_id):
        companyInfoData = self.collection.find_one({"_id":_id})
        return CompanyInfo(companyInfoData) if companyInfoData else None