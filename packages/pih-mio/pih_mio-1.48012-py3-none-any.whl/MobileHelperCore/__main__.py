def start() -> None:
    from MobileHelperCore.service import A, Service, checker, as_developer
    print(A.O.green_str(f"As developer: {as_developer()}"))
    Service(10, checker).start()

if __name__ == '__main__':
    start()
