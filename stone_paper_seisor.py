def game():
 import random
 elements=["stone","paper","seisor"]
 computer=random.choice(['stone','paper','seisor'])
 #print(computer.upper())
 user=input("""Select your option
               1.Stone
               2.Paper
               3.Seisor
           """.center(10))
 u=(user.lower())
 print("u=",u)
 c=computer
 if u=='stone'or u=='1':
    u='stone'
 elif u=="paper"or u=='2':
    u='paper'
 elif u=='seisor'or u=='3':
    u='seisor'
 print("User = ",u)
 print("Computer =",computer)
 if u==c:
    print('Draw'.upper().center(100))
 elif u=='stone' and c=='paper':
    print("Computer wins".upper().center(100))
 elif u=='paper' and c=='seisor':
    print("Compuer Wins".upper().center(100))
 elif u=='seisor' and c=='stone':
    print("Computer wins".upper().center(100))
 else:
    print("User wins".upper().center(100))
 resume=int(input("Enter 1 to play again and 2 to EXIT : "))
 if resume==1:
    game()
game()
