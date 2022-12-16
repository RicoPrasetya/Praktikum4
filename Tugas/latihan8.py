a=input("Masukkan Bilangan Ke-1 : ")
b=input("Masukkan Bilangan Ke-2 : ")
c=input("Masukkan Bilangan Ke-3 : ")
print()
if a > b:
    if a > c:
        maks = a
else:
    if b > c:
        maks = b
    else:
        maks = c
print("Bilangan Terbesar : ", maks)