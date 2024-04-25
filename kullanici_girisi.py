def kitap_bilgisi():
    kitap_kontrol = False
    while not kitap_kontrol:
        kitap_ismi = input("Bilgilerini görüntülemek istediğiniz kitabın ismini giriniz: ").strip().upper()
        sayac = 0
        with open("kitap_bilgileri.txt", "r") as dosya:
            while True:
                satir = dosya.readline()
                sayac += 1
                if satir.strip() == kitap_ismi:
                    print("\nGirdiğiniz kitap kütüphane arşivinde mevcuttur.\n")
                    kitap_kontrol = True
                    for i in range(1, 8):
                        if i == 1:
                            print("Kitabın ismi:",satir.strip().capitalize())
                        elif i == 2:
                            print("Kitabın ISBN numarası:",satir.strip())
                        elif i == 3:
                            print("Kitabın yazarı:",satir.strip())
                        elif i == 4:
                            print("Kitabın yayınevi:",satir.strip())
                        elif i == 5:
                            print("Kitabın yayın yılı:", satir.strip())
                        elif i == 6:
                            print("Kitabın stok adedi:",satir.strip())
                        else:
                            print("Kitabın Türü:",satir.strip())
                        satir = dosya.readline()
                        sayac += 1
                if not satir:
                    break
            if kitap_kontrol:
                break
        if not kitap_kontrol:
            print("Girdiğiniz kitap kütüphane arşivinde bulunmamaktadır. Lütfen tekrar deneyiniz.")

def tur_sec(secim):

    if secim < 1 or secim > 5:
        print("Lütfen 1-5 arasında bir sayı giriniz:")
    else:
        if secim == 1:
            print("\nKişisel Gelişim Kategorisindeki Kitaplar:")
        elif secim == 2:
            print("\nEğitim kategorisindeki kitaplar:")
        elif secim == 3:
            print("\nHukuk kategorisindeki kitaplar:")
        elif secim == 4:
            print("\nBilim kategorisindeki kitaplar:")
        elif secim == 5:
            print("\nTarih kategorisindeki kitaplar:")
        with open("kitap_bilgileri.txt", "r") as dosya:
            sayac = 1
            satir = dosya.readline() 

            while True:  # Dosya sonuna kadar oku
                if satir == "":
                    break
                else:
                    if sayac == (14 * (secim - 1)) + 1: #kullanıcı kaçıncı kitabı seçerse o kitabın ilk bilgisinin bulunduğu satırı veren işlem
                        for i in range(1, 9):
                            if i == 1 or i == 8:
                                print(satir.strip().capitalize()) 
                            satir = dosya.readline()
                            sayac += 1
                    sayac += 1
                    satir = dosya.readline()

def kitap_odunc_alma():
    kitap_kontrol = False
    while not kitap_kontrol:
        kitap_ismi = input("Kitap ismi gir: ").strip().upper()
        sayac = 0
        with open("kitap_bilgileri.txt", "r+") as dosya:
            while True:
                satir = dosya.readline()
                sayac += 1
                if satir.strip() == kitap_ismi:
                    print("Girdiğiniz kitap kütüphane arşivinde mevcuttur.")
                    kitap_kontrol = True
                    for i in range(1, 7):
                        satir = dosya.readline()
                        sayac += 1
                        if i == 5:
                            print("Kitabın stok adedi:", satir.strip())
                            stok_adedi = int(satir.strip())
                            karakter = dosya.tell()
                    if stok_adedi != 0:
                        odunc_alma = input("Kitabı ödünç almak için e/E çıkış yapmak için herhangi bir harf giriniz: ")
                        if odunc_alma.lower() == "e":
                            guncel_stok = stok_adedi - 1
                            dosya.seek(karakter - 3)
                            dosya.write(str(guncel_stok))
                            print("Kitap başarıyla ödünç alındı ^^")
                        else:
                            print("Çıkış yapılıyor")
                    else:
                        print("Kitap stokta bulunmamaktadır")
                if not satir:
                    break
            if kitap_kontrol:
                break
        if not kitap_kontrol:
            print("Girdiğiniz kitap kütüphane arşivinde bulunmamaktadır. Lütfen tekrar deneyiniz.")

def kitap_iade():
    kitap_kontrol = False
    while not kitap_kontrol:
        kitap_ismi = input("Kitap ismi gir: ").strip().upper()
        sayac = 0
        with open("kitap_bilgileri.txt", "r+") as dosya:
            dosya.seek(0)  # Dosyanın başına dön
            satir = dosya.readline()
            sayac += 1
            while satir:
                if satir.strip() == kitap_ismi:
                    print("Girdiğiniz kitap kütüphane arşivinde mevcuttur.")
                    kitap_kontrol = True
                    iade_secim = input("İade işlemini gerçekleştirmek için e/E çıkış yapmak için herhangi bir harf basınız: ")
                    if iade_secim.lower() == "e":
                        for i in range(sayac, sayac + 6):
                            satir = dosya.readline()
                            if i % 7 == 5:
                                guncel_stok = int(satir.strip()) + 1
                                karakter = dosya.tell()
                                dosya.seek(karakter - 3)
                                dosya.write(str(guncel_stok))
                                print("İade işleminiz başarıyla gerçekleşmiştir.")
                    else:
                        print("Çıkış yapılıyor...")
                        break
                satir = dosya.readline()
                sayac += 1
            if not kitap_kontrol:
                print("Girdiğiniz kitap ismi kütüphane arşivinde mevcut değildir.")