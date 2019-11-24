def pengulangan():
    print('silahkan masukkan 3 bilangan yang anda inginkan')
    a=int(input("bilangan A = "))
    b=int(input("bilangan B = "))
    c=int(input("bilangan C= "))

    if a>b and a>c:
        print (a, 'lebih besar daripada B dan C')
    elif b>a and b>c:
        print (b, 'lebih besar daripada A dan C')
    else:
        print (c, 'lebih besar daripada A dan B')
        
pengulangan()
