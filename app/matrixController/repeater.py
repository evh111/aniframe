from threading import Timer
import threading
import time


class Repeater:
    """
    Simple wrapper around a timer that keeps
    itself going once we start it.
    """

    def __init__(self, interval, func):
        self.interval = interval
        self.func = func
        self.timer = None
        self.startTime = time.time()

    def setInterval(self, interval):
        self.interval = interval

    def pause(self):
        self.timer.cancel()

    def resume(self):
        self.timer.cancel()
        self.start()

    def start(self):
        # the actual timer calls THIS method again,
        # instead of the wrapped function.
        self.timer = Timer(self.interval, self.start)
        # But then this method just calls the wrapped
        # function
        self.func()
        self.timer.start()
