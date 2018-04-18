print("Enter a string")
str=gets().chomp()
print("The string is #{str} \n")

#printing alternate words
arr=str.split
len=arr.length
puts len
print("\n The words alternatively present are : \n")
alt=""
for i in 0..len-1
 if ((i%2)==0)
   print("")
 else
   #print(arr[i]+" ")
   alt=alt+arr[i]+" "
 end
end
puts alt
#reverse a string

print("\n The string in reverse : \n")
for i in arr
 print(i.reverse()+" ")
end
print("\n")

#palindrome
print("\n Palindrome check : \n")
if str==str.reverse()
 print ("\nit is a palindrome...")
else
 print ("\nIt is not a palindrome...")
end

#vowel
vowel=""
print("\n The words starting with vowels are : \n")
for i in arr
 if (i.start_with?('a')||i.start_with?('e')||i.start_with?('i')||i.start_with?('o')||i.start_with?('u'))
   vowel=vowel+i+" "
 else
   print("")
 end
end
puts vowel

#multiply the words
#use collect function
print("\n The words with repetetions are : \n")
repeat=""
repeat=arr.collect{|i| i*2}
puts repeat
