num = int(input())  
  
#calculating the number of digits  
num_of_digits = len(str(num))  
  
#computing the square of a number  
square = num**2  
  
#obtaining the last digits   
last_digits = square%pow(10,num_of_digits)  
  
#comparing the digits of number with input  
if last_digits == num:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number")  