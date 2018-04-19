class Acco
 @@no=0
 @@name=""
 @@bal=0
 def initialize(name,no,bal)
  @name=name
  @no=no
  @bal=bal
 end
 def deposit
  print("Enter the amount to deposit")
  depo=gets.chomp
  depo=depo.to_f
  @bal+=depo
 end
 def withdraw
  print("Enter the amount to withdraw")
  with=gets.chomp
  with=with.to_f
  @bal-=with
 end
 def checkbal
  puts"#@bal"
 end
 def details
  puts"#@name"
  puts"#@no"
  puts"#@bal"
 end
end


print("enter details")
name=gets.chomp
no=gets.chomp
bal=gets.chomp
bal=bal.to_f
print("1.deposit2.withdraw3.balcheck4.details")
wish='y'
a=Acco.new(name,no,bal)
while wish=='y' or wish =='Y'
  n=gets.chomp
  if n=='1'
   puts"going to deposit"
   a.deposit
  elsif n=='2'
   puts"going to withdraw"
   a.withdraw
  elsif n=='3'
   puts"going to bal"
   a.checkbal
  else
   a.details
   puts"going to disp"
  end
  wish=gets.chomp
end 
