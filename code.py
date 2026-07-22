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
    color_coefficient = {
        "black": 250,
        "brown": 100,
        "red": 50,
        "orange": 15,
        "yellow": 25,
        "green": 20,
        "blue": 10,
        "violet": 5,
        "purple": 5,
        "grey": 1,
    }
    print("Welcome to the resistor calculator!")
    slct = int(input("How many stripes does your resistor have?: "))
    if slct == 3:
        first_st = color_digits.get(input("What is the color of the first stripe?: "))
        while first_st not in color_digits:
            print("ERROR: No color found")
            first_st = color_digits.get(
                input("What is the color of the first stripe?: ")
            )
        if first_st in color_digits:
            continue
        secon_st = color_digits.get(input("What is the color of the second stripe?: "))
        if secon_st not in color_digits:
            print("ERROR: No color found")
            secon_st = color_digits.get(
                input("What is the color of the second stripe?: ")
            )
        if secon_st in color_digits:
            continue
        res_first = float(first_st + secon_st)
        third_st = color_multipliers.get(
            input("What is the color of the third stripe?: ")
        )
        if third_st not in color_multipliers:
            print("ERROR: No color found")
            third_st = color_multipliers.get(
                input("What is the color of the third stripe?: ")
            )
        if third_st in color_multipliers:
            continue
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
        res_third_plus = res_secon + res_calculated_percent
        res_third_minus = res_secon - res_calculated_percent
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
        res_third_plus = res_secon + res_calculated_percent
        res_third_minus = res_secon - res_calculated_percent
        print(
            f"The resistor has {res_secon} ohms, it can vary to ±{res_calculated_percent} resulting in +{res_third_plus} and -{res_third_minus}"
        )
    if slct == 6:
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
        sixth_st = color_coefficient.get(
            input("What is the color of the sixth stripe?")
        )
        temp_init = float(input("What is the temperature?: "))
        temp_coef = temp_init - 25
        res_fort = res_secon * sixth_st * temp_coef * 10**-6
        res_fift_minus = res_secon + res_fort - res_calculated_percent
        res_fift_plus = res_secon + res_fort - res_calculated_percent
        print(
            f"The resistor has {res_secon} ohms, it can vary to ±{res_calculated_percent} ohms resulting in +{res_third_plus}ohms and -{res_third_minus} ohms, and it can vary {res_fort} ohms with the temperature coefficient and it can get to (with tolerance +) {res_fift_minus} ohms and (with tolerance -) {res_fift_plus}"
        )
    else:
        print("ERROR: No Resistor stripes amount found")
        continue
