list1 = ["sia","pia","sia","sia","dia","ria","dia"]
print(len(list1))
dup = []
for item in list1:
    if item not in dup :
        dup.append(item)
print(len(dup))
print(dup)