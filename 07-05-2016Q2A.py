string=input("Enter sentences separated by a full stop : ")
 #Nested list
print("The nested list is :")
list=[]
list=string.split(".")
print(list)
list2=[]
for i in list:
 word=i.split(" ")
 list2.append(word)
print(list2)

#list palindrome
print("Palindrome check : ")
for i in list2:
   print(i)
   if(i==i[::-1]):
    print("It is Palindrome")
   else:
    print("It is Not a palindrome")

#capitalize each word in nested likst n display
print("Caps each word : ")
list4=[]
for i in list2:
  stri=""
  for j in i:
    stri=stri+j+" "
  stri=stri.title()
  list3=stri.split(" ")
  print(list3)
  list4.append(list3)
print(list4)

#sentences display

for i in list2:
  stri=""
  for j in i:
    stri=stri+j+" "
  print(stri+".")
