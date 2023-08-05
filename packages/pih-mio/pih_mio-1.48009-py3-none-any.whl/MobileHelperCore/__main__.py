def start() -> None:
    from service import A, Service, checker, as_developer
    A.O.green(f"As developer: {as_developer()}")
    Service(10, checker).start()

if __name__ == '__main__':
    start()
