#İF

x=12
b=23

if x>b:
    print("x, b'den büyüktür.")
'Baştaki boşluk önemli...'
print("b, x'den büyüktür.")

sayi=input("KARŞILAŞTIRILACAK BİRİNCİ SAYIYI GİRİNİZ: ")
sayi1=int(sayi)

sayis=input("KARŞILAŞTIRILACAK İKİNCİ SAYIYI GİRİNİZ: ")
sayi2=int(sayis)

if sayi1>sayi2:
    print("İLK GİRDİĞİNİZ SAYI DAHA BÜYÜKTÜR...")
elif sayi1<sayi2:
    print("İKİNCİ GİRDİĞİNİZ SAYI DAHA BÜYÜKTÜR...")
else:
    print("İKİ SAYI BİRBİRİNE EŞİTTİR...")

benim_string = "aysegul sarikaya"

if "aysegul" in benim_string:
    print("aysegul stringte mevcut")
else:
    print("aysegul stringte mevcut değildir.")

if "gul" in benim_string:
    print("gul stringte mevcut")

meyve_kalorileri = {"elma":100, "armut":200, "çilek":300, "muz":400}

if "çilek" in meyve_kalorileri.keys():
    print("var")
else:
    print("yok")

if 200 in meyve_kalorileri.values():
    print("var")
else:
    print("yok")

