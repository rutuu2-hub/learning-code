def check_score(score):
    if score >= 90:
        return "a"
    elif score >= 80:
        return "b"
    elif score >= 70:
        return "c"
    else:
        return "f"
    
scores = [95,85,75,65,34,22,100]

for score in scores:
    result = check_score(score)
    print(score,"tanii dun",result)