import sys


def find_key(d, t_value):
    for key, value in d.items():
        if value == t_value:
            return key
    return ("Unknown capital")


def state(argv):

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    print(find_key(states, find_key(capital_cities, argv)))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        state(sys.argv[1])