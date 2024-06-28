from flask import Blueprint, render_template, request, redirect, g, url_for, flash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity , verify_jwt_in_request
from models import db, User

# Crear blueprints para cada conjunto de rutas



my_profile_routes = Blueprint('my_profile_routes', __name__)





