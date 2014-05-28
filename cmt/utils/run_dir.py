import os

class RunDir(object):
    def __init__(self, dir, create=False):
        self._run_dir = dir
        self._create = create

    def __enter__(self):
        self._starting_dir = os.path.abspath(os.getcwd())
        if self._create and not os.path.isdir(self._run_dir):
            os.makedirs(self._run_dir)
        os.chdir(self._run_dir)

    def __exit__(self, type, value, traceback):
        os.chdir(self._starting_dir)


def open_run_dir(dir, **kwds):
    return RunDir(dir, **kwds)