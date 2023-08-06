import requests
from etlwrench import models

class ModuleEndpoint:
    
    def __init__(self, host: str):
        self.__host = host
    
    def get_all(self) -> (list[models.Module], Exception):
        try:
            response = requests.get(
                url=self.__host + "/module",
            )
        except Exception as e:
            return None, e
        
        if response.status_code != 200:
            return None, requests.ConnectionError
        
        modules = []
        
        for module_json in response.json():
            modules.append(models.Module(**module_json))

        return modules, None
