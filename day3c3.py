def check_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

a_count = 0
f_count = 0

while True:
    user_input = input("onoogoo oruul (stop gej bichvel zogsono): ")

    if user_input == "stop":
        print("programm duuslaa")
        break

    try:
        score = int(user_input)

        if score < 0 or score > 100:
            print("dungee shalgaad ahiad oruuna uu")
            continue

        result = check_score(score)
        print("Dun:", result)

        if result == "A":
            a_count += 1
        elif result == "F":
            f_count += 1

    except:
        print("zuvhun dungee oruulna uu")

print("A avsan:", a_count)
print("F avsan:", f_count)