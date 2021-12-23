
A=float(input("NHAP SO Chieu Cao:"))

B=float(input("nhap so Canh Day:"))
C=float(input("NHAP SO canh:"))

if A==B==C:
    print("Tam Giac can")
    d=float(input('nhap p:'))
    s=math.sqrt(d*(d-A)*(d-B)*(d-C))
    print(s)
    
elif A==B:
    print("Tam Giac deu")
    T_name=(A+B+C)/2
    print(T_name)

    d=float(input('nhap p:'))
    
    h=math.sqrt(d*(d-A)*(d-B)*(d-C))
    print(h)

else:
    #s=1/2a.B
    print("Tam giac vuong")
    n=A*B/2
    print(n)
    