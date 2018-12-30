from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from restaurant_learn.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from restaurant_learn.restaurant_bp.routes import restaurant_bp
    from restaurant_learn.menu_item_bp.routes import menu_item_bp
    from restaurant_learn.user_bp.routes import user_bp, google_bp
    from restaurant_learn.main_bp.routes import main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(google_bp, url_prefix='/google_login')
    app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
    app.register_blueprint(
        menu_item_bp, url_prefix='/restaurants/<int:restaurant_id>/menu')

    return app
