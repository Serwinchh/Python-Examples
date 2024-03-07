# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
telefonlar = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
# 2-  Liste Kaç elemanlıdır ?
print(len(telefonlar))
# 3-  Listenin ilk ve son elemanı nedir ?
print(telefonlar[0])
print(telefonlar[-1])
# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
telefonlar[0] = "Samsung S9"
print(telefonlar)
# 5-  "Samsung S6" listenin bir elemanı mıdır ?
if "Samsung S6" in telefonlar:
      print("Samsung S6 liste içinde var.")
# 6-  Listenin -3 indeksindeki değer nedir ?
print(telefonlar[-3])

# 7-  Listenin ilk 2 elemanını alın.
print(telefonlar[:2])
# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
telefonlar[-2:] = ["Samsung S9","Samsung S10"]
print(telefonlar)

# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
telefonlar=telefonlar + ["IPhone X","IPhone XR"]
print(telefonlar)

# 10- Listenin son elemanını silin.
del telefonlar[-1]
print(telefonlar)

# 11- Liste elemanlarını tersten yazdırınız.
sonuc = telefonlar[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayınız.

      # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
      # kullaniciB: Sena Turan  1999, (80,80,70)
      # kullaniciC: Ahmet Turan 1998, (80,70,90)

ogrenciA = ["Yiğit","Bilgi",2010,[70,60,70]]
ogrenciB = ["Sena","Turan",1999,[80,80,70]]
ogrenciC = ["Ahmet","Turan",1998,[80,70,90]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]

""""""

isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append('Cenk')
print(isimler)

# 2-  "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena")
print(isimler)


# 3-  "Yiğit" ismini listeden siliniz.
isimler.remove("Yiğit")
print(isimler)

# 4-  "Hasan" isminin indeksi nedir ?
index = isimler.index('Hasan')
print(index)

# 5-  "Beril" listenin bir elemanı mıdır ?
sonuc = "Beril" in isimler
print(sonuc)

# 6-  Liste elemanlarını ters çevirin.
isimler.reverse()
yaslar.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
isimler.sort()

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort()

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
s = "IPhone X,IPhone XR"
sonuc = s.split(',')
print(sonuc)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
print(min(yaslar))
print(max(yaslar))

# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka 1: ")
markalar.append(marka)

marka = input("marka 2: ")
markalar.append(marka)

marka = input("marka 3: ")
markalar.append(marka)

print(markalar)

print(isimler)
print(yaslar)