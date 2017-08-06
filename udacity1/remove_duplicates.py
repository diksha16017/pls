list1 = ["sia","pia","sia","sia","dia","ria","dia"]
print(len(list1))
dup = []
for item in list1:
    if item not in dup :
        dup.append(item)
print(len(dup))
print(dup)

set1 = set(list1)
print (len(set1))
print(set1)

print ("ria" in set1)
print ("jia" not in set1)
print ("jia" in set1)