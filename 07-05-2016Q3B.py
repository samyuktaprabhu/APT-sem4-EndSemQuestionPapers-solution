n=input("")
list1=n.split(",")
list2=[]
list3=[]
list4=[]
k=0
kk=0
print(list1)
for i in list1:
  j=i[::-1]
  k=int(j[0])*1+int(j[1])*2+int(j[2])*4+int(j[3])*8
  print(k)
  if(k%5==0):
    list3.append(k)
  else:
    list4.append(k)

print(list3)
print(list4)
