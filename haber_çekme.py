import requests
from bs4 import BeautifulSoup

# Veri toplanacak web sayfasının URL'si
url = 'https://www.example.com'

# Web sayfasını almak için GET isteği yapılır
response = requests.get(url)

# Web sayfasının içeriği BeautifulSoup ile parse edilir
soup = BeautifulSoup(response.text, 'html.parser')

# Tüm başlıkları (h1 etiketleri) bul
basliklar = soup.find_all('h1')

# Her başlığı ekrana yazdır
for baslik in basliklar:
    print(baslik.text)