print(".......HESAP MAKİNESİ.......")
print("İŞLEMLER:")
print("1:Toplama\n2:Çıkartma\n3:Çarpma\n4:Bölme")
print("Yapacağınız işlemi giriniz:")
islem=input()
islem1=int(islem)

if islem1==1 :
    print("Toplanacak birinci sayıyı giriniz: ")
    sayi1 = input()
    print("Toplanacak ikinci sayıyı giriniz: ")
    sayi2 = input()
    print("Toplam:",float(sayi1) + float(sayi2))

elif islem1==2 :
    print("Çıkarılacak birinci sayıyı giriniz: ")
    sayi1 = input()
    print("Çıkarılacak ikinci sayıyı giriniz: ")
    sayi2 = input()
    print("Çıkartma:", float(sayi1) - float(sayi2))


elif islem1==3:
    print("Çaprılacak birinci sayıyı giriniz: ")
    sayi1 = input()
    print("Çarpılacak ikinci sayıyı giriniz: ")
    sayi2 = input()
    print("Çarpma:", float(sayi1) * float(sayi2))

elif islem1==4:
    print("Bölünecek birinci sayıyı giriniz: ")
    sayi1 = input()
    print("Bölünecek ikinci sayıyı giriniz: ")
    sayi2 = input()
    print("Bölme:", float(sayi1) / float(sayi2))

else:
    print("Yanlış sayı girdiniz...")