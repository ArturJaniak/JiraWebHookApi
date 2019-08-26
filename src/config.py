class Config(object):
    DEBUG = False
    TESTING = False
    SLACK_URL = "https://hooks.slack.com/services/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"


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

