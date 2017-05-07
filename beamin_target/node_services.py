import os
import subprocess
import json


class NodeServices():
    def __init__(self, node_path='node'):
        self.node_path = node_path
        self.processes = []

    def start(self):
        self.stop()

        for service in self.get_services() :
            service_path = os.path.join(self.node_path, service)
            process = subprocess.Popen(['python3', service_path])
            self.processes.append(process)

    def stop(self):
        for process in self.processes:
            process.terminate()

    def restart():
        self.stop()
        self.start()

    def get_services(self):
        services_data = os.path.join(self.node_path, 'data_services.json')
        return json.load(open(services_data))['services']
