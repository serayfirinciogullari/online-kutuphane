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
