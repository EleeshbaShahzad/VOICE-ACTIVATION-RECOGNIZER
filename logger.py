from collections import deque

class Logger:

    def __init__(self):
        self.logs = deque(maxlen=20)  # FIFO queue

    def add(self, item):
        self.logs.append(item)

    def show(self):
        return list(self.logs)