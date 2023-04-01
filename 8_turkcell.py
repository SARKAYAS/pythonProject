#CLASS

class Meyve():
    isim=""
    renk=""
    fiyat=""

elma=Meyve()
print(type(elma))

elma.fiyat=500
elma.renk="yeşil"
elma.isim="Amasya elması"

print("elmanın rengi:",elma.renk)
print("elmanın fiyatı:", elma.fiyat)
print("elmanın ismi:", elma.isim)

armut=Meyve()

armut.renk="sarı"

print("armutun rengi:",armut.renk)

class Bilgisayar():

    carpan=5
    def __init__(self,marka,ram,işlemci):
        self.marka = marka
        self.işlemci= işlemci
        self.ram=ram

    def ramin_yüz_katı(self):
        return self.ram*100

    def ramin_beş_katı(self):
        return self.ram* self.carpan

    def ramin_beş_katı2(self):
        return self.ram* Bilgisayar.carpan

bilgisayar1=Bilgisayar("lenovo", 20,"i7")

print("Birinci bilgisayarın işlemcisi:",bilgisayar1.işlemci)
print("Birinci bilgisayarın markası:",bilgisayar1.marka)
print("Birinci bilgisayarın rami:",bilgisayar1.ram)
print("Ramin yüz katı:", bilgisayar1.ramin_yüz_katı())
print("Ramin beş katı:", bilgisayar1.ramin_beş_katı())
print("Ramin beş katı (classtan) :", bilgisayar1.ramin_beş_katı2())

bilgisayar2=Bilgisayar("Monster",16, "i5")

print("İkinci bilgisayarın işlemcisi:",bilgisayar2.işlemci)
print("İkinci bilgisayarın markası:",bilgisayar2.marka)
print("İkinci bilgisayarın rami:",bilgisayar2.ram)
print("Ramin yüz katı:", bilgisayar2.ramin_yüz_katı())
print("Ramin beş katı:", bilgisayar2.ramin_beş_katı())
print("Ramin beş katı (classtan):", bilgisayar2.ramin_beş_katı2())

bilgisayar2.carpan=2

print("Ramin iki katı:", bilgisayar2.ramin_beş_katı())
print("Ramin iki katı (classtan):", bilgisayar2.ramin_beş_katı2())
print("\n\n\n\n\n")

#INHERITANCE = KALITIM


class Hikaye():

    def __init__(self):
        print("Hikaye sınıfında init çağırıldı.")

    def method1(self):
        print("yazarı bellidir")

    def method2(self):
        print(" giriş, gelişme ve sonuç bölümleri vardır.")

    def method3(self):
        print("olayların geçtiği zaman ve mekân bellidir.")

    def method4(self):
        print("gerçek veya gerçeğe yakın olaylar anlatılır.")

    def method5(self):
        print("anlatmaya bağlı edebi metin türüdür.")

class Roman(Hikaye):

    def __init__(self):
        Hikaye.__init__(self)
        print("Romandayız çeeek")


    def method6(self):
        print("Romanda kişi sayısı fazladır.")

benim_romanım=Roman()


print("\n.....ROMANIN ÖZELLİKLERİ.....\n")
print(benim_romanım.method6())
print(benim_romanım.method5())
print(benim_romanım.method4())
print(benim_romanım.method3())
print(benim_romanım.method2())
print(benim_romanım.method1())


#POLYMORPHISM = ÇOK ŞEKİLLİLİK


class Matematik():

    def __init__(self, isim):
        self.isim=isim

    def formul(self):
        return self.isim + " formul kullanılır."

class Fizik():
    def __init__(self,isim):
        self.isim= isim

    def formul(self):
        return self.isim + " formul kullanılır"

matematik = Matematik("Matematik")
fizik=Fizik("Fizik")

print("fizik:",fizik.formul())
print("matematik:",matematik.formul())

yeni_liste=[matematik,fizik]

for ortak in yeni_liste:
    print(ortak.formul())


class Kişi():

    def __init__(self,isim,yaş):
        self.isim=isim
        self.yaş=yaş

    def __str__(self):
        return f"adı: {self.isim} ,yaşı:{self.yaş}"

    def __len__(self):
        return self.yaş

fatma=Kişi("fatma", 22)

print("Kişi ismi:",fatma.isim)
print("Kişinin yaşı",fatma.yaş)
print(fatma)
print(len(fatma))











