from models import BaseModel

class CorrelationalInterface(BaseModel):
    
    def __init__(self,data = None):
        super().__init__(data)
        self.OrgRefMsg = data.get("OrgRefMsg")
        self.OrgTypMsg = data.get("OrgTypMsg")
        self.PrntRegMsg = data.get("PrntRegMsg")
        self.PrntTypMsg = data.get("PrntTypMsg")
        
        