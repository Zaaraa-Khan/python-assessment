a=int(input("Enter a number="))
b=int(input("Enter a second number="))
c=int(input("Enter a third number="))
if a>=b and a>=c:
    print("The Largest number is =",a)
elif b>=a and b>=c:
    print("The Largest number is =",b)
else:
    print("The Largest number is =",c)
