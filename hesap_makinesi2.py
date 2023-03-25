print(".......HESAP MAKİNESİ.......")

def hesaplama(sayi1,sayi2):
    pass

islem = input("Yapılacak işlemi giriniz:")

while True:
    if islem not in "+-*/":
        print("Lütfen doğru işlem giriniz... ")
        islem = input()
        continue
    try:
        sayi1 = float(input("Birinci sayıyı giriniz:"))
        sayi2 = float(input("İkinci sayıyı giriniz:"))
        break
    except:
        print("Lütfen doğru giriniz:")

if islem=="+":
   print(sayi2+sayi1)

elif islem== "-":
    print(sayi1-sayi2)

elif islem== "*":
    print(sayi1*sayi2)

elif islem== "/":
    print(sayi1/sayi2)
