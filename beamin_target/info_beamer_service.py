import subprocess


class InfoBeamerService():
    def __init__(self, config):
        self.config = config
        self.cmd = config["info_beamer_cmd"]
        self.node_path = 'node'

    def start(self):
        subprocess.run([self.cmd, self.node_path], stderr=subprocess.STDOUT)
