from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db , User
from routes import home_routes , refugios_routes , auth_routes, my_profile_routes
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request
import os

# Obtener la ruta absoluta del directorio base del proyecto
base_dir = os.path.abspath(os.path.dirname(__file__))
# Definir la ruta de la base de datos SQLite en el directorio superior
db_path = os.path.join(base_dir, "producionDB.db")


def create_app():
    # Configurar los directorios de plantillas y archivos estáticos
    template_dir = os.path.join(base_dir, 'src', 'templates')
    static_dir = os.path.join(base_dir, 'src', 'static')

    # Crear la aplicación Flask
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    # Configurar la URI de la base de datos SQLite y opciones del motor SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_size': 20,
        'pool_timeout': 30,
    }
    app.config['SECRET_KEY'] = 'este_es_el_grupo_12_python' 
    app.config['JWT_SECRET_KEY'] = 'este_es_el_grupo_12_python'

    # Inicializar la extensión SQLAlchemy con la aplicación
    db.init_app(app)
    
    # Inicializar JWTManager con la aplicación Flask
    jwt = JWTManager(app)

    app.register_blueprint(home_routes)
    app.register_blueprint(refugios_routes)
    app.register_blueprint(my_profile_routes, url_prefix='/profile')
    app.register_blueprint(auth_routes)
    return app


# Crear la aplicación utilizando la función factory create_app
app = create_app()


@app.context_processor
def inject_user():
    current_user = None
    try:
        verify_jwt_in_request(optional=True)  # Verificar si hay JWT en la solicitud, pero no es obligatorio
        current_user_id = get_jwt_identity()
        if current_user_id:
            current_user = User.query.get(current_user_id)
    except:
        pass  # Maneja cualquier error al verificar el JWT

    return {'current_user': current_user}
    
# Entrar al contexto de la aplicación para asegurar que se creen las tablas de la base de datos
with app.app_context():
    db.create_all()

# Iniciar el servidor de desarrollo si se ejecuta este script directamente
if __name__ == '__main__':
    app.run(debug=True)