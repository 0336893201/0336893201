

#FIND MAX,OR MIN???
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
