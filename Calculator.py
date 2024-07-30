# Codsoft
#This is my internship project with Codsoft
num1=int(input("Enter first number here:"))
num2=int(input("Enter second number here:"))

print("Press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")

choice=int(input("Enter your choice from 1-4:"))

if choice==1:
    print("The sum of given number is:",num1+num2)
elif choice==2:
    print("The difference between two number is:",num1-num2)
elif choice==3:
    print("The product of two numbers is:",num1*num2)
elif choice==4:
    print("The quotient of the given number is:",num1/num2)
else:
    print("Invalid choice!!")
