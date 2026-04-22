while True:
    user = input("nasaa bich esvel garah bol q")
    
    if user == "q":
        break
    
    try:
        age = int(user)

        if age <= 13:
            print("huuhed")
        elif 13<= age <=17:
            print("teen")
        elif 18<= age <=59:
            print("adult")
        else:
            print("ahmad")
    except ValueError:
        print("too bich")     


