import random
a=random.randint(1,100)
choose=int(input("Gess no of your choice between 1 to 100 : "))
print("your number",choose)
print("My number",a)
if choose== a :
    print("Your Number Mathched With My Number ")
else :
    print("Your Number Not Matched With Mine")
    print('Better luck next time ')