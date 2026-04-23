def check_number(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
numbers = [1,2,3,4,5,6]

for n in numbers:
    result = check_number(n)
    print(n,"->",result)