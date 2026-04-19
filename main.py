from engine import Engine
import config


class App:

    def __init__(self):
        self.engine = Engine()

    def run(self):

        print(f"{config.APP_NAME} v{config.VERSION}")

        while True:

            cmd = input("\nEnter command: ")

            if cmd == "exit":
                break

            elif cmd == "logs":
                print(self.engine.get_logs())

            else:
                result = self.engine.process(cmd)
                print(result)


if __name__ == "__main__":
    App().run()