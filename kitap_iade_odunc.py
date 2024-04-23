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