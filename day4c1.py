import random

secret = random.randint(1, 10)

a_count = 0

while True:
    try:
        user_input = int(input("1-10 hoorond too g taagarai: "))
        a_count += 1

        if user_input == secret:
            print("zuv baina!")
            break

        elif user_input > secret:
            print("heterhii ih")

        else:
            print("heterhii baga")

    except:
        print("zuvhun too oruulna uu")

print("niit oroldlogo:", a_count)