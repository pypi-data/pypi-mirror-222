from service import A, Service, checker, as_developer

def start() -> None:
    A.O.green(f"As developer: {as_developer()}")
    Service(10, checker).start()

if __name__ == '__main__':
    start()
