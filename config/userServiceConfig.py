import requests


class UserServiceConfiguration:

    class __UserServiceConfiguration:

        def __init__(self):
            try:
                config = requests.get('http://127.0.0.1:8888/v1/configurations/db').json()
                self.HOST: str = config["host"]
                self.USER: str = config["user"]
                self.PASSWORD: str = config["password"]
                self.DB: str = config["database"]
                self.CHARSET: str = config["charset"]
            except ConnectionError as con_err:
                print("Configuration Service Error: ConnectionError : ")
                print(con_err)
            except TimeoutError as timeout_err:
                print("Configuration Service Error: TimeoutError : ")
                print(timeout_err)

    instance = None

    def __init__(self):
        if not UserServiceConfiguration.instance:
            UserServiceConfiguration.instance = UserServiceConfiguration.__UserServiceConfiguration()
