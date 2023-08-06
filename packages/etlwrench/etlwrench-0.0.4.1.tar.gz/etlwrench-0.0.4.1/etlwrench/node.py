import os
import requests

from etlwrench import models
from etlwrench.cluster import ClusterEndpoint
from etlwrench.supervisor import SupervisorEndpoint
from etlwrench.debug import DebugEndpoint
from etlwrench.module import ModuleEndpoint
from etlwrench.config import ConfigEndpoint

class Cluster:
    
    def __init__(self, cluster_endpoint:ClusterEndpoint, supervisor_endpoint:SupervisorEndpoint, 
                module:str, data:models.Cluster):
        self.__cluster_endpoint = cluster_endpoint
        self.__supervisor_endpoint = supervisor_endpoint
        self.module = module
        self.data = data
    
    def execute(self, config: str) -> models.Supervisor:
        provision_response, exception = self.__supervisor_endpoint.provision(
            module=self.module, 
            cluster=self.data.identifier, 
            config=config
            )
        
        if exception is not None:
            return None
        
        supervisor, exception = self.__supervisor_endpoint.get(
            module=self.module, 
            cluster=self.data.identifier,
            id=provision_response.id
            )
       
        if exception is not None:
            return None
        
        return supervisor

class Configs:
    
    def __init__(self, config_endpoint: ConfigEndpoint, module:str):
        self.__config_endpoint = config_endpoint
        self.module = module
    
    def get(self, config:str) -> models.Config:
        return self.__config_endpoint.get(self.module, config)
    
    def create(self, config:models.Config) -> Exception:
        return self.__config_endpoint.create(self.module, config)


class ModuleEndpoints:
    
    def __init__(self, module_endpoint:ModuleEndpoint, cluster_endpoint:ClusterEndpoint,
                       supervisor_endpoint:SupervisorEndpoint, config_endpoint:ConfigEndpoint) -> None:
        self.module = module_endpoint
        self.cluster = cluster_endpoint
        self.supervisor = supervisor_endpoint
        self.config = config_endpoint


class Module:
    
    def __init__(self, endpoints:ModuleEndpoints, data:models.Module):
        self.__endpoints = endpoints
        self.data = data
    
    def clusters(self) -> list[Cluster]:
        cluster_data_list, exception = self.__cluster_endpoint.get(self.data.identifier)
        
        if exception is not None:
            return []
        
        cluster_list = []
        
        for cluster_data in cluster_data_list:
            cluster_list.append(Cluster(
                cluster_endpoint=self.__endpoints.cluster,
                supervisor_endpoint=self.__endpoints.supervisor,
                module=self.data.identifier,
                data=cluster_data
            ))
        
        return cluster_list
    
    def cluster(self, name:str) -> Cluster:
        cluster_data_list, exception = self.__cluster_endpoint.get(self.data.identifier)
        
        if exception is not None:
            return None
        
        for cluster_data in cluster_data_list:
            if name == cluster_data.identifier:
                return Cluster(
                    cluster_endpoint=self.__endpoints.cluster,
                    supervisor_endpoint=self.__endpoints.supervisor,
                    module=self.data.identifier,
                    data=cluster_data
                )

        return None
    
    def configs(self) -> Configs:
        return Configs(self.__endpoints.config, self.data.identifier) 


class NodeEndpoints:
    
    def __init__(self, host: str):
        self.debug = DebugEndpoint(host)
        self.module = ModuleEndpoint(host)
        self.cluster = ClusterEndpoint(host)
        self.supervisor = SupervisorEndpoint(host)
        self.config = ConfigEndpoint(host)

class Node:
    
    def __init__(self, host: str):
        self.__endpoints = NodeEndpoints(host)
    
    def modules(self) -> list[Module]:
        data_modules, exception = self.__endpoints.module.get_all()
        
        if exception is not None:
            return []
        
        module_list = []
        
        for data_module in data_modules:
            module_list.append(Module(
                endpoints=ModuleEndpoints(
                    module_endpoint=self.__endpoints.module,
                    config_endpoint=self.__endpoints.config,
                    cluster_endpoint=self.__endpoints.cluster,
                    supervisor_endpoint=self.__endpoints.supervisor
                ),
                data=data_module,
            ))

        return module_list
    
    def module(self, name:str) -> Module:
        data_modules, exception = self.__endpoints.module.get_all()
        
        if exception is not None:
            return None
        
        for data_module in data_modules:
            if data_module.identifier == name:
                return Module(
                    endpoints=ModuleEndpoints(
                        module_endpoint=self.__endpoints.module,
                        config_endpoint=self.__endpoints.config,
                        cluster_endpoint=self.__endpoints.cluster,
                        supervisor_endpoint=self.__endpoints.supervisor
                    ),
                    data=data_module,
                )
        
        return None
    
    def shutdown(self) -> bool:
        return self.__endpoints.debug.shutdown()
    
    def debug(self) -> bool:
        try:
            return self.__endpoints.debug.toggle_debug()
        except ConnectionRefusedError:
            return False
    
    def ping(self) -> (bool, int):
        return self.__endpoints.debug.ping()


if __name__ == "__main__":
    
    node = Node(host="http://127.0.0.1:8136")
    
    # turn debug mode OFF
    node.toggle_debug() 
    
    # turn debug mode ON
    node.toggle_debug()
    
    # check health of node
    success, delay = node.ping()
    if success:
        print(f"health check took {delay}ns")
    
    module_list = node.modules()
    print(module_list)
    
    common_module = node.module(name="common")
    print(common_module.data)
    
    common_module_clusters = common_module.clusters()
    print(common_module_clusters)
    
    vector_cluster = common_module.cluster(name="Vec")
    print(vector_cluster.data)
    
    supervisor = vector_cluster.execute(config="Vec")
    print(supervisor)
    
    # if not node.shutdown():
    #     print("failed to shutdown node")
    # else:
    #     print("node shutdown successfully")