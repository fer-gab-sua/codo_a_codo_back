from flask import Blueprint, render_template, request, abort , redirect, url_for
from flask_login import current_user, login_required
from models import User , Mochilas, Mochila, db 
import requests

my_profile_routes = Blueprint('my_profile', __name__)

def clima():
        api_key = '1d93bc91eeb6a258d8c2ee0bf8475bb1'
        cityid = 3858765
        url = f'https://api.openweathermap.org/data/2.5/weather?id={cityid}&appid={api_key}&units=metric&lang=es'

        response = requests.get(url)
        weather_data = response.json()
        if response.status_code == 200:
            weather = {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],  # Temperatura actual en Celsius
                'temperature_max': weather_data['main']['temp_max'],  # Temperatura máxima en Celsius
                'temperature_min': weather_data['main']['temp_min'],  # Temperatura mínima en Celsius
                'sensacion_termica' : weather_data['main']['feels_like'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon']
            }
            return weather
        else:
            return ''

@my_profile_routes.route('/myprofile', methods=['GET'])
@login_required
def myprofile():
    mochilas_list = Mochilas.query.filter_by(user_id=current_user.user_id).all()
    weather = clima()
    return render_template('myprofile.html', 
                           user=current_user, 
                           mochilas_list=mochilas_list, 
                           weather=weather)

@my_profile_routes.route('/myprofile/new_mochila', methods=['GET', 'POST'])
@login_required
def new_mochila():
    if request.method == 'POST':
        nombre = request.form['nombre_mochila']
        descripcion = request.form['descripcion_mochila']
        
        # Crear una nueva instancia de Mochilas
        nueva_mochila = Mochilas(user_id=current_user.user_id, nombre=nombre, descripcion=descripcion)
        
        # Agregar y confirmar la nueva mochila en la base de datos
        db.session.add(nueva_mochila)
        db.session.commit()
        
        return redirect(url_for('my_profile.myprofile'))

    return redirect(url_for('my_profile.myprofile'))
    


@my_profile_routes.route('/myprofile/delete_mochila/<int:mochila_id>', methods=['POST'])
@login_required
def delete_mochila(mochila_id):
    mochila = Mochilas.query.get_or_404(mochila_id)
    if mochila.user_id != current_user.user_id:
        abort(403)  # Forbidden: No tienes permisos para borrar esta mochila
    db.session.delete(mochila)
    db.session.commit()
    return redirect(url_for('my_profile.myprofile'))


@my_profile_routes.route('/myprofile/delete_item/<int:item_id>', methods=['POST'])
@login_required
def delete_item(item_id):
    item = Mochila.query.filter_by(id=item_id).first()
    if not item:
        abort(404)
    mochila_id = item.mochila_id

    print("--------------------------------------------------------------------------------------")
    print( mochila_id )
    mochilas_list = Mochilas.query.filter_by(user_id=current_user.user_id).all()
    mochila_select = Mochilas.query.filter_by(id=mochila_id).first()
    
    weather = clima()


    db.session.delete(item)
    db.session.commit()
    contenido_mochila= Mochila.query.filter_by(mochila_id=mochila_id).all()
    return render_template('myprofile.html', 
                           user=current_user, 
                           mochilas_list=mochilas_list,
                           mochila_select=mochila_select,
                           contenido_mochila=contenido_mochila, 
                           weather=weather
                           )




@my_profile_routes.route('/myprofile/update_mochila/<int:mochila_id>', methods=['POST'])
@login_required
def update_mochila(mochila_id): ##Seria mas un select mochila para que pueda visualizar el detalle de las mochilas
    mochilas_list = Mochilas.query.filter_by(user_id=current_user.user_id).all()
    mochila_select = Mochilas.query.filter_by(id=mochila_id).first()
    contenido_mochila= Mochila.query.filter_by(mochila_id=mochila_id).all()
    weather = clima()
    return render_template('myprofile.html', 
                           user=current_user, 
                           mochilas_list=mochilas_list,
                           mochila_select=mochila_select,
                           contenido_mochila=contenido_mochila, 
                           weather=weather
                           )



@my_profile_routes.route('/myprofile/new_item/<int:mochila_id>', methods=['GET', 'POST'])
@login_required
def new_item(mochila_id):
    if request.method == 'POST':
        nombre = request.form['contenido']
        descripcion = request.form['cantidad']
        
        
        # Crear una nueva instancia de Mochilas
        nuevo_item = Mochila(mochila_id=mochila_id, contenido=nombre,  cantidad=descripcion)
        
        # Agregar y confirmar la nueva mochila en la base de datos
        db.session.add(nuevo_item)
        db.session.commit()

        mochilas_list = Mochilas.query.filter_by(user_id=current_user.user_id).all()
        mochila_select = Mochilas.query.filter_by(user_id=current_user.user_id, id=mochila_id).first()

        contenido_mochila = Mochila.query.filter_by(mochila_id=mochila_select.id).all()

        weather = clima()
        return render_template('myprofile.html', 
                           user=current_user, 
                           mochilas_list=mochilas_list,
                           mochila_select=mochila_select,
                           contenido_mochila=contenido_mochila, 
                           weather=weather
                           )

    elif request.method == 'GET':
        mochila = Mochila.query.filter_by(mochila_id=mochila_id)
        mochilas = Mochilas.query.filter_by(user_id=current_user.user_id).all()
        return render_template('myprofile.html', user=current_user, mochila_select=mochila_select, mochilas=mochilas,  weather=weather)













