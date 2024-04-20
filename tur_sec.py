import linecache #dosya satırlarını okumak için eklenen modül

def tur_sec(secim):
    if secim < 1 or secim > 5:
        print("Lütfen 1-5 arasında bir sayı giriniz:")
    else:
        try:
            dosya = "kitap_bilgileri.txt"
            baslangic_satiri = (secim - 1) * 16 + 1
            for i in range(baslangic_satiri, baslangic_satiri + 16):
                satir = linecache.getline(dosya, i) #dosyanın i satırına kadar okunacağını belirtir
                print(satir.strip()) #okunan satırları yazdırır

        except FileNotFoundError:
            print("Dosya bulunamadı.")
