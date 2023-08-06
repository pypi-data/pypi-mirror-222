import requests

from etlwrench import models

class ClusterEndpoint:
    
    def __init__(self, host:str):
        self.__host = host
    
    def get(self, module: str) -> (list[models.Cluster], Exception):
        try:
            response = requests.get(
                url=f"{self.__host}/cluster?module={module}"
            )
        except Exception as e:
            return None, e
        
        if response.status_code != 200:
            return None, requests.ConnectionError

        clusters = []
        
        for item in response.json().items():
            clusters.append(models.Cluster(id=item[0], mounted=item[1]))
        
        return clusters, None
    
    def mount(self, module: str, id: str) -> bool:
        try:
            response = requests.put(
                url=f"{self.__host}/cluster",
                json={
                    "module": module,
                    "cluster": id,
                    "mounted": True
                }
            )
        except Exception:
            return False
        
        return response.status_code == 200

    def unmount(self, module: str, id: str) -> bool:
        try:
            response = requests.put(
                url=f"{self.__host}/cluster",
                json={
                    "module": module,
                    "cluster": id,
                    "mounted": False
                }
            )
        except Exception:
            return False
        
        return response.status_code == 200
