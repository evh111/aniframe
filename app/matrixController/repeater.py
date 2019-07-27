from threading import Timer

class Repeater:
    """
    Simple wrapper around a timer that keeps
    itself going once we start it.
    """

    def __init__(self, interval, func):
        self.interval = interval
        self.func = func
        self.timer = None

    def start(self):
        # the actual timer calls THIS method again,
        # instead of the wrapped function.
        self.timer = Timer(self.interval, self.start)
        # But then this method just calls the wrapped 
        # function
        self.func()
        self.timer.start()
