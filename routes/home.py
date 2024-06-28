from flask import Blueprint,render_template



home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def home():
    return render_template('index.html')



@home_routes.route('/refugios')
def refugios():
    print("aca lleguo refu")
    return render_template('refugios.html')


@home_routes.route('/actividades')
def actividades():
    return render_template('actividades.html')


@home_routes.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


    
