num1=int(input("Enter frist number : "))
num2=int(input("Enter second number : "))
print("The number you have entered are :",num1,"And",num2,"Respectively")
operator=input("Enter + for addition,- for subtraction,* for multiplication,/ for division ENTER YOUR CHOICE :")
print("your want to do:",operator)
if operator=="+":
    a=num1+num2
    print("Result is",a)
elif operator=="-":
    b=num1-num2
    print("Result is",b)
elif operator=="*":
    c=num1*num2
    print("Result is",c)
elif operator=="/":
    d=num1/num2
    print("Result is",d)
else:
    print("You have entered an INVALID operator PLEASE TRY AGAIN!") 