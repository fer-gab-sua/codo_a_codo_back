from flask import Blueprint, render_template, request, redirect, url_for , flash ,current_app
from flask_login import login_user, logout_user, login_required
from models import User,  db
import os
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
auth_routes = Blueprint('auth', __name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



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
        file = request.files['profile_picture']
        
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

        # Ahora el new_user tiene el user_id asignado
        user_id = new_user.user_id

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            nuevonombrefile = f"{user_id}{extension}"
            upload_path = os.path.join(current_app.config['STATIC_DIR'], 'archivos')
            os.makedirs(upload_path, exist_ok=True)
            file.save(os.path.join(upload_path, nuevonombrefile))

            # Actualizar la imagen de perfil en la base de datos
            new_user.set_profile_img(nuevonombrefile)
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