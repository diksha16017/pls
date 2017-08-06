list1 = [["dia", 12], ["sia", 15], ["ria", 31], ["jia", 10]]
total = 0
hold = []

for item in list1:
    if total + item[1] > 28 :
        break
    else :
        total += item[1]
        hold.append(item[0])

print(hold)
print(total)