class icecekler():
    def __init__(self,isim,fiyat):
        self.ad=isim
        self.fiyat=fiyat
    @staticmethod
    def menu():
        print("1)Cay 3TL\n2)Kahve 5TL\n3)Meyve suyu 5TL\n4)İce tea 4TL\n5)Milkshake 8TL\n6)Limonata 5TL")
        secim = input("Siparise eklemek istediginiz urunun numarasini giriniz: ")
        if(secim == "1"):
            dem = input("Demli mi olsun acik mi: ")
            c = cay(dem)
            c.ad += dem
            print("Cay eklenmiştir.")
            return c
        elif(secim == "2"):
            seker = input("Kac sekerli: ")
            k = kahve(seker)
            k.ad += "seker:"+seker
            print("Kahve eklenmiştir.")
            return k
        elif(secim == "3"):
            aroma = input("Meyve suyu aromasi: ")
            seker = input("Sekerli mi sekersiz mi: ")
            m =meyvesuyu(aroma,seker)
            m.ad += "aroma:"+aroma +"seker:"+ seker
            return m
        elif(secim == "4"):
            aroma = input("Ice tea aromasi: ")
            i = ice_tea(aroma)
            i.ad += "aroma:" + aroma
            print("Ice tea eklenmiştir.")
            return i
        elif(secim == "5"):
            aroma = input("Milkshake aromasi: ")
            m = milkshake(aroma)
            m.ad += "aroma:" + aroma
            print("Milkshake eklenmiştir.")
            return m
        elif(secim == "6"):
            seker = input("Limonata sekerli mi: ")
            l = limonata(seker)
            l.ad += "seker:" +seker
            print("Limonata eklenmiştir.")
            return l
    # isim fiyat 

class cay(icecekler):
    def __init__(self,tat):
        super().__init__("cay", 3)
        self.tat=tat
    #demli açık
    
class kahve(icecekler):
     def __init__(self,seker):
        super().__init__("kahve", 5)
        self.seker=seker
        
class meyvesuyu(icecekler):    
    def __init__(self,aroma,seker):
        super().__init__("meyvesuyu", 5)
        self.seker=seker
        self.aroma=aroma

    #şekerli şekersiz
    #portakal vişne ananas mango elma kayısı
    
class ice_tea(icecekler):
   def __init__(self,aroma):
       super().__init__("ice_tea",4)
       self.aroma=aroma
    #şeftali limon karpuz 
    

class milkshake(icecekler):
    def __init__(self,aroma):
       super().__init__("milkshake",8)
       self.aroma=aroma
    #çilek çikolata  
    
class limonata(icecekler):
    def __init__(self,seker):
       super().__init__("limonata",5)
       self.seker=seker 
    #şekerli şekersiz

class yiyecekler():
    def __init__(self,ad,gram,fiyat):
        self.ad = ad
        self.gram = gram
        self.fiyat = fiyat
    @staticmethod
    def menu():
        print("Tost cesitleri 5TL\t1)Kasarli\t2)Sucuklu\t3)Karisik\n4)Patates kizartma 15TL\nMenemen cesitleri 30TL\t5)Sade\t6)Kasarli\t7)Sucuklu\t8)Kavurmali")
        secim = input("Siparise eklemek istediginiz urunun numarasini giriniz: ")
        if(secim =="1"):
            t = tost()
            print("Kasarli tost eklenmistir.")
            return t
        elif(secim =="2"):
            t = sucukluTost()
            print("Sucuklu tost eklenmistir.")
            return t
        elif(secim =="3"):
            t = karisikTost()
            print("Karisik tost eklenmistir.")
            return t
        elif(secim =="4"):
            p = patatesKizartma()
            print("Karisik tost eklenmistir.")
            return p
        elif(secim =="5"):
            m = menemen()
            print("menemen eklenmiştir.")
            return m
        elif(secim =="6"):
            m = kasarliMenemen()
            print("menemen eklenmiştir.")
            return m
        elif(secim =="7"):
            m = sucukluMenemen()
            print("menemen eklenmiştir.")
            return m
        elif(secim =="8"):
            m = kavurmalıMenemen()
            print("menemen eklenmiştir.")
            return m
        
class tost(yiyecekler):
    def __init__(self,ad ="kasarliTost"):
        super().__init__(ad,250,5)
class sucukluTost(tost):
    def __init__(self):
        super().__init__("sucukluTost")
class karisikTost(tost):
    def __init__(self):
        super().__init__("karisikTost")
        
class patatesKizartma(yiyecekler):
    def __init__(self):
        super().__init__("patatesKizartma", 150,15)

class menemen(yiyecekler):
    def __init__(self,tur="sadeMenemen"):
        super().__init__(tur, 500,30)
class kasarliMenemen(menemen):
    def __init__(self):
        super().__init__("kasarliMenemen")
class sucukluMenemen(menemen):
    def __init__(self):
        super().__init__("sucukluMenemen")
class kavurmalıMenemen(menemen):
    def __init__(self):
        super().__init__("kavurmalıMenemen")

