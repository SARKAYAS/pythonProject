#ATIL HOCAM SAĞ OLSUN
print(2**5)
yas=10;
print("yaşı:",yas)
print(yas*8)
yaricap=10
print("10 yarıçaplı dairenin çevresi:", 2*3.14*yaricap)
cevre=2*3.14*yaricap
print("Çevre:" , cevre)

#VERİ TİPLERİ

#Python int'i int'e bölerse float sonuç çıkartır C'nin aksine
x=10
print(type(x))
print(x/6)
print(type(x/6))
print("kalan sayıyı bulma:", 5%3)

x="merhaba"
x='merhaba '
print(x)
print(x.capitalize())  #Baştaki harfi büyük yapıyor.

print("x'in uzunluğu:", len(x))

#KULLANICIDAN VERİ ALMA

'Kullanıcıdan alınan vweri string olarak alındığı için çarpma sorunlu çıkar'

veri=input("kullanıcıdan veri al: ")

print(type(veri))

print("Girilen sayının 3 katı:" , int(veri)*3)

veri_int = int(veri)

print("Girilen sayının 10 katı: ", veri_int*10)

print(type(veri_int))
print(veri*5)  #girilen sayı/stringi 5 kere yazar
#Pythonda veri tipleri istediğimiz zaman değiştiririz.
#intecır'dan stringe geçiş olur ama stringden integır'a geçiş olmuyor.

adım= "AYŞEGÜL"
soyadım= "SARIKAYA"

tam_ismim=adım+" "+soyadım
print(tam_ismim)

print("tam adımın uzunluğu:", len(tam_ismim))

print("13. harfim: ", tam_ismim[14])

a=len(tam_ismim)

print("Son harfi alma: ", tam_ismim[a-1])
#ya da aynısını

print("Son harf bulma pyhton kısa yolu: ", tam_ismim[-1])

#STARTING INDEX - STOPPING INDEX - SLICING
#x[starting:stopping]
o= "Mal Fatma kulağıma öksürdü"

print(o)
print("Cümlenizin uzunluğu: ",len(o))
print(o[0:9])

#STEP SIZE
#x[starting:stopping:step size]

print(o[0:30:2])
print(o[::-1])   #Cümleyi tersten yazar

#IMMUTABILITY - IMMUTABLE - MUTABLE

benim_listem = [10,20,30,40,50]
'Koleksiyon: Birden fazla elemanı aynı yapı içinde tutma'
print(benim_listem[2])
print(type(benim_listem))
benim_listem[2]=100
print(benim_listem[2])
