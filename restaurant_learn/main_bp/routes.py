from flask import  render_template, jsonify, Blueprint
from restaurant_learn import db
from restaurant_learn.database_setup import Restaurant

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/restaurants/')
@main_bp.route('/')
def restaurants():
    restaurants = db.session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants = restaurants)

@main_bp.route('/restaurants/json/')
@main_bp.route('/json/')
def restaurantsJson():
    restaurants = db.session.query(Restaurant).all()
    return(jsonify([restaurant.serialize for restaurant in restaurants]))