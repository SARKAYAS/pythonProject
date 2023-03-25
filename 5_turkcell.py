#FOR DÖNGÜSÜ

numara_listesi = [10,20,30,40,50,60,80,70,90]

print("DÖNGÜ BAŞLADI")
for numara in numara_listesi:
    print(numara/5+2)
print("DÖNGÜ BİTTİ")

tek_cift= [10,52,44,65,87,5456478,15215,349,268,10,52]


ornek_set=set(tek_cift)
print(ornek_set)

for sayi in ornek_set:
    if sayi%2==0:
        print(sayi, "SAYISI ÇİFTTİR")
    elif sayi%2==1:
        print(sayi, "SAYISI TEKTİR")

karmasik_liste = [(1,2),(3,6),(5,10),(9,7),(4,8)]

for eleman in karmasik_liste:
    print(eleman)

for (a,b) in karmasik_liste:
    print("ilk elemanlar:",a)
for (a,b) in karmasik_liste:
    print("ikinci elemanlar" ,b)

meyve_kalorileri = {"elma":100, "armut":200, "çilek":300, "muz":400}

for (anahtar,keys) in meyve_kalorileri.items():
    print("anahtarlar:",anahtar)

for (anahtar,keys) in meyve_kalorileri.items():
    print("keys:", keys)

liste=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]

for number in liste:
    if number==100:
        break
    print(number)

for number in liste:
    if number==100:
        '100 sayısını atlar.'
        continue
    print(number)

for number in liste:
    pass

#WHILE

print("\n")
print("While döngüsüne geçtik...\n")

x = 0
while x<10:
    print(x)
    x=x+1
