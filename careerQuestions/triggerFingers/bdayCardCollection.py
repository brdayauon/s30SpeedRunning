def birthdayCardCollection(leanne, D):
    seen= set(leanne)
    total = 0
    money = D
    for i in range(1, D+1):
        if i > money:
            break
        if i in seen:
            continue
        else:
            total += 1
            money -= i
    return total
leanne = [1,2,4,5]
D = 20

print(birthdayCardCollection(leanne, D))