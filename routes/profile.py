from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from models import User , Mochilas, Mochila, db # Asegúrate de importar tu modelo de usuario adecuadamente





my_profile_routes = Blueprint('my_profile', __name__)

@my_profile_routes.route('/myprofile', methods=['GET'])
@login_required
def myprofile():
    # current_user contiene el usuario autenticado actualmente
    if current_user:
        mochilas = Mochilas.query.filter_by(user_id=current_user.user_id).all()

        return render_template('myprofile.html', user=current_user, mochilas=mochilas)
    else:
        # En teoría, no deberíamos llegar aquí gracias a @login_required
        return "Usuario no autenticado"
    

@my_profile_routes.route('/myprofile/new_mochila', methods=['GET', 'POST'])
@login_required
def new_mochila():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        
        # Crear una nueva instancia de Mochilas
        nueva_mochila = Mochilas(user_id=current_user.user_id, nombre=nombre, descripcion=descripcion)
        
        # Agregar y confirmar la nueva mochila en la base de datos
        db.session.add(nueva_mochila)
        db.session.commit()
        mochila = Mochila.query.filter_by(mochila_id=1)
        mochilas = Mochilas.query.filter_by(user_id=current_user.user_id).all()
        return render_template('myprofile.html', user=current_user , mochilas=mochilas, mochila=mochila)

    elif request.method == 'GET':
        mochila = Mochila.query.filter_by(mochila_id=1)
        mochilas = Mochilas.query.filter_by(user_id=current_user.user_id).all()
        return render_template('myprofile.html', user=current_user , mochilas=mochilas, mochila=mochila)
    


@my_profile_routes.route('/myprofile/new_item', methods=['GET', 'POST'])
@login_required
def new_item():
    if request.method == 'POST':
        mochila_id = request.form['id_mochila']
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        
        # Crear una nueva instancia de Mochilas
        nuevo_item = Mochila(mochila_id=mochila_id , cantidad=cantidad, contenido=nombre)
        
        # Agregar y confirmar la nueva mochila en la base de datos
        db.session.add(nuevo_item)
        db.session.commit()
        
        mochilas = Mochilas.query.filter_by(user_id=current_user.user_id).all()
        mochila = Mochila.query.filter_by(id=mochila_id)
        if mochila:
            return render_template('myprofile.html', user=current_user , mochilas=mochilas, mochila=mochila)
        else:
            return render_template('myprofile.html', user=current_user)
    
    return render_template('myprofile.html', user=current_user , mochilas=mochilas)