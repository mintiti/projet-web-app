from .models import *
from .database import *
@commit(db)
def add_products(list_products):
    """
    takes in a list of products to add, and adds them to the database
    :param list_products: a list of new products to add to the database
    :return: None
    """
    for product in list_products :
        db.session.add(product)
        db.session.commit()
        if product.food_type == SANDWICH:
            new_menu_price_entry(product)

@commit(db)
def new_menu_price_entry(sandwich):
    price = 5 if sandwich.price <= 2.1 else 7
    db.session.add(PrixMenu(sandwich_principal= sandwich.id, prix= price))


def add_product_to_order():
    pass

#TODO : database accessors for sandwiches, drinks, desserts and menus