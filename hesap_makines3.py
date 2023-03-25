print(".......HESAP MAKİNESİ.......")
print("İŞLEMLER:")
print("1:Toplama\n2:Çıkartma\n3:Çarpma\n4:Bölme")

while True:
    islem1 = input("Yapacağınız işlemin sayısını giriniz:")
    islem = int(islem1)

    if islem>0 and islem<5:
        break
    else:
        print("Yanlış sayı girdiniz lütfen doğru sayı giriniz:")
        continue


if islem==1:
    def toplama(sayi1,sayi2):
        return sayi1+sayi2
    a=float(input("Toplanacak 1. sayıyı giriniz:"))
    b=float(input("Toplanacak 2. sayıyı giriniz:"))
    print("Girdiğiniz sayıların toplamı:",toplama(a,b))

elif islem==2:
    def çıkartma(sayi1, sayi2):
        return sayi1 - sayi2


    a = float(input("Çıkartılacak 1. sayıyı giriniz:"))
    b = float(input("Çıkartılacak 2. sayıyı giriniz:"))
    print("Girdiğiniz sayıların farkı:", çıkartma(a, b))

elif islem==3:
    def çarpma(sayi1, sayi2):
        return sayi1 * sayi2


    a = float(input("Çarpılacak 1. sayıyı giriniz:"))
    b = float(input("Çarpılacak 2. sayıyı giriniz:"))
    print("Girdiğiniz sayıların çarpımı:", çarpma(a, b))

elif islem==4:
    def bölme(sayi1, sayi2):
        return sayi1 / sayi2


    a = float(input("Bölünen sayıyı giriniz:"))
    b = float(input("Bölen sayıyı giriniz:"))
    print("Girdiğiniz sayıların bölümü:", bölme(a, b))






