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
    print("Welcome to the resistor calculator!")
    slct = int(input("How many stripes does your resistor have?: "))
    if slct == 3:
        first_st = color_digits.get(input("What is the color of the first stripe?: "))
        secon_st = color_digits.get(input("What is the color of the second stripe?: "))
        res_first = float(first_st + secon_st)
        third_st = color_multipliers.get(
            input("What is the color of the third stripe?: ")
        )
        res_secon = res_first * third_st
        print(f"The resistor has {res_secon} ohms")
    if slct == 4:
        first_st = color_digits.get(input("What is the color of the first stripe?: "))
        secon_st = color_digits.get(input("What is the color of the second stripe?: "))
        res_first = float(first_st + secon_st)
        third_st = color_multipliers.get(
            input("What is the color of the third stripe?: ")
        )
        res_secon = res_first * third_st
        fourt_st = color_tolerance.get(
            input("What is the color of the fourth stripe?: ")
        )
        res_percent = res_secon / 100
        res_calculated_percent = res_percent * fourt_st
        res_third_plus = res_secon - res_calculated_percent
        res_third_minus = res_secon + res_calculated_percent
        print(
            f"The resistor has {res_secon} ohms, it can vary to ±{res_calculated_percent} resulting in +{res_third_plus} and -{res_third_minus}"
        )
    if slct == 5:
        first_st = color_digits.get(input("What is the color of the first stripe?: "))
        secon_st = color_digits.get(input("What is the color of the second stripe?: "))
        third_st = color_digits.get(input("What is the color of the third stripe?: "))
        res_first = float(first_st + secon_st + third_st)
        fourt_st = color_multipliers.get(
            input("What is the color of the fourth stripe?: ")
        )
        res_secon = res_first * fourt_st
        fifth_st = color_tolerance.get(
            input("What is the color of the fifth stripe?: ")
        )
        res_percent = res_secon / 100
        res_calculated_percent = res_percent * fifth_st
        res_third_plus = res_secon - res_calculated_percent
        res_third_minus = res_secon + res_calculated_percent
        print(
            f"The resistor has {res_secon} ohms, it can vary to ±{res_calculated_percent} resulting in +{res_third_plus} and -{res_third_minus}"
        )
