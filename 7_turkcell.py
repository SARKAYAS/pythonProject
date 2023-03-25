#ÇIKTI VERME

def fonkbir(a):
    if a=="python":
        return "python yazdınız."
    elif a=="java":
        return "java verdiniz."
    elif a=="kotlin":
        return "kotlin verdiniz."
    else:
        return "popüler dilleri vermediniz."

print(fonkbir("python"))
print(fonkbir("c"))
print(fonkbir("flutter"))
print(fonkbir("java"))

#ARGS - KWARGS
#Args: belirsiz sayı demek
#Kwargs: Sözlük vermek için kullanılır.
#Tek yıldız (*) birden fazla argüman, iki yıldız(**) birden fazla key verilebilir.


'Sadece * ile de olur.'
def sonsuzToplama(*args):
    return sum(args)

print(sonsuzToplama(10,20,50,100,80,900,70,65,45,14))
print(sonsuzToplama(10,2,3))

def fonkiki(**kwargs):
    return(kwargs)

print(fonkiki(muz=100,elma=300,karpuz=500))
print(type(fonkiki(muz=100,elma=300,karpuz=500)))

def ikiyleCarp(numara):
    return numara*2
print("28 sayısının 2 ile çarpımı:",ikiyleCarp(28))

numara_listesi= [10,20,30,40,50,60,70,80,90]
yeni_liste=[]

for eleman in numara_listesi:
    yeni_liste.append(ikiyleCarp(eleman))
print("Listenin 2 ile çarpımı:" ,yeni_liste)

#MAP
#Bir veri/veri dizisinin başka bir veriye/veri dizisine çevirmek için kullanılır

print(map(ikiyleCarp,numara_listesi))
print(list(map(ikiyleCarp,numara_listesi)))
'Soldaki elemanlar sağdaki fonksiyona tabii tutulur.'

def stringKontrol(s):
    return "gül" in s

string_liste= ["ayşegül","gülistan","gülazer","fatma","gülsüm","gülsün","ramazan"]

print(list(map(stringKontrol,string_liste)))

#FİLTER
#Map ile benzer ancak sadece filtreleme yapar.

print(list(filter(stringKontrol,string_liste)))
'Sadece true/false yazıp bırakmaz. True olan değerleri getirir.'

#LAMBDA
#Anonim tek satırlık, bir defa kullanacağımız fonksiyonlara denir.

def ucleCarp(num):
    return num*3
print("20nin 3 katı:",ucleCarp(20))


carpma= lambda num: num*3
'input:output'
'Buradaki carpma fonksiyondur.'
print(f"20nin 3 katı: {carpma(20)}")


print(list(filter(lambda string : "a" in string, string_liste)))
'İçinde sadece a harfi geçen elemanları alır.'


#SCOPE (KAPSAM)
#LOCAL, ENCLOSING, GLOBAL, BUILT-IN
#DERLEYİCİ DERLERKEN ÜSTTEKİ SIRAYLA DERLER.
#Built-in: Hiçbir tanımlama yapılmazsa sistemde ne kayıtlı ise onu çağırır.

superkahraman="spiderman"
'GLOBAL'

def ornekFonk():
    superkahraman="batman"
    'Enclosing'

    def icFonk():
        superkahraman= "IRON MAN"
        'LOCAL'
        print(superkahraman)

    icFonk()

print(ornekFonk())
print(superkahraman)


z=5

def yeniFonk():
    global z
    z=10
    print(z)
'Global fonksiyonu değiştiririz.'

print(yeniFonk())
print(z)

while True:
    try:
        yeni_int = int(input("Numaranızı giriniz:"))
    except:
        print("Yanlış girdiniz.")
        continue
    else:
        print("Teşekkürler")
        break
    finally:
        print("Finally çağırıldı.")
    'Hep çağırılır.'




