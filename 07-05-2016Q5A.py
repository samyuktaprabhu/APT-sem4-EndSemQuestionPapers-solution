def calci(*op,opr,f):
 print(op)
 print(opr)
 print(f)
 res=op[0]
 for i in op[1:]:
   #print(i)
   if(opr=="add" or opr==""):
    res=res+i	
   elif(opr=="sub"):
    res=res-i
   elif(opr=="mul"):
    res=res*i
   elif(opr=="div"):
    if(i!=0):	
     res=res/i
    else:
     return "div by zero error"
   else:
     return "error"
 if(f=="int"):
  return res
 else:
  return float(res)	
  
print(calci(2,3,56,opr="",f="float"))
print(calci(1.6,2.8,3,7,9,opr="mul",f="float"))
 
