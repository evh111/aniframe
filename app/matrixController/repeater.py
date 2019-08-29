from threading import Timer
import threading
import time


class Repeater:
    """
    Simple wrapper around a timer that keeps
    itself going once we start it.
    """

    def __init__(self, timeout, callback, interval, func):
        self.interval = interval
        self.func = func
        self.timer = None
        self.timeout = timeout
        self.startTime = time.time()
        self.callback = callback

    def setInterval(self, interval):
        self.interval = interval

    def pause(self):
        self.timer.cancel()
        self.pauseTime = time.time()

    def resume(self):
        self.timer = threading.Timer(
            self.timeout - (self.pauseTime - self.startTime), self.callback)

        self.timer.start()

    def start(self):
        # the actual timer calls THIS method again,
        # instead of the wrapped function.
        self.timer = Timer(self.interval, self.start)
        # But then this method just calls the wrapped
        # function
        self.func()
        self.timer.start()
