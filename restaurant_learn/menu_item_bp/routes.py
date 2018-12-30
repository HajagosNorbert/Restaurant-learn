from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, Blueprint
from restaurant_learn import db
from restaurant_learn.database_setup import Restaurant, MenuItem

menu_item_bp = Blueprint('menu_item_bp', __name__)


@menu_item_bp.route('/menu/create/', methods=['GET', 'POST'])
def createMenuItem(restaurant_id):
    if request.method == 'GET':
        return render_template('createMenuItem.html', restaurant_id=restaurant_id)
    if request.method == 'POST':
        name = request.form['name']
        menu_item = MenuItem(name=name, restaurant_id=restaurant_id)
        db.session.add(menu_item)
        flash('Item added!')
        db.session.commit()

        return redirect(url_for('main_bp.restaurant', restaurant_id=restaurant_id))


@menu_item_bp.route('/menu/<int:menu_item_id>/')
def menuItem(restaurant_id, menu_item_id):
    menu_item = db.session.query(MenuItem).filter_by(id=menu_item_id).one()
    return render_template('menuItem.html', menu_item=menu_item)


@menu_item_bp.route('/menu/<int:menu_item_id>/json/')
def menuItemJson(restaurant_id, menu_item_id):
    menu_item = db.session.query(MenuItem).filter_by(id=menu_item_id).one()
    return jsonify(menu_item.serialize)


@menu_item_bp.route('/menu/<int:menu_item_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_item_id):
    try:
        menu_item = db.session.query(MenuItem).filter_by(id=menu_item_id).one()
    except:
        return 'No item with this id', 404

    if request.method == 'GET':
        return render_template('editMenuItem.html', restaurant_id=restaurant_id, menu_item=menu_item)
    if request.method == 'POST':
        newName = request.form['name']
        menu_item.name = newName
        db.session.add(menu_item)
        flash('Item modified!')
        db.session.commit()
        return redirect(url_for('main_bp.restaurant', restaurant_id=restaurant_id))


@menu_item_bp.route('/menu/<int:menu_item_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_item_id):
    try:
        menu_item = db.session.query(MenuItem).filter_by(id=menu_item_id).one()
    except:
        return 'No item with this id', 404

    if request.method == 'GET':
        return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, menu_item=menu_item)

    if request.method == 'POST':
        if not request.form:
            return 'Only valid ways to delete for you'
        db.session.delete(menu_item)
        flash('Item delete!')
        db.session.commit()
        return redirect(url_for('main_bp.restaurant', restaurant_id=restaurant_id))
