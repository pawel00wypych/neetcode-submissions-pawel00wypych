class Logger:

    def __init__(self):
        self.allowed_timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.allowed_timestamps and self.allowed_timestamps[message] > timestamp:
            return False
        else:
            self.allowed_timestamps[message] = timestamp + 10
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
