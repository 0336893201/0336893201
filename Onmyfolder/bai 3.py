



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
else:'true'
if x < 10:
    SyntaxError("Khong thuoc ngay nao")


