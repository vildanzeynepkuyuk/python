sayi1 = int(input("\nBirinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

buyuk = sayi1 if sayi1 >= sayi2 else sayi2
kucuk = sayi1 if sayi1 < sayi2 else sayi2

kalan = 1
bolum = 0

while kalan!=0:
    bolum = buyuk // kucuk
    kalan = buyuk % kucuk
    buyuk = bolum
    kucuk = kalan


print("Bölüm: ", bolum)