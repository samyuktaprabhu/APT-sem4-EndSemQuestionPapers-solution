def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

def dectohex(num):
   if num>1:
       dectohex(num//16)
   rem=num%16

   if(rem<9):
       print(rem, end='')
   else:
     if(rem==10):
       print('A', end='')
     elif(rem==11):
       print('B', end='')
     elif(rem==12):
       print('C', end='')
     elif(rem==13):
       print('D', end='')
     elif(rem==14):
       print('E', end='')
     elif(rem==15):
       print('F', end='')
	
def dectooct(num):
   if num>1:
       dectooct(num//8)
   print(num%8,end='')


# decimal number
number = int(input("Enter any decimal number: "))

decimalToBinary(number)
print("")
dectohex(number)
print("")
dectooct(number)
