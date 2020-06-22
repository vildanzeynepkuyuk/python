print("Bu program kullanıcının girdiği sayıya kadar \nsayıların, karesi ve küplerini bir dosyaya yazar.\n")

#Kullanıcıdan bir sayı girmesini istedik, girilen sayıyı integer yapıp, sayi değişkenine atadık.
sayi=int(input("bir sayı giriniz: "))

#bir output.txt dosyası oluşturduk, a+ parametresi ile appendable yani eklenebilir olmasını istedik.

#Sayı, kare ve küplü sayılar için "tablo başlık satırı" oluşturduk.
#sep parametresi ile yazılacakların arasına seperator olarak tab kunulmasını istedik.
#file=output parametresi ile ekrana değil output.txt'ye yazsın istedik 
with open('output.txt', mode='a+') as output:
    print("sayı","kare","küp",sep="\t",file=output)
    print("----","----","----",sep="\t",file=output)

i=1
while (i<=sayi):
    with open('output.txt', mode='a') as output:
        print('{:,}'.format(i),'{:,}'.format(i**2),'{:,}'.format(i**3),sep="\t",file=output)
    i=i+1
    
        
