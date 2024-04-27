import random
def roll_again():
    b=random.randint(1,6)
    print("the number on dice is :",b)
    again=int(input("Enter 1 to roll again and 2 for EXIT : "))
    if again==1:
      roll_again() 
user=int(input("Enter 1 to Roll the dice : "))
a=random.randint(1,6)
if user==1:
    print("the number on dice is :",a)
again=int(input("Enter 1 to roll again"))
if again==1:
    roll_again()
