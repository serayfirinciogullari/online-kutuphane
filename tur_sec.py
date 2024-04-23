def tur_sec(secim):

    if secim < 1 or secim > 5:
        print("Lütfen 1-5 arasında bir sayı giriniz:")
    else:
        dosya = open("kitap_bilgileri.txt", "r")
        sayac = 1
        satir = dosya.readline() 

        while satir:  # Dosya sonuna kadar oku
            if sayac == (14 * (secim - 1)) + 1: #kullanıcı kaçıncı kitabı seçerse o kitabın ilk bilgisinin bulunduğu satırı veren işlem
                for i in range(1, 15):
                    print(satir.strip()) 
                    satir = dosya.readline()
                    sayac += 1
                break  # Gerekli bilgileri yazdıktan sonra döngüyü kır

            sayac += 1
            satir = dosya.readline() 

        dosya.close()
