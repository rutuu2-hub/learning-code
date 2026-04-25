import random

level = input("level songoh 'easy''medium''hard'")

if level == "easy":
   max_num = 10
elif level == "medium":
     max_num = 50
else :
     max_num = 100

secret = random.randint(1,max_num)

a_count = 0

while True:
    try:
        userinput = int(input(f"1-{max_num} hoorond too taana uu: "))
        
        if userinput < 1 or max_num < userinput:
            print(f"1-{max_num} hoorond too oruulna uu")
            continue

        a_count += 1

        if userinput == secret:
            print("ta hojloo")
            break
        elif userinput > secret:
            print("arai ih baina")
        else :
            print("arai baga bn")

        if a_count == 7:
            print("ta hojigdloo")
            break
    except:
        print("zuvhun too ooruulna uu")

print("niit orldlogo", a_count)