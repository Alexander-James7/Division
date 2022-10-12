#Created by: Alexander James with help by Owen Whalley
#Created on: 2022/10/12

# This code asks the user for 2 numbers to subtract, and gives the quotient and remainder
x = int(input("What is your first number: "))
y = int(input("What is your second number: "))

# This counts the number of times the code loops, and assigns that number to the quotient.
count = -1

while x > 0:
  x -= y
  count += 1
  
if x < 0:
  for i in range(1):
    x += y
    break
# We get the remainder by constantly subtracting the second number from the first number until we hit 0.
print("The quotient is "+str(count)+" and the remainder is "+str(x))
  
