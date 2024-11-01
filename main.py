class Yemek:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat

    def __str__(self):
        return "{} - {} TL".format(self.ad, self.fiyat)

class Siparis:
    def __init__(self, masa_no):
        self.masa_no = masa_no
        self.yemekler = []

    def yemek_ekle(self, yemek):
        self.yemekler.append(yemek)

    def toplam_fiyat(self):
        return sum(yemek.fiyat for yemek in self.yemekler)

    def __str__(self):
        yemek_listesi = "\n".join(str(yemek) for yemek in self.yemekler)
        return "Masa {} Siparişi:\n{} \nToplam Fiyat: {} TL".format(self.masa_no, yemek_listesi, self.toplam_fiyat())

yemek1 = Yemek("Köfte", 140)
yemek2 = Yemek("Tavuk", 120)
yemek3 = Yemek("Pilav", 75)
yemek4 = Yemek("Patates Kızartması", 90)
yemek5 = Yemek("Ekmek Kadayıfı", 45)
yemek6 = Yemek("Tiramisu", 45)

siparis1 = Siparis(masa_no=1)
siparis2 = Siparis(masa_no=2)

siparis1.yemek_ekle(yemek1)
siparis1.yemek_ekle(yemek4)
siparis1.yemek_ekle(yemek6)

siparis2.yemek_ekle(yemek2)
siparis2.yemek_ekle(yemek3)
siparis2.yemek_ekle(yemek5)

print(siparis1)
print(siparis2)
