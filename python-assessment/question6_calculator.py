def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

num1=float(input("Enter first number="))
num2=float(input("Enter second number="))

print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter you choice(1-4)="))

if choice==1:
    print("Result=",add(num1,num2))
elif choice==2:
    print("Result=",sub(num1,num2))
elif choice==3:
    print("Result=",mult(num1,num2))
elif choice==4:
    if num2!=0:
        print("Result=",div(num1,num2))
    else:
        print("Division by zero is not possible")
else:
    print("Invalid Choice")
    
