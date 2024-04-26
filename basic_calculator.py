no1=int(input("Enter 1st number : "))
no2=int(input("Enter 2nd number : "))
opt=int(input("select operation (1.addition,2.Subtraction,3.Multiplication,4.Division): "))
if opt==1:
 addition=no1+no2
 print("Addition : ",addition)
elif opt==2:
    subtraction=no1-no2
    print("Subtraction = ",subtraction)
elif opt==3:
    multiplication=no1*no2
    print("Multiplication is : ",multiplication)
elif opt==4:
    division=no1/no2
    print("Division is : ",division)
else :
    print("Invalid ooerator")
