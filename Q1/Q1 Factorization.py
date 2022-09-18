#We need to define variables then using for loop for factorization
fact =1 
var=  100
for i in range(1,var):
  fact = fact*1 
  # now we found factorization we need to sum  
  sum = 0
  temp =fact
  while(temp) :
    sum =sum+ (temp%10)
    temp=int(temp/10)
    #This is our final result
    
  
