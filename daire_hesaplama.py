from math import pi

#DAİRENİN ÇEVRE VE ALANINI BULMA
print("MENÜ: ")
print("1:DAİRENİN ÇEVRESİ")
print("2:DAİRENİN ALANI")

sayi=input("Yapacağınız işlemi seçiniz:")
sayi1=int(sayi)

#Importu tam olarak öğrenmediyseniz onun yerine burda pi sayısını kendiniz tanımlamalısınız.
#pi=3.14

if sayi1==1 :
    yaricap = input("Dairenin yarıçapını giriniz:")


    print(float(yaricap) * 2 * pi)

elif sayi1==2:

        cap = input("Dairenin çapını giriniz:")

        yaricap = float(cap) / 2


        print("Dairenin alanı: ", yaricap * yaricap * pi)

else:
    print("Yanlış sayı girdiniz...")

