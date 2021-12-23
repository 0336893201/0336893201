

#IDENTIFIED A SEASON IN A MONTH

g=int(input("nhap so thang:"))


if g ==3 or g<=4 :
    print(f'thang mua xuan la:{g}')

elif g >=9 and g!=12:
     print(f'thang mua thu la:{g}')

elif g >= 12 :
    print(f'thang mua dong:{g}')
elif g <= 10  :
    print(f'thang mua he la:{g}')
