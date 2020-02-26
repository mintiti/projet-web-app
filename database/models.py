from database.database import db


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
sandwich_ingredients_junction_table = db.Table('recettes_sandwich')


# Food Tables
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


# Nourriture à la carte

class Sandwich(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    prix = db.Column(db.Float)
    stock = db.Column(db.Integer)
    ingredients = db.relationship('Ingredient', backref='sandwiches', secondary=sandwich_ingredients_junction_table)


class Boisson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    prix = db.Column(db.Float)


class Viennoiserie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    prix = db.Column(db.Float)


# Menus
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sandwich = db.Column(db.Integer, db.ForeignKey('sandwich.id'))
    boisson = db.Column(db.Integer, db.ForeignKey('boisson.id'))
    dessert = db.Column(db.Integer, db.ForeignKey('viennoiserie.id'))


class PrixMenu(db.Model):
    sandwich_principal = db.Column(db.Integer, db.ForeignKey('sandwich.id'), primary_key=True)
    prix = db.Column(db.Float)


# Commandes
class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commande_le = db.Column(db.DateTime)
    pour_le = db.Column(db.DateTime)
    livre = db.Column(db.Boolean)
    commandeur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))

class CommandeItem(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('commande.id'))
    item = 