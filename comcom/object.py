import os

import procedural


class CommandRunner(object):
    def __init__(self):
        procedural.init()
        self.closed = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.closed:
            procedural.destroy()
            self.closed = True

    def run_command(self, input, file, argv, env=os.environ, timeout=-1):
        procedural.run_command(input, file, argv, env, timeout)
