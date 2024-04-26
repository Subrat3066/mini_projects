age=int(input("Enter Your Age : "))
if age>=18:
    print("You Are Eligible For Voting".upper())
    print()
    print("Select Your Leader's Group")
    print("1.BJP , 2.Congress , 3.AAP , 4.RJD , 5.CPI , 6.BSP , 7.JDU")
    choice=int(input("Enter the number corresponding to your political party : "))
    if choice==1:
        print("You Have Voted BJP")
        print("Thanks For Your Vote")
    if choice==2:
        print("You Have Voted Congress")
        print("Thanks For Your Vote")
    if choice==3:
        print("You Have Voted AAP")
        print("Thanks For Your Vote")
    if choice==4:
        print("You Have Voted RJD")
        print("Thanks For Your Vote")
    if choice==5:
        print("You Have Voted CPI")
        print("Thanks For Your Vote")
    if choice==6:
        print("You Have Voted BSP")
        print("Thanks For Your Vote")
    if choice==7:
        print("You Have Voted JDU")
        print("Thanks For Your Vote")
    else:
     ("INVALED OPTION")
else :
    b=" year"
    a=str(18-age)+b
    print("You are not Eligible To Vote Right Now")
    print("Please Come After",a)
    