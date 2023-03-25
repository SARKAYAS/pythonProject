#METODLAR VE FONKSİYONLAR
'Sınıf içindeki fonksiyonlara metod denir.'
'Fonksiyonlar:Kod bloklarıdır, girdi alabilir, çıktı verebilir, sonradan kullanılabilir.'

'Değere . konulunca çıkanlar fonksiyon/metodlardır.'

'UPPER: bütün harfleri büyütür.'
'CAPİTALİZE: baştaki harfi büyütür.'
'Her veri tipine özel metod fonk oluşturulabilir.'
''
benim_string= "atıl samancıoğlu"
print(benim_string)

benim_string.upper()
print(benim_string)
print(benim_string.upper())
buyuk_yazim= benim_string.upper()
print(buyuk_yazim)

help(benim_string.upper)
'Yardım dökümantasyonu. Uppera () koymamamızın nedeni ()in çalıştır komutu olmasıdır.'

def enBasitFonksiyon():
    'def fonk tanımlar'
    print("en basit fonk çalıştırma")

print(enBasitFonksiyon())

def fonkiki():
    x=28
    x+=4
    print(f"x'in güncel değeri: {x}")

print(fonkiki())

#INPUT & RETURN

def fonk4(isim="ayşegül"):
    print(f"merhaba {isim}")

print(fonk4())
'Buraya bir şey girmezse geliştirici alternatif olarak ayşegğl yazılır.'


def toplama(num1,num2):
    toplam=num1+num2
    print(toplam)
print("toplama:",toplama(10,20))
print("toplama:",toplama(-1000,2000))

x =None
'Değer atanmadı anlamında kullanılır.'
print("x'in değeri:",type(x))

def fonkdort(num1,num2):
    print("sayıları çarpma",num1*num2)
    return num1*num2

y = fonkdort(10,20)
print("y'nin değeri:", y)
print("y'nin tipi",type(y))


def fonkuc(gelistiriciden_isteme):
    print(f"merhaba {gelistiriciden_isteme}")
print(fonkuc("zeynep"))

isim= input("kullanıcıdan alınacak isim : ")
print(fonkuc(isim))