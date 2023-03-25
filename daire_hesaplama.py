#DAİRENİN ÇEVRE VE ALANINI BULMA
print("MENÜ: ")
print("1:DAİRENİN ÇEVRESİ")
print("2:DAİRENİN ALANI")

sayi=input("Yapacağınız işlemi seçiniz:")
sayi1=int(sayi)

if sayi1==1 :
    yaricap = input("Dairenin yarıçapını giriniz:")

    pi = 3.14

    print(float(yaricap) * 2 * pi)

else:

        cap = input("DAİRENİN ÇAPINI GİRİNİZ:")

        yaricap = float(cap) / 2

        pi = 3.14

        print("Dairenin alanı: ", yaricap * yaricap * pi)