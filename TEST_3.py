##from array import array
##import math
##X=int(input("nhap so bat ky:"))
##D=int(input("nhap so bat ky:"))

##test= X if X < D and print("SO NHAP VAO LA SO LE") else X > D and print("SO NHAP VAO LA SO CHAN")



###B=array('u',[u'\u0052'])
###print(B)
###R=B.tounicode()
###print(B)

##z=D if D==X and print("none") else X>=D==0 and print("A")
##print(z)




##def test_func(lsit1,lsit2):
##    return lsit1+ lsit2

##lsit1=[1,6,9,63,1,6,7,3]
##lsit2=[1,2,3,3,1000,3,21]

##if lsit1[0] > lsit2[5]:

##    print(list(lsit_reload))
##else:
##    "ERROR"
##lsit_reload=map(test_func,lsit1,lsit2)
##print(lsit_reload)


##print(list(lsit_reload))





#import math
#import datetime
#import time

##S=sqrt(p*(p-a)*(p-b)*(p-c));p=(a+b+c)/2
##right triangle=a*b/2
#A=float(input("NHAP SO Chieu Cao:"))
#B=float(input("nhap so Canh Day:"))
#C=float(input("NHAP SO canh:"))

#if A==B==C:
#    print("Tam Giac can")
#    d=float(input('nhap p:'))
#    s=math.sqrt(d*(d-A)*(d-B)*(d-C))
#    print(s)
    
#elif A==B:
#    print("Tam Giac deu")
#    T_name=(A+B+C)/2
#    print(T_name)

#    d=float(input('nhap p:'))
    
#    h=math.sqrt(d*(d-A)*(d-B)*(d-C))
#    print(h)

#else:
#    #s=1/2a.B
#    print("Tam giac vuong")
#    n=A*B/2
#    print(n)
    


x=int(input("nhap so bat ky tu 0-10:"))
y=["Thu hai","thu tu","thu sau","chu nhat"]
z=["thu ba","thu nam","thu bay"]
if x ==2:  
    print("La ngay thu:",y[0])
elif x== 3:
    print("la ngay thu:",z[0])
elif x== 4:
    print("la ngay thu:",y[0])
elif x==5:
    print("la ngay thu:",z[1])
elif x==7:
    print("la ngay thu:",z[3])
elif x == 10:
    print("La ngay thu:",y[3])
else:
    "Khong thuoc ngay nao"

       
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


##DO SOMETHING NEW

##b=['Thang 1','thang 3','thang 5','thang 7','thang 8','thang 10','thang 12']
##m=['thang 4','thang 6','thang 9','thang 11']
##g=['thang 2']
##if v >=12:
##    print("Nhung thang co 31 ngay la:",b)
##elif v <= 12:
##    print("Nhung thang co 30 ngay la:",m)
##elif v <=-1:
##    print("Thang co 28 or 29 ngay:",g)


NUmber_1=int(input("write some number in there:"))
numBer_2=float(input("Write some number in there:"))
Number_3=int(input("Write some number in there:"))
Number_4=float(input("Wrtie some number in there:"))

J=NUmber_1,numBer_2,Number_3,Number_4

if NUmber_1 > numBer_2 or Number_3 > Number_4:

    print(max(J))
elif NUmber_1 ==numBer_2 or Number_3 <Number_4:
    print(min(J))
else:
  "False"



#IDENTIFIED A SEASON IN A MONTH

g=int(input("nhap so thang:"))
y=int(input("nhap  so thang:"))
i=int(input("nhap  so thang:"))


if g ==3 :
    print(f'thang mua xuan la:{g,y,i}')
elif i > 10 or i >=10:
    print(f'thang mua dong:{g,y,i}')
elif i <= 10 or i >2  :
    print(f'thang mua he la:{g,y,i}')
else:
   o= print('thang mua thu la:{}'.format(g,y,i=thangmuathu['g,y,i']))
   print(o)