from database.database import db
import datetime

# Constants
SANDWICH = 0
DRINK = 1
DESSERT = 2
MENU = 3


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


junction_table = db.Table('participation',
                          db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
                          db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
                          )


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'))
    sport = db.relationship('Sport', backref='teams')  # Sport <-> Team relationship
    players = db.relationship('Player', backref='teams', secondary=junction_table)  # Sport <-> Player relationship


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)


# Junction tables
items_ingredients_junction_table = db.Table('ingredients_in',
                                            db.Column('Produit', db.Integer, db.ForeignKey('products.id')),
                                            db.Column('Ingredient', db.Integer, db.ForeignKey('ingredients.id')))


# Ingredient Table
class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


# à la carte food
class Products(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    food_type = db.Column(db.Integer)  # Either SANDWICH , DRINK or DESSERT
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    ingredients = db.relationship('Ingredients', backref='Items', secondary=items_ingredients_junction_table)


# Menus
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sandwich = db.Column(db.Integer, db.ForeignKey('products.id'))
    boisson = db.Column(db.Integer, db.ForeignKey('products.id'))
    dessert = db.Column(db.Integer, db.ForeignKey('products.id'))


class PrixMenu(db.Model):
    sandwich_principal = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    prix = db.Column(db.Float)


# Commandes
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime)
    delivery_date = db.Column(db.DateTime, nullable=True)
    delivered = db.Column(db.Boolean)
    validated = db.Column(db.Boolean)
    ordered_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    paid = db.Column(db.Boolean)
    items = db.relationship("OrderItem")


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    item = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)


# Users
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
