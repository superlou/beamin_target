import subprocess
import os


class InfoBeamerService():
    def __init__(self, config, node_path='node'):
        self.config = config
        self.cmd = config.get('info_beamer_cmd', 'info-beamer')
        self.is_raspberry_pi = config.get('raspberry_pi', True)
        self.node_path = node_path
        self.process = None

    def start(self):
        if self.process is None:
            env = os.environ.copy()

            if self.is_raspberry_pi:
                env['INFOBEAMER_BLANK_MODE'] = 'layer'

            self.process = subprocess.Popen([self.cmd, self.node_path],
                                            stderr=subprocess.STDOUT,
                                            env=env)

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
