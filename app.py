import flask
from database.models import *

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"


db.init_app(app)

with app.test_request_context():
    db.create_all()


# @app.route("/clean")
def clean():
    db.drop_all()
    db.create_all()
    return "Cleaned!"


@app.route("/test")
def test():
    clean()

    # Create two sports
    judo = Sport(name="judo")
    football = Sport(name="football")
    db.session.add(judo)
    db.session.add(football)
    db.session.commit()

    # Create three players
    player1 = Player(firstname="Jonathan", lastname="Pastor")
    player2 = Player(firstname="Hervé", lastname="Dupont")
    player3 = Player(firstname="André", lastname="Laroute")
    db.session.add(player1)
    db.session.add(player2)
    db.session.add(player3)
    db.session.commit()

    # Create a team with the two players
    rocket = Team(name="rocket", sport=judo)
    sonette = Team(name="sonette", sport=football)
    db.session.add(rocket)
    db.session.add(sonette)
    db.session.commit()

    # Add the two players to the team 'rocket'
    rocket.players.append(player1)
    rocket.players.append(player2)
    db.session.add(rocket)
    # Add the two players to the team 'sonette'
    sonette.players.append(player2)
    sonette.players.append(player3)
    db.session.commit()
    # Remove one player from the team 'sonette'
    sonette.players.remove(player3)
    db.session.add(sonette)
    db.session.commit()

    # Fetch all sports
    sports = Sport.query.all()

    return flask.render_template("index.jinja2", sports=sports)


if __name__ == '__main__':
    app.run(debug=True)
