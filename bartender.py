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


def yes_or_no(question):
        """Error checking function, for yes or no questions."""

        while True:
            resp = input("{} ".format(question)).lower()
            if resp == 'y' or resp == 'yes':
                return 'yes'
            elif resp == 'n' or resp == 'no':
                return 'no'
            else:
                print("Remember, yes or no.")


def preferences(questions, ingredients):
    """determine the drink preference of the pirate"""
    pirate_pref = {}
    print("answer yes or no")
    for idx, val in questions.items():
        pref = yes_or_no(val)
        if pref.lower() == 'yes':
            pirate_pref[idx] = True
        else:
            pirate_pref[idx] = False

    build_drink(pirate_pref, ingredients)


def build_drink(pref, mix):
    """accepts preferences and creates a random drink based on them"""
    drink = []

    for idx, val in pref.items():
        if val:
            drink.append(random.choice(mix[idx]))

    present_drink(drink)


def name_drink():
    """Creating a random drink name based on a adjective and a noun"""
    adjectives = ['Feared', 'Evil', 'Dusty', 'Salty', 'Colossal', 'Cuddly']
    nouns = ['Cannon', 'Flag', 'Ship', 'Hook', 'Hurricane', 'Marauder', 'Pistol', 'Dog']

    drink_name = [random.choice(adjectives), random.choice(nouns)]
    drink_name = ' '.join(drink_name)

    return drink_name


def present_drink(ingred):
    """Presents the drink to customer"""
    if len(ingred) == 5:
        print(
        "Let's take a {}, {}, {}, {}, and finally {}!".format(ingred[0], ingred[1], ingred[2], ingred[3], ingred[4]))
    elif len(ingred) == 4:
        print("In that case a {}, {}, {}, and finally {}.".format(ingred[0], ingred[1], ingred[2], ingred[3]))
    elif len(ingred) == 3:
        print("let me see, {}, {}, and {} should do.".format(ingred[0], ingred[1], ingred[2]))
    elif len(ingred) == 2:
        print("Easy enough, {} and {}.".format(ingred[0], ingred[1]))
    elif len(ingred) == 1:
        print("WOW only a {}".format(ingred[0]))
    else:
        print("You are at the wrong place!")

    print("And We will call it 'The {}'".format(name_drink()))


if __name__ == '__main__':
    drink_number = 0
    if drink_number == 0:
        preferences(questions, ingredients)
        drink_number += 1

    while True:
        temp_ans = yes_or_no("Like another? had {} drink(s) ".format(drink_number))

        if temp_ans == 'no':
            break
        else:
            preferences(questions, ingredients)
            drink_number += 1
            if drink_number == 5:
                print('Ahoy, We are responsible pirates, gotta cut you off! ')
                break
