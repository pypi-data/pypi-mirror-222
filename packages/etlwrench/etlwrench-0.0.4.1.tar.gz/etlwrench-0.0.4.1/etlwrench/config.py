import requests

from etlwrench import models

class ConfigEndpoint:
    
    def __init__(self, host:str):
        self.__host = f"{host}/config"
    
    def get(self, module:str, config:str) -> (models.Config, Exception):
        try:
            response = requests.get(
                url=f"{self.__host}?cluster={config}&module={module}"
            )
        except Exception as e:
            return None, e
        
        if response.status_code != 200:
            return None, requests.exceptions.RequestException
        
        config_object = models.Config(**response.json())
        return config_object, None
    
    def create(self, module:str, config:models.Config) -> Exception:
        try:
            response = requests.post(
                url=f"{self.__host}?module={module}",
                json=config.json()
            )
        except Exception as e:
            return e
        
        if response.status_code != 200:
            return requests.exceptions.RequestException
        
        return None