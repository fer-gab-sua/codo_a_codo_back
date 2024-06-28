from flask import Blueprint, render_template
from flask_login import current_user, login_required
from models import User  # Asegúrate de importar tu modelo de usuario adecuadamente



my_profile_routes = Blueprint('my_profile', __name__)

@my_profile_routes.route('/myprofile', methods=['GET'])
@login_required
def myprofile():
    # current_user contiene el usuario autenticado actualmente
    if current_user:
        return render_template('myprofile.html', user=current_user)
    else:
        # En teoría, no deberíamos llegar aquí gracias a @login_required
        return "Usuario no autenticado"