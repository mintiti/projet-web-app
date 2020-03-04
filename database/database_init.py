

sandwich_dict = {'Jambon Beurre': {'prix': 2.1,
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
            if ingredient not in ingredientsList :
                ingredients_list.append(ingredient)

# Create the list of ingredients
ingredients_list = []
add_ingredients(sandwich_dict, ingredients_list)
add_ingredients(drink_dict, ingredients_list)
add_ingredients(dessert_dict, ingredients_list)


if __name__ == '__main__':
    print(ingredients_list)
