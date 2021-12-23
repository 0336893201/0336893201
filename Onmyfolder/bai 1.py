



import math

#S=sqrt(p*(p-a)*(p-b)*(p-c));p=(a+b+c)/2
#right triangle=a*b/2
A=float(input("NHAP SO Chieu Cao:"))
B=float(input("nhap so Canh Day:"))
C=float(input("NHAP SO canh:"))

if A==B==C:
    print("Tam Giac can")
    math.sqrt(3)
    d=float(input('nhap p:'))
    s=math.sqrt(3)*B*B/4
    print(s)
    
elif A>B:
    print("Tam Giac deu")
    

    d=float(input('nhap p:'))
    T_name=(A+B+C)/2
   
    h=math.sqrt(d)*(d-A)*(d-B)*(d-C)
    
else:
    #s=1/2a.B
    print("Tam giac vuong")
    n=A*B/2
    print(n)
    

