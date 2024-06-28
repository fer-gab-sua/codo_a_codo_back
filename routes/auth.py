from flask import Blueprint, render_template, request, redirect, url_for , flash
from flask_login import login_user, logout_user, login_required
from models import User,  db


from werkzeug.security import check_password_hash
auth_routes = Blueprint('auth', __name__)





@auth_routes.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        _correo = request.form["email"]
        _password = request.form["password"]
        user = User.query.filter_by(use_str_email=_correo).first()

        if user and check_password_hash(user.use_str_password, _password):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('my_profile.myprofile')) ######tegno que apuntar a la ruta protegida
        else:
            flash("Usuario o contraseña incorrectos.", 'error')
            return render_template('login.html', mensaje='Usuario o Contraseña Incorrecto')

    return render_template('login.html')

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
            return redirect(url_for('auth.register'))

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
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_routes.route('/logout')
def logout():
    # Lógica para cerrar sesión (limpieza de tokens, etc.)
    # Ejemplo básico de cierre de sesión:
    # logout_user()  # Esta función depende de cómo manejes la sesión o JWT
    logout_user()
    print("se cerro")

    return redirect(url_for('home_routes.home'))  # Redirige al inicio después del logout