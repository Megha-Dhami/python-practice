num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
sum=num1+num2
sub=num1-num2
mul=num1*num2

print("addition: ",sum)
print("subtraction: ",sub)
print("multiplication: ",mul)

if num2==0:
    print("Division: cannot divide by zero")
else:
    div=num1/num2
    print("division: ",div)