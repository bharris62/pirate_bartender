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


def yes_or_no(resp):
        '''Error checking function, for yes or no questions.'''
        try:
            if resp.lower() == 'y' or resp == 'yes':
                return 'yes'
            elif resp.lower() == 'n' or resp == 'no':
                return 'no'
            else:
                print("Remember, yes or no.")

        except ValueError:
            print("Must be answered in yes or no.")


def preferences(questions, ingredients):
    '''determine the drink preference of the pirate'''
    pirate_pref = {}
    print("answer yes or no")
    for idx, val in questions.items():
        while True:
            pref = input("{} ".format(val))
            check_response = yes_or_no(pref)
            if check_response == 'yes' or check_response == 'no':
                break

        if pref.lower() == 'yes':
            pirate_pref[idx] = True
        else:
            pirate_pref[idx] = False

    build_drink(pirate_pref, ingredients)


def build_drink(pref, mix):
    '''accepts preferences and creates a random drink based on them'''
    drink = []

    for idx, val in pref.items():
        if val == True:
            drink.append(random.choice(mix[idx]))

    present_drink(drink)


def name_drink(name_length):
    words = ['Ahoy', 'Aye', 'Booty', 'Blimey', 'Coffer', 'Hearties', 'Mutiny', 'Salty', 'Squiffy', 'Yo Ho Ho', 'Ye']

    drink_name = []
    iteration = 0
    while iteration < name_length:
        drink_name.append(random.choice(words))
        iteration += 1

    drink_name = ' '.join(drink_name)
    return drink_name


def present_drink(ingred):
    '''Presents the drink to customer'''
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

    print("And We will call it '{}'".format(name_drink(len(ingred))))


if __name__ == '__main__':
    drink_number = 0
    while True:
        if drink_number == 0:
            preferences(questions, ingredients)
        drink_number += 1
        if drink_number == 5:
            print('Ahoy, We are responsible pirates, gotta cut you off! ')
            break

        while True:
            ans = input("Like another? had {} drink(s) ".format(drink_number))
            temp_ans = yes_or_no(ans)

            if temp_ans == 'no':
                break
            else:
                preferences(questions, ingredients)
        break