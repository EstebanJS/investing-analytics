from core.services import CompanyInfoServices

class Controller:
    def __init__(self):
        service = CompanyInfoServices()
    
    def get_company_info(CompanyName):
        return service.get_company_info(CompanyName)
        