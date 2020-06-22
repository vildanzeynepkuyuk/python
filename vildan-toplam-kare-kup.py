devam=True
while (devam):
    print("\nBu program kare ve küp hesaplar veya iki sayının toplamını hesaplar")
    print("1.Kare ve Küp için 1 giriniz.")
    print("2.Toplama için 2 giriniz.")
    secenek=int(input("Seçeneğinizi Giriniz: "))


    if (secenek==1):
        a=1
        while (a==1):
            vildan=int(input("\nBir sayı giriniz : "))
            print("Girdiğiniz sayının karesi: ", vildan**2)
            print("Girdiğiniz sayının kübü: ", vildan**3)
            if (vildan==0):
                print ("kare küp bölümü bitti")
                a=5
                devam=False
        
    if (secenek==2):
        b=1
        while (b==1):
            birincisayi=int(input("\nToplanacak birinci sayıyı giriniz : "))
            ikincisayi=int(input("Toplanacak ikinci sayıyı giriniz : "))
            print("Girdiğiniz iki sayının toplamı: ", birincisayi+ikincisayi)
            if (birincisayi==0):
                print ("toplam bölümü bitti")
                b=5
                devam=False

    print("\nDevam etmek istiyormusunuz?")
    print("Devam için True yaz bitirmek için 0 yaz")
    devam=bool(input("Seçeneğinizi Giriniz: "))


print("Program gerçekten bitti : elvedaaaa..... Yeniden görüşmek üzere..")


