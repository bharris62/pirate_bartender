import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def preferences(questions, ingredients):
    '''determine the drink preference of the pirate'''
    pirate_pref = {}

    for idx,val in questions.items():
        print("yes or no?")
        pref = input(val)

        if pref.lower() == 'yes':
            pirate_pref[idx] = True
        else:
            pirate_pref[idx] = False


    build_drink(pirate_pref, ingredients)

def build_drink(pref, ingredients):
    '''accepts preferences and creates a random drink based on them'''
    drink = []

    for idx,val in pref.items():
        if val == True:
            drink.append(random.choice(ingredients[idx]))

    present_drink(drink)

def present_drink(ingred):
    pass


if __name__ == '__main__':
    preferences(questions, ingredients)