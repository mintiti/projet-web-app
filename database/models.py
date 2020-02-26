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
