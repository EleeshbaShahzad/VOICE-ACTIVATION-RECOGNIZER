import datetime
import webbrowser
from logger import Logger


class Engine:

    def __init__(self):

        self.commands = {
            "time": self.time,
            "chrome": self.chrome,
            "search": self.search
        }
        self.logger = Logger()
    def time(self, cmd):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"Time: {now}"
    def chrome(self, cmd):
        webbrowser.open("https://google.com")
        return "Chrome opened"
    def search(self, cmd):
        q = cmd.replace("search", "").strip()
        webbrowser.open(f"https://google.com/search?q={q}")
        return f"Searching: {q}"
    def process(self, cmd):
        cmd = cmd.lower().strip()
        self.logger.add(cmd)
        for key in self.commands:
            if key in cmd:
                return self.commands[key](cmd)
        return "Unknown command"
    def get_logs(self):
        return self.logger.show()