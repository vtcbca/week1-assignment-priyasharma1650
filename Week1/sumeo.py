num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
s=num1+num2
print("The sum of two numbers:{} and {} is {} ".format(num1,num2,s))
if(s%2==0):
    print("The number is even")
else:
    print("The number is odd")
