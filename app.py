import flask
from flask import flash, request, redirect, url_for, render_template
from database.models import *
from database import API
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
    initialize_order_db()
    initialize_order_item()
    initialize_menu_prices()

    return "Cleaned!"


db.init_app(app)

with app.test_request_context():
    clean()


@app.route("/")
def home():
    cart = API.get_cart_data(1)
    return flask.render_template("base.html.jinja2", cart = cart)


@app.route("/sandwichs", methods=['GET', "POST"])
def sandwichs():
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_product_to_order(form)
        return flask.redirect(flask.url_for('sandwichs'))
    cart = API.get_cart_data(1)
    sandwiches = API.get_sandwiches()
    return flask.render_template("sandwiches.html.jinja2", products=sandwiches, cart = cart)


@app.route("/boissons", methods=['GET', "POST"])
def boissons():
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_product_to_order(form)
        return flask.redirect(flask.url_for('boissons'))
    cart = API.get_cart_data(1)
    drinks = API.get_drinks()
    return flask.render_template("boissons.html.jinja2", products=drinks, cart = cart)


@app.route("/menus", methods=['GET', "POST"])
def menus():
    menu_prices_list, sandwich_dict = API.get_menu_prices()
    drinks = API.get_drinks()
    des = API.get_desserts()
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_menu_to_order(form)
        return flask.redirect(flask.url_for('menus'))
    cart = API.get_cart_data(1)
    return flask.render_template("menus.html.jinja2", menus_list=menu_prices_list, sandwich_dict=sandwich_dict,
                                 drinks=drinks, des=des, cart= cart)


@app.route("/desserts", methods=['GET', "POST"])
def desserts():
    if flask.request.method == 'POST':
        form = flask.request.form
        API.add_product_to_order(form)
        return flask.redirect(flask.url_for('desserts'))
    cart = API.get_cart_data(1)
    des = API.get_desserts()
    return flask.render_template("desserts.html.jinja2", products=des, cart = cart)

@app.route("/validate/<int:order_id>")
def validate(order_id):
    API.validate_order(order_id)
    return flask.redirect(flask.url_for("home"))

@app.route("/backend", methods=['GET', "POST"])
def backend():
    if request.method == 'POST':
        title = request.form.get('title')
        food_type = request.form.get('food_type')
        price = request.form.get('price')
        stock = request.form.get('stock')
        products0 = Products(name=title, food_type=food_type, price=price, stock=stock)
        API.add_products([products0])
        flash('Item created')
        return redirect(url_for("backend"))

    products = Products.query.all()
    return flask.render_template("bacckend.html", products=products)


@app.route('/edit_products/<products_id>', methods=['GET', 'POST'])
def edit(products_id):
    products = Products.query.get(products_id)

    if request.method == 'POST':  # 处理编辑表单的提交请求
        title = request.form.get('title')
        food_type = request.form.get('food_type')
        price = request.form.get('price')
        stock = request.form.get('stock')
        if not title or not food_type or not price or not stock or len(title) > 60 or len(food_type) > 1:
            flash('Invalid input.')
            return redirect(url_for('edit', products_id=products_id))  # 重定向回对应的编辑页面

        products.name = title  # 更新
        products.food_type = food_type
        products.price = price
        products.stock = stock
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('backend'))  # 重定向回主页

    return render_template('edit.html', products=products)  # 传入被编辑的电影记录


@app.route('/delete_products/<product_id>')
def delete_product(product_id):
    product = API.get_product_by_ID(product_id)
    if product != None :
        try:
            db.session.delete(product)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('err delete')
    else:
        flash('not found')
    return redirect(url_for('backend'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
