

#Select a day by press random key in keyboard

v=int(input("nhap so bat ky tu 1-12:"))
if v==2:
    print('thang 2 chi co 28 or 29 ngay')

if v == 1 :
    print('thang 1 co 31 ngay')
elif v==3 :
    print('thang 3 co 31 ngay')
elif v==5 :
    print('thang 5 co 31 ngay')
elif v==7:
    print('thang 7 co 31 ngay')
elif v==8:
    print('thang 8 co 31 ngay')
elif v==10:
    print('thang 10 co 31 ngay')
elif v==12:
    print('thang 12 co 31 ngay')


if v==4 or v>=6:
    print('thang 4 co 30 ngay')


elif v > 7 :
    print('thang 9 va thang 11 deu co 30 ngay ')

if v==6:
    print('thang 6 co 30 ngay')
