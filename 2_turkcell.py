#ATIL HOCAM SAĞ OLSUN VOL2

#KOLEKSİYONLAR

#IMMUTABILITY - IMMUTABLE - MUTABLE

benim_listem = [10,20,30,40,50]
'Koleksiyon: Birden fazla elemanı aynı yapı içinde tutma'
print(benim_listem[2])
print(type(benim_listem))
benim_listem[2]=100
print(benim_listem[2])

numara_listem=[10,20,10,20,20]
print(numara_listem)
print(type(numara_listem))
numara_listem.append(50)
print("50 ekledikten sonra:" ,numara_listem)

print("20den kaç tane var listede:",numara_listem.count(20))

print("10dan kaç tane var listede:",numara_listem.count(10))

print("50den kaç tane var listede:",numara_listem.count(50))

numara_listem.pop()
#Son elemanı listeden atar.

print(numara_listem)

numara_listem.reverse()
print(numara_listem)
#Listeyi tersine çevirir.

numara_listem.remove(10)
print(numara_listem)
#10 sayısının 1 tanesini çıkartır.

numara_listem.sort()
print(numara_listem)
#Dizmeye çalışır, harf ise alfabetik; sayı ise sırayla


liste1=['a',"g","c","d"]
liste2=["1","2","3"]

print("1:",liste1)
print("2:",liste2)

liste12=liste1+liste2
print("1+2=", liste12)

liste21=liste2+liste1
print("2+1=", liste21)

print("1'i 3 kere yazdırır:" ,liste1*3)

liste12.sort()
print(liste12)

#liste2=[1,2,3]
#liste21.sort()
#print(liste21)
#BAŞTA BÖYLE YAZILSAYDI KOD SIRALAMA OLMAZDI ÇÜNKÜ İNT VE STRİNG ARALARINDA SIRALANMAZ.

liste_karisik=[2,8,"hello",3.14]
print("1.eleman:", type(liste_karisik[0]))
print("3.eleman:", type(liste_karisik[2]))
print("4.eleman:", type(liste_karisik[3]))

#NESTED LİST (İÇ İÇE GEÇMİŞ LİSTELER

nested_list=[1,"world",["a","b"],"KJ",[2,4,8]]
print(nested_list)
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(type(nested_list[2]))
print(nested_list[3])
print(nested_list[4])
print(nested_list[4][2])

#DICTIONARY - SÖZLÜK ( {} kullanılır.)
#dictionay= {keys:values}


benim_sozluk= {"anahtarkelime" : "değer"}
print(benim_sozluk["anahtarkelime"])

meyve_kalorileri = {"elma":100, "armut":200, "çilek":300, "muz":400}
print(type(meyve_kalorileri))
print(meyve_kalorileri)
print("Elmanın kalorisi:", meyve_kalorileri["elma"])

print(meyve_kalorileri.keys())
print(meyve_kalorileri.values())

'Yeni veri ekleme'
meyve_kalorileri["karpuz"]=800
print(meyve_kalorileri)

'Veri değerini değiştirme'
meyve_kalorileri["armut"]=280
print(meyve_kalorileri)

'Garip sözlük'
garip_sozluk={1:"atıl", 2:"zeynep"}
print(garip_sozluk[1])
print(garip_sozluk[2])

'Sayı ve değer yerleri karışık sözlük'
karisik_sozluk= {100:"anahtar", "değer":200}
print(karisik_sozluk[100])
print(karisik_sozluk["değer"])

'Liste Sözlük Karışık'
listeli_sozluk= {"anahtar1":100, "anahtar2":[0,1,2,3,4,5,6,7,8,9], "anahtar3":{"anahtar31":2023}}
print(listeli_sozluk["anahtar1"])
print(listeli_sozluk["anahtar2"])
print(listeli_sozluk["anahtar3"])
print(listeli_sozluk["anahtar2"][5])
print(listeli_sozluk["anahtar2"][0])
print(listeli_sozluk["anahtar3"]["anahtar31"])


#SETLER
'Birden fazla barındırılan elemanları siler'

set_liste=[1,2,3,4,5,"a","b",2,"b"]
print(type(set_liste))

set1=set(set_liste)
print(set1)
print(type(set1))

benim_setim={"a","s",2,8,8,"s"}
print(benim_setim)

'SET DE SÖZLÜK DE KÜME PARANTEZİ İLE GÖZTERİLİR'
'Boş küme parantezi ile tanımlarsak sözlük olarak algılanır.'

benim_setim.add(28)

print(benim_setim)

set_liste2={1,2,9,3,4,5,6,7,8,0,0,"k","j","x","x",7}
set2=set(set_liste2)
print(set2)
print(type(set2))
'Sıraya da koyuyor.'

setten_listeye=list(set2)
print(setten_listeye)
print(type(setten_listeye))
'Setten listeye tekrar çevirirken önceki çoğul sayılar gitmiş olur.'


#TUPLE
'LİSTENİN AYNISI'
'NORMAL PARANTEZLE OLUŞUR.'
'ANCAK İÇİNE EKLEME YAPILAMAZ. KÜTÜPHANE KULLANIMINDA VE DEĞİŞTİRİLEMEZ VERİLERDE KULLANILIR BU KOLEKSİYON'

benim_tuple=(1,2,5,5,"z")
print(benim_tuple)
print(type(benim_tuple))
print(benim_tuple.count(5))




#**********    ÖZET   **********



#LİSTELERDE [] KULLANILIR.
  #öRNEĞİN:

only_liste=[10,20,"a"]


#SÖZLİKLERDE {} KULLANILIR.
  #DİCTİONRY= {"KEYS":"VALUES"}

  #ÖRNEĞİN:

only_dictionary={"seni" : "seviyorum"}


#SETLERDE {} KULLANILIR.
  #LİSTE VE DİCTİONARY'NİN KARIŞIMI GİBİ

only_set={"ayşo",2,8,}


#TUPLE () KULLANILIR.

benim_tuple=("hello",1,"world",2)
