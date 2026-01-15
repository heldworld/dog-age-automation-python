while True:
    try:
        dogAge = float(input("Enter dog age (0–15): "))
#equivalent human Age
        if 0 < dogAge <= 1:
            humanAge = dogAge * 15
        elif 1 < dogAge <= 5:
            humanAge = dogAge * 11 + 2
        elif 5 < dogAge <= 15:
            humanAge = dogAge * 8 - 3
        else:
            print("The calculator only supports ages 0–15.")
            continue

        # Classification
        if humanAge < 20:
            ageGP = "Young"
        elif 20 <= humanAge <= 39:
            ageGP = "Adult"
        else:
            ageGP = "Senior"

        print(f"Your Dog equivalent Human Age is {humanAge:.1f} and classified as {ageGP}")
        break

    except ValueError:
        print("Input a valid number.")