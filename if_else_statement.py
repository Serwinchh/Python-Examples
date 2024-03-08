# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
if  (sayi > 50) and (sayi<=100):
    print(f"{sayi}, 50 ile 100 arasındadır.")
else:
   print(f"{sayi}, 50 ile 100 arasında değildir.")

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
if (sayi > 0):
    if (sayi % 2 == 1):
        print('girilen sayı pozitif tek sayıdır.')
    else:
        print('sayı pozitif ancak tek değil.')
else:
    print('girilen sayı negatif.')

# 3- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if (x>y) and (x>z):
    print("x en büyük sayı: ")
elif (y>x) and (y>z):
    print("y en büyük sayı: ")
elif (z>x) and (z>y):
    print("z en büyük sayı: ")


# 4- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.

ad = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

kiloIndeks = kg / (hg ** 2)

if (kiloIndeks >= 0) and (kiloIndeks <=18.4):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf.")
elif (kiloIndeks > 18.4) and (kiloIndeks <=24.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal.")
elif (kiloIndeks > 24.9) and (kiloIndeks <=29.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu.")
elif (kiloIndeks >= 29.9) and (kiloIndeks <=34.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez.")
else:
    print('bilgileriniz yanlış.')


# 5- Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.

benzinFiyat = float(input("Benzin Fiyatı:"))
dizelFiyat = float(input("Dizel Fiyatı:"))
toplamYakitUcreti = 0

ortalamaYakitTuketimi = float(input('100 km deki ortalama yakıt tüketimi: '))
gidilecekYol = float(input('gidilecek yol kaç km: '))
yakitTipi = input('yakıt tipiniz nedir: ')

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif (yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
else:
    print('yanlış yakıt tipi girdiniz.')

if (toplamYakitUcreti != 0):
    print(toplamYakitUcreti)



# 6- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 

isim = input('isim: ')
yas = int(input('yaş: '))
egitim = input('eğitim: ')

if (yas >= 18):
    if (egitim == 'lise' or egitim == 'üniversite'):
        print('ehliyet alabilirsiniz.')
    else:
        print(f'{isim} ehliyet alamazsınız çünkü eğitim durumu yetersiz.')
else:
    print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor.')



# 7- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.

import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/7/11)')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<= 365):
    print('1.servis bakımı.')
elif (gun>365) and (gun<=365*2):
    print('2.servis bakımı')
elif (gun>=365*2) and (gun<=365*3):
    print('3.servis bakımı')
else:
    print('hatalı bilgi girdiniz.')