str1=input("Enter elements of first set")
set1=set(str1.split(" "))
str2=input("Enter elements of second set")
set2=set(str2.split(" "))

print(set1)
print(set2)

print(" Union of set ")
print(set1|set2)

print(" intersection of set ")
print(set1&set2)

print(" difference of set ")
print(set1^set2)
