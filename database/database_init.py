from .database import db, commit
from .models import *

sandwiches_dict = {'Jambon Beurre': {'prix': 2.1,
                                     'stock': 10,
                                     'ingredients': ['Jambon', 'Beurre']
                                     },
                   'Poulet Caesar': {'prix': 2.5,
                                     'stock': 10,
                                     'ingredients': ['Poulet', 'Sauce Caesar']
                                     },
                   'Grec': {'prix': 2.5,
                            'stock': 10,
                            'ingredients': ['Viande Grec', 'Salade', 'Tomate', 'Ognon']
                            },
                   'Double Cheeseburger': {'prix': 2.5,
                                           'stock': 10,
                                           'ingredients': ['Steak Haché XXL', 'Fromage de chèvre', 'Tomate', 'Ketchup',
                                                           'Mayonnaise']
                                           },
                   'IMT Atlantique - Campus Nantes': {'prix': 2.5,
                                                      'stock': 10,
                                                      'ingredients': ['Magret de Canard', 'Foie gras',
                                                                      'Sauce secrète IMTA', "Plein d'amour"]
                                                      },
                   'IMT Atlantique - Campus Brest': {'prix': 0.5,
                                                     'stock': 10,
                                                     'ingredients': ['Ananas', 'Beurre', 'Bruine', 'Nuages Gris Maison']
                                                     }}
drink_dict = {'Coca Cola': {'prix': 0.5,
                            'stock': 10,
                            'ingredients': ['Sucre']
                            },
              'Orangina': {'prix': 0.5,
                           'stock': 10,
                           'ingredients': ['Sucre']
                           },
              'Pepsi': {'prix': 0.5,
                        'stock': 10,
                        'ingredients': ['Sucre']
                        },
              'Pepsi Max': {'prix': 0.5,
                            'stock': 10,
                            'ingredients': []
                            },
              'Coca Cola Zero': {'prix': 0.5,
                                 'stock': 10,
                                 'ingredients': []
                                 },
              'Tropico': {'prix': 0.5,
                          'stock': 10,
                          'ingredients': []
                          }}
dessert_dict = {'Pain au chocolat': {'prix': 1.23,
                                     'stock': 10,
                                     'ingredients': []
                                     },
                'Croissant': {'prix': 1.1986,
                              'stock': 10,
                              'ingredients': ['Beurre']
                              },
                'Cookie au chocolat noir': {'prix': 1.25,
                                            'stock': 10,
                                            'ingredients': []
                                            },
                'Pain au chocolat noisette': {'prix': 1.35,
                                              'stock': 10,
                                              'ingredients': []
                                              }}


def add_ingredients(product_dict, ingredientsList):
    for product in product_dict:
        for ingredient in product_dict[product]['ingredients']:
            if ingredient not in ingredientsList:
                ingredients_list.append(ingredient)


# Create the list of ingredients
ingredients_list = []
add_ingredients(sandwiches_dict, ingredients_list)
add_ingredients(drink_dict, ingredients_list)
add_ingredients(dessert_dict, ingredients_list)

ingredient_name_to_instance_dict = {}  # Maps ingredient names to the object instances created


# Initialization of the database functions
def initialize_ingredients():
    for ing in ingredients_list:
        obj = Ingredients(name=ing)
        ingredient_name_to_instance_dict[ing] = obj


@commit(db)
def initialize_sandwiches():
    print(sandwiches_dict)
    for sand in sandwiches_dict:
        sandwich = sandwiches_dict[sand]
        ingredients_in_sandwich = [ingredient_name_to_instance_dict[ing] for ing in sandwich['ingredients']]
        sandwich_instance = Products(name=sand, food_type=SANDWICH, price=sandwich['prix'], stock=sandwich['stock'],
                                     ingredients=ingredients_in_sandwich)
        db.session.add(sandwich_instance)
        print(f"instanciated sandwich {sand}")


@commit(db)
def initialize_drinks():
    for drink in drink_dict:
        dri = drink_dict[drink]
        ingredients_in_drink = [ingredient_name_to_instance_dict[ing] for ing in dri['ingredients']]
        drink_instance = Products(name=drink, food_type=DRINK, price=dri['prix'], stock=dri['stock'],
                                  ingredients=ingredients_in_drink)
        db.session.add(drink_instance)


@commit(db)
def initialize_users():
    user0 = Users(name="Dolly Prane")
    db.session.add(user0)


@commit(db)
def initialize_menu_prices():
    # menu a 5eu si sandwich <= 2.1, 7eu sinon
    sand_list = Products.query.filter(Products.food_type == SANDWICH).all()
    for s in sand_list:
        if s.price <= 2.1:
            menu_sandwich = PrixMenu(sandwich_principal=s.id, prix=5)
        else:
            menu_sandwich = PrixMenu(sandwich_principal=s.id, prix=7)
        db.session.add(menu_sandwich)


@commit(db)
def initialize_desserts():
    for dessert in dessert_dict:
        des = dessert_dict[dessert]
        ingr_in_dessert = [ingredient_name_to_instance_dict[ing] for ing in des['ingredients']]
        des_instance = Products(name=dessert, food_type=DESSERT, price=des['prix'], stock=des['stock'],
                                ingredients=ingr_in_dessert)
        db.session.add(des_instance)
