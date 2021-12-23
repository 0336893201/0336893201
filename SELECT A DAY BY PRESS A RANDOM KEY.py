
#Select TO know how many days in a month by press random key in keyboard

v=int(input("nhap so bat ky tu 1-12:"))
if v == 1:
    print('thang 1 co 31 ngay')
elif v==3:
    print('thang 3 co 31 ngay')
elif v== 5:
    print('thang 5 co 31 ngay')
elif v==7:
    print('thang 7 co 31 ngay')
elif v==8:
    print('thang 8 co 31 ngay')
elif v==10:
    print('thang 10 co 31 ngay')
elif v==12:
    print('thang 12 co 31 ngay')

if v < 7:
    print('thang 4 co 30 ngay')
elif v <= 7:
    print('thang 6 co 30 ngay')
elif v > 7 :
    print('thang 9 va thang 11 deu co 30 ngay ')
elif v==2:
    
    print('thang 2 chi co 28 or 29 ngay')





#Select a day by press random key in keyboard


x=int(input("nhap so bat ky tu 0-10:"))
y=["Thu hai","thu tu","thu sau","chu nhat"]
z=["thu ba","thu nam","thu bay"]
for i in x,y,z:
    if x ==2:  
        print("La ngay thu:",y[0])
    elif x== 3:
        print("la ngay thu:",z[0])
    elif x== 4:
        print("la ngay thu:",y[0])
    elif x==5:
        print("la ngay thu:",z[1])
    elif x==7:
        print("la ngay thu:",z[2])
    elif x == 10:
        print("La ngay thu:",y[3])
    else:
        SyntaxError( "Khong thuoc ngay nao")

