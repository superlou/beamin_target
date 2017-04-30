import subprocess


class InfoBeamerService():
    def __init__(self, config):
        self.config = config
        self.cmd = config["info_beamer_cmd"]
        self.node_path = 'node'
        self.process = None

    def start(self):
        if self.process is None:
            self.process = subprocess.Popen([self.cmd, self.node_path],
                                            stderr=subprocess.STDOUT)

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None

    def restart(self):
        self.stop()
        self.start()

    def is_running(self):
        if not self.process:
            return False

        if self.process.poll():
            # poll sets and returns returncode if the process has terminated
            return False
        else:
            return True
