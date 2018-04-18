n=int(input("Enter the number of rows:P"))
k=2*n-2  
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k=k-2 
    a=1
    for j in range(0, i+1):
        print(a, end=" ")
        a+=1
    print()

   
