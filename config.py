import os

class Config():
    SECRET_KEY = 'este_es_el_grupo_12_python'
    JWT_SECRET_KEY = 'este_es_el_grupo_12_python'

    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "producionDB.db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 20,
        'pool_timeout': 30,
    }
    SECRET_KEY = 'este_es_el_grupo_12_python' 
    JWT_SECRET_KEY = 'este_es_el_grupo_12_python'

class Rutes(Config):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'src', 'templates')
    STATIC_DIR = os.path.join(BASE_DIR, 'src', 'static')

class DevelopmentConfig(Rutes):
    DEBUG=True



config = {
    'development' : DevelopmentConfig
}