while True:
    balance=int(input('enter your balance:'))
    print(f'''
          1.Soap:-Rs.100
          2.Detergent:-Rs.150
          3.face wash:-Rs.100
          4.Biscuit/other:-Rs.50
          5.Medicine:-Rs.200
          6.end''')
    
    item=list(map(int,input('Choose: the option(1/2/3/4/5) separated with space :').split()))
    
    x=0
    print('your items are:')
    for i in item:
        
        if i==1:
          x+=100
          print('Soap')
        elif i==2:
            x+=150
            print('Detergent')
        elif i==3:
            x+=100
            print('face Wash')
        elif i==4:
            x+=50
            print('Biscuit')
        elif i==5:
            x+=200
            print('Medicine')
        else:
            print('thank you')
    if balance<x:
        print('Insufficient Balance')
    
    else:
        balance-=x
        print('Grand Total for all your products are:',x)
        print('your remaining amount:',balance)
        print('Thank you')
        break    