ENV = "dev"


class DefaultConfig:
    port = 8080


class ProdConfig(DefaultConfig):
    host = "0.0.0.0"
    workers = 4
    reload = False


class DevConfig(DefaultConfig):
    host = "localhost"
    workers = 1
    reload = True


config = ProdConfig if ENV == "prod" else DevConfig
