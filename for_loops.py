sayilar = [1,5,16,35,57,72,75,10]

# 1- sayilar listesindeki her bir elemanı yazdırın.
for sayi in sayilar:
    print(sayi)

# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?
for sayi in sayilar:
    if (sayi % 5 == 0):
        print(sayi)

# 3- Sayilar listesinde sayıların toplamı kaçtır ?
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
print(toplam)

# 4- Sayilar listesindeki çift sayıların karesini alınız.
for sayi in sayilar:
    if(sayi%2==0):
        print(sayi, sayi*sayi)

urunler = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']

# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.

for urun in urunler:
    print(urun[1])

# 6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)
count = 0
for urun in urunler:
    index = urun.find('iphone')
    if (index>-1):
        count += 1
print(count)


urunler = [
    {'name':'iphone 8', 'price': '4000' },
    {'name':'iphone 8 Plus', 'price': '5000' },
    {'name':'iphone X', 'price': '6000' },
    {'name':'iphone XR', 'price': '7000' },
    {'name':'iphone 11', 'price': '8000' },
    {'name':'samsung s10', 'price': '6000' },
]

# 7- Tüm ürün bilgilerini listeleyiniz.

for urun in urunler:
    print(f"ürün adı: {urun['name']} ve ürün fiyatı: {urun['price']} TL")

# 8- Ürünlerin fiyatları toplamı nedir ?

toplam = 0
for urun in urunler:
    toplam = toplam + int(urun['price'])
print(f'ürün toplamları: {toplam} TL')

# 9- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz ?
for urun in urunler:
    if (int(urun['price']) <= 6000):
        print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")

