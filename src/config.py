class Config(object):
    DEBUG = False
    TESTING = False
    SLACK_URL = "https://hooks.slack.com/services/data/data/data"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = False


CFG_MAP = {
    'develop': DevelopmentConfig(),
    'testing': TestingConfig()
}


def get_cfg(value):
    return CFG_MAP.get(value, DevelopmentConfig())

