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
                                print(satir.strip()) 
                            satir = dosya.readline()
                            sayac += 1
                    sayac += 1
                    satir = dosya.readline()