import time
from threading import Thread


def display(content):
    while True:
        print(content, end="", flush=True)
        time.sleep(0.1)


def main():
    Thread(target=display, args=("Ping",), daemon=True).start()
    Thread(target=display, args=("Pong",), daemon=True).start()
    time.sleep(5)


if __name__ == "__main__":
    main()
