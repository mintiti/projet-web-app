import flask
from database.models import *
from database.database_init import *

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"


def clean():
    db.drop_all()
    db.create_all()
    initialize_ingredients()
    initialize_desserts()
    initialize_drinks()
    initialize_sandwiches()
    initialize_users()
    initialize_menu_prices()

    return "Cleaned!"


db.init_app(app)

with app.test_request_context():
    clean()


@app.route("/test")
def test():

    # # Create two sports
    # judo = Sport(name="judo")
    # football = Sport(name="football")
    # db.session.add(judo)
    # db.session.add(football)
    # db.session.commit()
    #
    # # Create three players
    # player1 = Player(firstname="Jonathan", lastname="Pastor")
    # player2 = Player(firstname="Hervé", lastname="Dupont")
    # player3 = Player(firstname="André", lastname="Laroute")
    # db.session.add(player1)
    # db.session.add(player2)
    # db.session.add(player3)
    # db.session.commit()
    #
    # # Create a team with the two players
    # rocket = Team(name="rocket", sport=judo)
    # sonette = Team(name="sonette", sport=football)
    # db.session.add(rocket)
    # db.session.add(sonette)
    # db.session.commit()
    # #
    # # # Add the two players to the team 'rocket'
    # # rocket.players.append(player1)
    # # rocket.players.append(player2)
    # # db.session.add(rocket)
    # # # Add the two players to the team 'sonette'
    # # sonette.players.append(player2)
    # # sonette.players.append(player3)
    # # db.session.commit()
    # # # Remove one player from the team 'sonette'
    # # sonette.players.remove(player3)
    # # db.session.add(sonette)
    # # db.session.commit()
    #
    # # Fetch all sports
    # sports = Sport.query.all()
    #
    # return flask.render_template("index.jinja2", sports=sports)

    return flask.render_template("base.html.jinja2")


@app.route("/")
def home():
    return flask.render_template("base.html.jinja2")


@app.route("/sandwichs")
def sandwichs():
    sandwiches = Products.query.filter(Products.food_type == SANDWICH).all()
    return flask.render_template("sandwiches.html.jinja2", products=sandwiches)


@app.route("/boissons")
def boissons():
    drinks = Products.query.filter(Products.food_type == DRINK).all()
    return flask.render_template("boissons.html.jinja2", products=drinks)


@app.route("/menus")
def menus():
    pr = Products.query.filter(Products.id == 5).all()[0]
    return flask.render_template("menus.html.jinja2", product=pr)


@app.route("/desserts")
def desserts():
    des = Products.query.filter(Products.food_type == DESSERT).all()
    return flask.render_template("desserts.html.jinja2", products = des)


if __name__ == '__main__':
    app.run(debug=True)

