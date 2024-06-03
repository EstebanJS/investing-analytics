from core.models import CompanyInfo,CorrelationalInterface
from core.repositories.company_info_repository import CompanyInfoRepository,CompanyInfoRepository
from utils import ActiveMQService
import uuid

class CompanyInfoServices:
    
    def __init__(self):
        self.company_info_repository = CompanyInfoRepository()
        self.correlational_interface = CorrelationalInterface()
        self.broker = ActiveMQService()
        
    def get_company_info(self, company_name:str):
        OrgRefMsg = uuid.uuid4()
        body = {"CompanyName": company_name}
        company_info = CompanyInfo({"status":"WAITHING_FOR_DATA","PtyCd":company_name})
        self.company_info_repository.insert(company_info)
        
        # Summary Info
        header = {"OrgRefMsg":OrgRefMsg,"OrgTypMsg":"SUMMARY"}
        self.broker.send_message()
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa

            company_data = response.json()
            
            # Crea una instancia de CompanyInfo con los datos recibidos
            company_info = CompanyInfo(company_data)
            
            # Guarda la información de la compañía en el repositorio
            self.company_info_repository.insert(company_info)

            return company_info

        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la solicitud POST: {e}")
            return None
        