class tatlilar():
        def __init__(self,ad,serbet,fiyat):
            self.ad = ad
            self.serbet = serbet
            self.fiyat = fiyat
        @staticmethod
        def menu():
            print("1)Baklava 70TL\n2)Sutlac 20TL\n3)Pasta 50TL")
            secim = input("Siparise eklemek istediginiz urunun numarasini giriniz: ")
            if(secim == "1"):
                miktar = input("Kac porsiyon baklava: ")
                b = baklava(miktar)
                b.ad += "miktar:"+miktar
                print(str(miktar)+" porsiyon baklava eklenmiştir.")
                return b
            elif(secim == "2"):
                miktar = input("Kac tabak sutlac: ")
                s = sutlac(miktar)
                s.ad += "miktar:"+miktar
                print(str(miktar)+" tabak sutlac eklenmistir.")
                return s
            elif(secim == "3"):
                tat = input("Pasta neli olsun: ")
                p = pasta(tat)
                p.ad = "aroma:" +tat
                print(tat+" pasta eklenmistir.")
                return p


class baklava(tatlilar):
    def __init__(self,miktar):
        self.miktar = miktar
        super().__init__("baklava","serbetli",miktar*70)

class sutlac(tatlilar):
    def __init__(self,miktar):
        self.miktar = miktar
        super().__init__("sutlac","serbetsiz",miktar*20)

class pasta(tatlilar):
    def __init__(self,neli):
        self.neli = neli
        super().__init__("pasta","serbetsiz",50)
        
def dosyaOku(dosyaAdi):
    dosya = open(dosyaAdi,"r")
    icerik = dosya.readlines()
    dosya.close()
    return icerik
def dosyaYaz(dosyaAdi,deger):
    dosya = open(dosyaAdi,"r")
    icerik = dosya.readline()
    dosya.close()
    dosya = open(dosyaAdi,"w")
    dosya.write(icerik+deger)
    dosya.close()
        
class siparisler():
    def __init__(self):
        self.siparisList = []
    def siparisEkle(self,masaNo):
        m = masa(masaNo)
        kayit = "Masa no:"+masaNo+" Siparis: "
        while True:
            secim = input("1)Yiyecek icin 1 yaziniz\n2)Icecek icin 2 yaziniz\n3)Tatli icin 3 yaziniz\n4)Siparisi tamamlamak icin 4 yaziniz\n")
            if(secim == "1"):
                print("Yiyecekler")
                urun = yiyecekler.menu()
            elif(secim == "2"):
                print("Icecekler")
                urun = icecekler.menu()
            elif(secim == "3"):
                print("Tatlilar")
                urun = tatlilar.menu()
            else:
                print("Siparis tamamlandi.")
                break     
            m.siparisEkle(urun)
            kayit += urun.ad +" "
        self.siparisList.append(m)
        dosyaYaz("siparis.txt",kayit+"\n")
    def paketSiparis(self,adres):
        p = paketServis()
        p.setAdres(adres)
        kayit = "Adres: "+p.getAdres()+" Siparis: "
        while True:
            secim = input("1)Yiyecek icin 1 yaziniz\n2)Icecek icin 2 yaziniz\n3)Tatli icin 3 yaziniz\n4)Siparisi tamamlamak icin 4 yaziniz\n")
            if(secim == "1"):
                print("Yiyecekler")
                urun = yiyecekler.menu()
            elif(secim == "2"):
                print("Icecekler")
                urun = icecekler.menu()
            elif(secim == "3"):
                print("Tatlilar")
                urun = tatlilar.menu()
            else:
                print("Siparis tamamlandi.")
                break 
            p.siparisEkle(urun)
            kayit += urun.ad +" "
        self.siparisList.append(p)
        dosyaYaz("siparis.txt",kayit+"\n")
    def siparisTamamla(self):
        tmp = self.siparisList.pop(0)
        siparisDosya = dosyaOku("siparis.txt")
        tamamlananSiparis = siparisDosya.pop(0)
        dosyaYaz("hasilat.txt",tamamlananSiparis+str(tmp.hesap)+"TL")
        dosya = open("siparis.txt","w")
        for i in siparisDosya:
            dosya.write(i)
        dosya.close()
        print(tamamlananSiparis+str(tmp.hesap)+"TL")
           
class servis():
    def __init__(self):
        self.hesap = 0
        self.siparis = []
    def siparisEkle(self,s):
        self.hesap += s.fiyat
        self.siparis.append(s)
class masa(servis):
    def __init__(self,masaNo):
        self.masaNo = masaNo
        super().__init__()

class paketServis(servis):
    def __init__(self):
        self.__adres = ""
        super().__init__()
    def getAdres(self):
        return self.__adres
    def setAdres(self,a):
        self.__adres = a

d = open("siparis.txt","w")
d.close()
d = open("hasilat.txt","w")
d.close()
s = siparisler()
while True:
    secim = input("1)Siparis eklemek icin 1 yazin\n2)Siparis tamamlamak icin 2 yazin\n3)Siradaki siparisi görmek icin e yazin\n4)Kapatmak icin 4 yazin\n")
    if(secim == "1"):
        if(input("1)Paket servis icin 1 yazin\n2)Acik servis icin 2 yazin\n")=="1"):
            s.paketSiparis(input("Adres giriniz: "))
        else:
            s.siparisEkle(input("Masa numarasini giriniz: "))
    elif(secim == "2"):
        if(len(s.siparisList)>0):
            s.siparisTamamla()
        else:
            print("Bekleyen siparis yok.")
    elif(secim =="3"):
        if(len(s.siparisList)>0):
            d = dosyaOku("siparis.txt")
            print(d[0])
        else:
            print("Bekleyen siparis yok.")
    else:
        break
