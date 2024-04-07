import os


class Config:
    prod: bool

    def __init__(self):
        self.prod = os.environ.get('PRODUCTION', 'false')


def get_config() -> Config:
    return Config()
