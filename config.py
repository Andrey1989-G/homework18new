class Config(object):
    DEBAG = True
    #уникальный индикатор создания сессии
    #SECRET_HERE = '23oj2iju98ur98fiwj'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}