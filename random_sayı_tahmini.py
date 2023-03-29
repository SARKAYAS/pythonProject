from random import randint
rand = randint(1, 10)
sayac = 0

sayi= int(input("1-10 arası sayı giriniz:"))

if rand==sayi:
    print("Doğru tahmin")

else:
    print("Yanlış tahmin, doğru sayı:", rand)


