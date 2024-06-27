from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    use_int_id = db.Column(db.Integer, primary_key=True, unique=True)
    use_str_email = db.Column(db.String(120), unique=True)
    use_str_password = db.Column(db.String(128), nullable=False)
    use_str_first_name = db.Column(db.String(100),nullable=True, default= '')
    use_str_last_name = db.Column(db.String(100), nullable=True, default= '')
    use_str_phone = db.Column(db.String(15), nullable=True, default= '')


    def __repr__(self):
        return '<User %r>' % self.use_str_email

    def set_password(self, password):
        self.use_str_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.use_str_password, password)