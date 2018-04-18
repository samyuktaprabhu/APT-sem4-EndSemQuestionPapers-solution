import copy
#n=int(input("Enter the number of element"))
list1=[1,2,"str",4.6,True,None,5,5,4.6,7,9,8,7,"str"]

#for i in range(0,n):
# list1.append(input("Enter element"))
#print(list1)
sum=0
numerical=[]
for i in list1:
 if isinstance(i,str):
  print(i," is a string")
 elif isinstance(i,bool):
  print(i," is a boolean")
 elif isinstance(i,int):
  print(i," is an int")
  sum+=i
  numerical.append(i)
 elif isinstance(i,complex):
  print(i," is a complex")
 elif isinstance(i,float):
  print(i," is a float")
 elif isinstance(i,list):
  print(i," is a list")
 elif isinstance(i,dict):
  print(i," is an dict")
 elif isinstance(i,tuple):
  print(i," is a tuple")
 elif isinstance(i,set):
  print(i," is a set")

print(numerical)
print(sum)
list3=[]
list3=copy.deepcopy(list1)
print(list3)



#remove duplicates
list4=[]
for i in list3:
 if i not in list4:
  list4.append(i)
list3=list4
print(list3)
