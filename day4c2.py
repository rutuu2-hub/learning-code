import random

secret = random.randint(1,10)

a_count = 0
while True:
    try:
        user_input = int(input("too g taana uu tand orldoh 3n bolomj baina"))
        a_count +=1

        if user_input == secret:
            print("taa taaj chadlaa")
            break
        elif user_input > secret:
            print("ih baina")
        else:
            print("baga baina")

        if a_count == 3:
            print("ta hojigdlo")
            break
    except:
        print("zuvhun too oruulna uu")

print("niit orldlog",a_count)