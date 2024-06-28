from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, unique=True)
    use_str_email = db.Column(db.String(120), unique=True)
    use_str_password = db.Column(db.String(128), nullable=False)
    use_str_first_name = db.Column(db.String(100),nullable=True, default= '')
    use_str_last_name = db.Column(db.String(100), nullable=True, default= '')
    use_str_phone = db.Column(db.String(15), nullable=True, default= '')
    is_active = db.Column(db.Boolean, default=True)
    
    backpacks = db.relationship('Mochilas', backref='owner', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.use_str_email

    def set_password(self, password):
        self.use_str_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.use_str_password, password)
    
    def get_id(self):
        return str(self.user_id)  
    
    
    @property
    def is_authenticated(self):
        # Devuelve True si el usuario está autenticado, False en caso contrario.
        return True  # Puedes implementar lógica personalizada aquí según necesites.

    @property
    def is_active(self):
        # Devuelve True si el usuario está activo, False en caso contrario.
        return True

    @property
    def is_anonymous(self):
        # Devuelve True si el usuario es anónimo, False en caso contrario.
        return False  # En tu caso, si los usuarios siempre están autenticados, puede ser False

class Mochilas(db.Model):
    __tablename__ = 'mochilas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    mochila_details = db.relationship('Mochila', backref='mochilas', lazy=True)

class Mochila(db.Model):
    __tablename__ = 'mochila'
    id = db.Column(db.Integer, primary_key=True)
    mochila_id = db.Column(db.Integer, db.ForeignKey('mochilas.id'), nullable=False)
    contenido = db.Column(db.String(200), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)