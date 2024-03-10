coins = float(input()) * 100
counter = 0

while coins != 0:
    coins = int(coins)
    if coins >= 200:  # --------------- от 2 до 5 лева --------------
        counter += 1
        coins -= 200

    elif coins >= 100:  # -------------- от 1 до 2 лева ---------------
        counter += 1
        coins -= 100

    elif coins >= 50:  # ------------- от 50 ст до 1лев --------------
        counter += 1
        coins -= 50

    elif coins >= 20:  # ------------- от 20ст до 50ст ---------------
        counter += 1
        coins -= 20

    elif coins >= 10:  # ------------ от 10 до 20ст ------------------
        counter += 1
        coins -= 10

    elif coins >= 5:  # -------------- от 5 до 10ст ----------------
        counter += 1
        coins -= 5

    elif coins >= 2:  # --------------- от 2 до 5ст ----------------
        counter += 1
        coins -= 2

    elif coins > 0:  # --------------- от 1 до 2ст ----------------
        counter += 1
        coins -= coins

print(counter)
