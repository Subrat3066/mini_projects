a=int(input("enter the starting point : "))
b=int(input("Enter the end point : "))
choice=int(input("Enter 1 for vertical and 2 for horizintal : "))
c=int(input("Enter 3 for forward and 4 for reverse updation : "))
e=int(input("Enter the updation : "))
d=0
if(c==3):
    d=e
    for i in range (a,b+1,d):
     if(choice==1):
         print(i)
     elif(choice==2):
         print(i,end=',')
elif(c==4):
    d=-e
    for i in range (a,b-1,d):
     if(choice==1):
         print(i)
     elif(choice==2):
         print(i,end=',')
else:
     print("invalid option".title().center(1000))
if b>a and d==-e :
    print("Starting point shouldn't be smaller than end point in reverse updation".upper().center(1000))
