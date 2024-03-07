a, b, c = 2, 5, 12
# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir ?
x = int(input("x: "))
y = int(input("y: "))

print((x * y) - (a+b+c))

# 2- c' nin  b' ye kalansız bölümünü hesaplayınız.
print(c // b)

# 3- (a,b,c) toplamının mod 3' ü nedir ?

print((a+b+c) % 3)

# 4- b' nin a. kuvvetini hesaplayınız.
print(b ** a)

# 5- a, *b, c = sayilar işlemine göre c' nin küpü kaçtır ?
sayilar = 1, 5, 7, 10, 3
a, *b, c = sayilar
print(c ** 3)

# 6- a, *b, c = sayilar işlemine göre b nin değerleri toplamı kaçtır ?
a, *b, c = sayilar
print(b[0] + b[1] + b[2])

# 1- Girilen 2 sayıdan hangisi büyüktür ?
sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))
sonuc = (sayi1 > sayi2) # True, False
print(f"{sayi1} {sayi2} den büyüktür: {sonuc}")

# 2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input('sayı: '))
sonuc = (sayi % 2 == 0)
print(f"{sayi} çift sayıdır: {sonuc}")

# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi = int(input("sayı: "))
sonuc = (sayi > 0) # Pozitif
print(f"girilen sayı pozitif: {sonuc}")

# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 = float(input("vize 1: "))
vize2 = float(input("vize 2: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")


# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
sonuc = (sayi > 50) and (sayi<=100)
print(f"{sayi}, 50 ile 100 arasındadır: {sonuc}")

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
sayi = int(input('sayı: '))
sonuc = (sayi > 0) and (sayi % 2 == 1)
print('girilen sayı pozitif tek sayıdır: ', sonuc)

# 3- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

sonuc = (x>y) and (x>z) # x en büyük
print("x en büyük sayı: ", sonuc)

sonuc = (y>x) and (y>z) # y en büyük
print("y en büyük sayı: ", sonuc)

sonuc = (z>x) and (z>y) # z en büyük
print("z en büyük sayı: ", sonuc)


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

kiloIndeks = kg / (hg ** 2)

zayif = (kiloIndeks >= 0) and (kiloIndeks <=18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <=24.9)
kilolu = (kiloIndeks > 24.9) and (kiloIndeks <=29.9)
obez = (kiloIndeks >= 29.9) and (kiloIndeks <=34.9)

print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal: {normal}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez: {obez}")

