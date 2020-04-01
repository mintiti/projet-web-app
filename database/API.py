from .models import *
from .database import *
from .utils import CartItem, Cart, OrderProduct, BackendOrder


# Utility
def check_stock(func):
    """Function wrapper, returns a product list with only products not out of stock"""

    def f(*args, **kwargs):
        ret = func(*args, **kwargs)
        for product in ret:
            if product.stock == 0:
                ret.remove(product)
        return ret

    return f

def check_order_availability(order_id):
    cart = get_cart_data(order_id)
    product_list = [get_product_by_ID(cartitem.id) for cartitem in cart]
    order_ok = True
    for cartitem, prod in zip(cart,product_list):
        order_ok = order_ok & (cartitem.quantity <= prod.stock)


    return order_ok

# Database modifiers


def modify_stock(order_id):
    cart = get_cart_data(order_id)
    product_list = [get_product_by_ID(cartitem.id) for cartitem in cart]
    for cartitem, prod in zip(cart,product_list):
        prod.stock -= cartitem.quantity

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


@commit(db)
def validate_order(id):
    order_available = check_order_availability(id)
    if order_available :
        modify_stock(id)
        order = Order.query.filter(Order.id == id).first()
        order.validated = True
        return order_available
    else :
        return order_available


# Database accessors

def get_order_prod_list(order_list):
    return [get_product_by_ID(order_item.item for order_item in order_list )]

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


def get_cart_data(order_id):
    """Returns a list of CartItem
        :arg order_id: the id of the order
        :return list of CartItem instances"""
    # prendre la liste des objets dans la commande
    order = get_order_by_id(order_id)
    cart = Cart()
    if not order.validated:
        order_item_list = get_order_list(order_id)
        # en chopper la liste de produits correspondante
        for order_item in order_item_list:
            product = Products.query.filter(Products.id == order_item.item).all()[0]
            cart_item = CartItem(product.id, product.name, order_item.quantity, product.price, product.food_type)
            cart.add(cart_item)

    return cart


def get_order_data(order_id):
    order_item_list = get_order_list(order_id)
    ord = BackendOrder()
    for ord_it in order_item_list:
        product = get_product_by_ID(ord_it.item)
        ord_prod = OrderProduct(product.name, ord_it.quantity, product.price, ord_it.id)
        ord.add(ord_prod)
    return ord

def get_order_list(order_id):
    return OrderItem.query.filter(OrderItem.order_id == order_id).all()

def get_order_by_id(order_id):
    return Order.query.filter(Order.id == order_id).first()

def get_all_orders():
    return Order.query.all()

def get_all_validated_orders():
    orders = get_all_orders()
    print(orders)
    for ord in orders:
        if not ord.validated :
            orders.remove(ord)

    return orders


@check_stock
def get_drinks():
    return Products.query.filter(Products.food_type == DRINK).all()


@check_stock
def get_sandwiches():
    return Products.query.filter(Products.food_type == SANDWICH).all()


@check_stock
def get_desserts():
    return Products.query.filter(Products.food_type == DESSERT).all()


# Deletes
@commit(db)
def delete_order_item(order_item_id):
    OrderItem.query.filter(OrderItem.id == order_item_id).delete()

@commit(db)
def delete_order(id):
    OrderItem.query.filter(OrderItem.order_id == id).delete()