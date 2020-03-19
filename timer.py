import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    #Create new timer
    def __init__(self):
        self._start_time = None

    #Start referenced timer
    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    #Stop referenced timer
    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return elapsed_time