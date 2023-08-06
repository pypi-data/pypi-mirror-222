import requests

class DebugEndpoint:
    
    def __init__(self, host: str):
        self.__host = f"{host}/debug"
    
    def ping(self) -> (bool, int):
        try:
            response = requests.post(
                url=self.__host,
                json={"action": "ping"}
            )
        except Exception:
            return False, -1
            
        if response.status_code != 200:
            return False, -1
        response_data = response.json()
        
        time_elapsed = 0
        if "time-elapsed" in response_data:
            time_elapsed = response_data["time-elapsed"]
        
        return True, time_elapsed

    def toggle_debug(self) -> bool:
        try:
            response = requests.post(
                url=self.__host,
                json={"action": "debug"}
            )
            return response.text == "debug mode activated"
        except Exception:
            return False
    
    def shutdown(self) -> bool:
        try:
            response = requests.post(
                url=self.__host,
                json={"action": "shutdown"}
            )
            return response.status_code == 200
        except Exception:
            return False