from .models import *
from .database import *


@commit(db)
def add_products(list_products):
    """
    takes in a list of products to add, and adds them to the database
    :param list_products: a list of new products to add to the database
    :return: None
    """
    for product in list_products:
        db.session.add(product)
        db.session.commit()
        if product.food_type == SANDWICH:
            new_menu_price_entry(product)


@commit(db)
def new_menu_price_entry(sandwich):
    price = 5 if sandwich.price <= 2.1 else 7
    db.session.add(PrixMenu(sandwich_principal=sandwich.id, prix=price))


# TODO : add order id tracking
@commit(db)
def add_product_to_order(form):
    orderitem = OrderItem(order_id=1, item=form['product_id'], quantity=form['quantity'])
    db.session.add(orderitem)


# TODO : add order id tracking
@commit(db)
def add_menu_to_order(form):
    for item in form:
        o_item = OrderItem(order_id=1, item=form[item], quantity=1)
        db.session.add(o_item)


# Database accessors
def check_stock(func):
    """Function wrapper, returns a product list with only products not out of stock"""

    def f(*args, **kwargs):
        ret = func(*args, **kwargs)
        for product in ret:
            if product.stock == 0:
                ret.remove(product)
        return ret

    return f


def get_product_by_ID(product_id):
    product = Products.query.filter(Products.id == product_id).all()[0]
    return product


def get_menu_prices():
    menu_prices_list = PrixMenu.query.all()
    sandwich_data = [get_product_by_ID(menu.sandwich_principal) for menu in menu_prices_list]
    sandwich_dict = {}
    for sand in sandwich_data:
        sandwich_dict[sand.id] = sand.name
    return menu_prices_list, sandwich_dict


def get_product_img_url(product_id):
    return 'https://via.placeholder.com/800'


def get_cart_data(order_id):
    order_item_list = OrderItem.query.filter(OrderItem.order_id == order_id).all()
    order_item_data = {}
    img_list = {}
    for order_item in order_item_list:
        product = get_product_by_ID(order_item.item)
        product_dict = {'name': product.name,
                        'price': product.price}
        order_item_data[order_item.item] = product_dict
        img_list[order_item.item] = get_product_img_url(order_item.item)
    return order_item_list, order_item_data, img_list


@check_stock
def get_drinks():
    return Products.query.filter(Products.food_type == DRINK).all()


@check_stock
def get_sandwiches():
    return Products.query.filter(Products.food_type == SANDWICH).all()


@check_stock
def get_desserts():
    return Products.query.filter(Products.food_type == DESSERT).all()
