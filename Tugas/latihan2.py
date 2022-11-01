b1=input("Masukkan Bilangan Ke-1 : ")
b2=input("Masukkan Bilangan Ke-2 : ")
b3=input("Masukkan Bilangan Ke-3 : ")
print()
if b1<b2<b3:
    print("Urutan dari yang terkecil : ",b1,b2,b3)
elif b2<b3<b1:
    print("Urutan dari yang terkecil : ",b2,b3,b1)
elif b3<b1<b2:
    print("Urutan dari yang terkecil : ",b3,b1,b2)
elif b1<b3<b2:
    print("Urutan dari yang terkecil : ",b1,b3,b2)
elif b2<b1<b3:
    print("Urutan dari yang terkecil : ",b2,b1,b3)
elif b3<b2<b1:
    print("Urutan dari yang terkecil : ",b3,b2,b1)