from restaurant_learn import db


class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    name = db.Column(db.String(250), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
        }


class MenuItem(db.Model):
    __tablename__ = 'menu_item'

    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course,
        }
