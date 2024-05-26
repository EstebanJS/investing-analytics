import requests
from core.models.company_info import CompanyInfo
from core.repositories.company_info_repository import CompanyInfoRepository

class CompanyInfoServices:
    
    def __init__(self):
        self.company_info_repository = CompanyInfoRepository()
        
    def create_company_info(self, company_name:str):
        url = ""
        payload = {"CompanyName": company_name}
        
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
        