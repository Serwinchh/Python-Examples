
"""Uygulama 1:Bir öğrencinin bilgilerini tutunuz"""

ogrenci_adı= "Ali"
ogrenci_soyadı= "Demir"
ogrenci_adı_soyadı= ogrenci_adı+ogrenci_soyadı
ogrenci_numarası= "5412562"
ogrenci_cinsiyet= "Erkek"
ogrenci_tc_kimlik= "45621789304"
ogrenci_dogum_yili= 1999
ogrenci_yasi= 2024-ogrenci_dogum_yili

"""Uygulama 2: Kullanıcıdan 3 ürün fiyatı al ve onları topla"""

urun_1=float(input("1.Ürün fiyatını giriniz:"))
urun_2=float(input("2.Ürün fiyatını giriniz:"))
urun_3=float(input("3.Ürün fiyatını giriniz:"))
urun_toplam=urun_1+urun_2+urun_3
print("Ürünlerin Toplamı:"+str(urun_toplam))

"""Uygulama 3: Kullanıcıdan alınan yarıçap değerine göre dairenin alanını ve çevresini hesapla"""

pi=3.14
yari_cap=float(input("Dairenin yarıçapını giriniz:"))
daire_alan=pi*yari_cap**2
daire_cevre=2*pi*yari_cap
print(f"Dairenin Alanı:{daire_alan}\nDairenin Çevresi:{daire_cevre}")

"""Uygulama 4: Kullanıcıdan alınan km bilgisini mil cinsine çevir"""

km=float(input("Km cinsinden yolu giriniz:"))
mil=km*1.60
print("Mil cinsinden yolunuz:"+str(mil))