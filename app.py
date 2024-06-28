from flask import Flask
from models import db ,User
from routes.home import home_routes
from routes.auth import auth_routes
from routes.profile import my_profile_routes
from config import config
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app_config = config['development']
    
    # Crear la aplicación Flask
    app = Flask(__name__, template_folder=app_config.TEMPLATE_DIR, static_folder=app_config.STATIC_DIR)
    
    # Aplicar configuración
    app.config.from_object(app_config)

    # Inicializar la base de datos
    db.init_app(app)

    # Configuración para Flask-Login

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    

    # Registrar los Blueprints
    app.register_blueprint(home_routes)
    app.register_blueprint(my_profile_routes, url_prefix='/profile')
    app.register_blueprint(auth_routes)
    
    return app

# Crear la aplicación utilizando la función factory create_app
app = create_app()

# Crear todas las tablas definidas en los modelos
with app.app_context():
    db.create_all()

# Iniciar el servidor de desarrollo si se ejecuta este script directamente
if __name__ == '__main__':
    app.run(debug=True)