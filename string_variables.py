website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(kursAdi))
# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])
# 3- 'website' içinden com karakterlerini alın.
print(website[-3:])
# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
print(kursAdi[:15])
print(kursAdi[-15:])
# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
print(kursAdi[::-1])
# 6- 'abc' ifadesini yan yana 3 defa yazdırın.
print('abc ' * 3)


website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
print(" Hello World ".strip())
print(" Hello World".lstrip())
print(" Hello World ".rstrip())
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
print("www.sadikturan.com".strip('w.moc'))
# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
print(kursAdi.lower())
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
print(website.count('a'))
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
print(website.startswith('www'))
print(website.endswith('com'))
# 6- 'website' içinde '.com' ifadesi var mı?
print(website.find('.com'))
# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(kursAdi.isalpha())
print(kursAdi.isdigit())
# 8- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
print(kursAdi.replace(' ','-'))
# 9-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print('Hello World'.replace('World','There'))
# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
kursAdi = kursAdi.lower().replace(':','')
print(kursAdi.split())