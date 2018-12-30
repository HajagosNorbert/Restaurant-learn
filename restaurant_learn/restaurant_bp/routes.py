from flask import render_template, redirect, request, url_for, flash, jsonify, Blueprint
from restaurant_learn import db
from restaurant_learn.database_setup import Restaurant, MenuItem

restaurant_bp = Blueprint('restaurant_bp', __name__)


@restaurant_bp.route('/create/', methods=['GET', 'POST'])
def createRestaurant():
    if request.method == 'GET':
        return render_template('createRestaurant.html')
    if request.method == 'POST':
        if request.form:
            name = request.form['name']
            restaurant = Restaurant(name=name)
            db.session.add(restaurant)
            flash('created!')
            db.session.commit()
            return redirect(url_for('main_bp.restaurants'))


@restaurant_bp.route('/<int:restaurant_id>/')
@restaurant_bp.route('/<int:restaurant_id>/menu/')
def restaurant(restaurant_id):
    try:
        restaurant = db.session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        menu_items = db.session.query(MenuItem).filter_by(
            restaurant_id=restaurant.id)
        return render_template('restaurant.html', restaurant=restaurant, menu_items=menu_items)

    except(AttributeError):
        return(('Rossz id', 404))


@restaurant_bp.route('/<int:restaurant_id>/json/')
@restaurant_bp.route('/<int:restaurant_id>/menu/json/')
def restaurantJson(restaurant_id):
    try:
        menu_items = db.session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id).all()
        return jsonify([menu_item.serialize for menu_item in menu_items])

    except(AttributeError):
        return('Rossz id', 404)


@restaurant_bp.route('/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'GET':
        return render_template('editRestaurant.html', restaurant=restaurant)
    if request.method == 'POST':
        if request.form:
            restaurant.name = request.form['name']
            db.session.add(restaurant)
            flash('Edited')
            db.session.commit()
            return redirect(url_for('main_bp.restaurant', restaurant_id=restaurant.id))


@restaurant_bp.route('/<int:restaurant_id>/menu/delete', methods=['GET', 'POST'])
@restaurant_bp.route('/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'GET':
        return render_template('deleteRestaurant.html', restaurant=restaurant)
    if request.method == 'POST':
        if request.form:
            db.session.delete(restaurant)
            flash('Deleted!')
            db.session.commit()
            return redirect(url_for('main_bp.restaurants'))
