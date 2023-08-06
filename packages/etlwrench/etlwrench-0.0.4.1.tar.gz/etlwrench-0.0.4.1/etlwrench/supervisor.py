import requests
from etlwrench import models

class SupervisorEndpoint:
    
    def __init__(self, host:str):
        self.__host = host
    
    def provision(self, module:str, cluster:str, config: str) -> (models.ProvisionResponse, Exception):
        try:
            response = requests.post(
                url=f"{self.__host}/supervisor",
                json={
                    "module": module,
                    "cluster": cluster,
                    "config": config
                }
            )
        except Exception as e:
            return None, e
        
        if response.status_code != 200:
            return None, requests.ConnectionError
        
        return models.ProvisionResponse(**response.json()), None
    
    def get(self, module:str, cluster:str, id:str) -> (models.Supervisor, Exception):
        try:
            response = requests.get(
                url=f"{self.__host}/supervisor?id={id}&module={module}&cluster={cluster}"
            )
        except Exception as e:
            return None, e
        
        if response.status_code != 200:
            return None, requests.ConnectionError
        
        return models.Supervisor(**response.json()), None