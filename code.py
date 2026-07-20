i = True
while i == True:
    color_digits = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "purple": "7",
        "grey": "8",
        "white": "9",
    }
    color_multipliers = {
        "black": 1,
        "brown": 10,
        "red": 100,
        "orange": 1000,
        "yellow": 10000,
        "green": 100000,
        "blue": 1000000,
        "violet": 10000000,
        "purple": 10000000,
        "grey": 100000000,
        "white": 1000000000,
        "gold": 0.1,
        "silver": 0.01,
    }
    color_tolerance = {
        "brown": 1,
        "red": 2,
        "green": 0.5,
        "blue": 0.25,
        "violet": 0.1,
        "purple": 0.1,
        "grey": 0.05,
        "gold": 5,
        "silver": 10,
    }
