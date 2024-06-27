from flask import Blueprint, render_template, request, redirect, g, url_for, flash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity , verify_jwt_in_request
from models import db, User

# Crear blueprints para cada conjunto de rutas
home_routes = Blueprint('home_routes', __name__)
refugios_routes = Blueprint('refugios_routes', __name__)
auth_routes = Blueprint('auth_routes', __name__)
my_profile_routes = Blueprint('my_profile_routes', __name__)



# Definir las rutas dentro de cada blueprint
@home_routes.route('/')
def home():
    return render_template('index.html')

@refugios_routes.route('/refugios')
def refugios():
    return render_template('refugios.html')

@my_profile_routes.route('/myprofile', methods=['GET'])
@jwt_required()
def myprofile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return render_template('myprofile.html', user=user)



@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form.get('nombre', '')
        last_name = request.form.get('apellido', '')
        phone = request.form.get('telefono', '')

        if User.query.filter_by(use_str_email=email).first():
            flash('El correo electrónico ya está registrado.')
            return redirect(url_for('auth_routes.register'))

        new_user = User(
            use_str_email=email,
            use_str_first_name=first_name,
            use_str_last_name=last_name,
            use_str_phone=phone
        )
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Usuario registrado con éxito.')
        return redirect(url_for('auth_routes.login'))

    return render_template('register.html')

@auth_routes.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        _correo = request.form["email"]
        _password = request.form["password"]
        user = User.query.filter_by(use_str_email=_correo).first()

        if user and user.check_password(_password):
            access_token = create_access_token(identity=user.use_int_id)
            print('inicio')
            flash('Inicio de sesión exitoso.')
            response = redirect(url_for('my_profile_routes.myprofile'))
            response.set_cookie('access_token', access_token, httponly=True, secure=False)  # Cambiar secure=True en producción
            return render_template('myprofile.html')
        else:
            flash("Usuario o contraseña incorrectos.")
            return render_template('login.html', mensaje="Usuario o contraseña incorrectos")

    return render_template('login.html')


