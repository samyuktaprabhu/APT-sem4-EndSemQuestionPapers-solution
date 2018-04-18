n=input("Enter a string")
list1=[]
list1=n.split(" ")
print(list1)
list2=[]

for i in list1:
 if i not in list2:
  list2.append(i)
  print(i)
print(list2)

list2.sort()

print(list2)

lc=0
c=0
dc=0

list5=[]
for i in list2:
 for j in i:
  if j.isdigit():
   dc+=1
  elif j.isalpha():
   lc+=1
   if(j in ('a','e','i','o','u','A','E','I','O','U')):
    list5.append(j)
  else:
   c+=1
   
print(" Digit count : ",dc)

print(" letter count : ",lc)
print(list5)
dictt={'a':0,'e':0,'i':0,'o':0,'u':0}
ac=0
ec=0
ic=0
oc=0
uc=0
for i in list5:
  if(i=='a' or i=='A'):
   ac+=1
  elif(i=='e'or i=='E'):
   ec+=1
  elif(i=='i' or i=='I'):
   ic+=1
  elif(i=='o' or i=='O'):
   oc+=1
  elif(i=='u' or i=='U'):
   uc+=1

print(ac)
print(ec)
print(ic)
print(oc)
print(uc)
dictt['a']=ac
dictt['e']=ec
dictt['i']=ic
dictt['o']=oc
dictt['u']=uc
print(dictt)
