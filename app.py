import flask
from database.models import *
from database.database_init import *
from database import API

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
    initialize_order_db()
    initialize_order_item()
    initialize_menu_prices()

    return "Cleaned!"


db.init_app(app)

with app.test_request_context():
    clean()


@app.route("/")
def home():
    return flask.render_template("base.html.jinja2")


@app.route("/sandwichs", methods=['GET', "POST"])
def sandwichs():
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_product_to_order(form)
    sandwiches = API.get_sandwiches()
    return flask.render_template("sandwiches.html.jinja2", products=sandwiches)


@app.route("/boissons", methods=['GET', "POST"])
def boissons():
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_product_to_order(form)
    drinks = API.get_drinks()
    return flask.render_template("boissons.html.jinja2", products=drinks)


@app.route("/menus", methods=['GET', "POST"])
def menus():
    menu_prices_list, sandwich_dict = API.get_menu_prices()
    drinks = API.get_drinks()
    des = API.get_desserts()
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_menu_to_order(form)
    return flask.render_template("menus.html.jinja2", menus_list=menu_prices_list, sandwich_dict=sandwich_dict,
                                 drinks=drinks, des=des)


@app.route("/desserts", methods=['GET', "POST"])
def desserts():
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_product_to_order(form)
    des = API.get_desserts()
    return flask.render_template("desserts.html.jinja2", products=des)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
