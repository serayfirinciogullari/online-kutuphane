import kitap_sil

def personel_girisi(sifre):
    dosya_sifre = open("admin_sifre.txt", "r")  # Metin dosyasında tutulan şifreyi okuyup dosya_sifre değişkeninde tutat
    satir = dosya_sifre.readline()
    dosya_sifre.close()

    if sifre == satir:  # Doğru şifre girilince çalışacak olan blok
        print("Oturum açıldı ^^")

        print("1-Şifre değiştirme\n2-Kitap ekleme\n3-Kitap silme\n4-Kitap durumu güncelleme")

        islem = int(input("Yapmak istediğiniz işlemi giriniz:"))

        if islem == 1:  # Şifre değiştirme bloğu
            yeni_sifre = input("Yeni şifreyi giriniz:")
            yeni_sifre_kontrol = input("Şifreyi tekrar gir:")

            if yeni_sifre == yeni_sifre_kontrol:  # Yeni şifreyi kullanıcıdan alıp şifrenin tutulduğu metin dosyasına yazma
                dosya_guncelleme = open("admin_sifre.txt", "w")
                dosya_guncelleme.write(yeni_sifre)
                print("Şifre başarıyla değiştirildi")
                dosya_guncelleme.close()
            else:
                while True:
                    deneme = input(f"Girilen şifreler uyuşmuyor, tekrar deneyin")
                    if deneme == yeni_sifre:
                        print("Şifreniz güncellendi ^^")
                        break

        elif islem == 2:  # Kitap ekleme bloğu
            isim = input("Eklemek istediğiniz kitabın ismini giriniz: ") + "\n"
            tur = input("Eklemek istediğiniz kitabın türünü giriniz: ") + "\n"
            yayinevi = input("Eklemek istediğiniz kitabın yayınevini giriniz: ") + "\n"
            yayin_yili = input("Eklemek istediğiniz kitabın yayın yılını giriniz: ") + "\n"
            isbn = input("Eklemek istediğiniz kitabın ISBN numarasını giriniz: ") + "\n"

            with open("kitap_bilgileri.txt", "a+", encoding="utf-8") as dosya:
                dosya.write(isim)
                dosya.write(tur)
                dosya.write(yayinevi)
                dosya.write(yayin_yili)
                dosya.write(isbn)
                print("Bilgiler başarıyla eklendi")

        elif islem == 3:  # Kitap silme bloğu
            silinen_kitap = input("Hangi kitabı silmek istiyorsunuz? ")
            kitap_sil.kitap_sil(silinen_kitap, "kitap_bilgileri.txt")

    else:  # Yanlış şifre girişi olunca çalışacak blok
        deneme_sayisi = 3
        while deneme_sayisi > 0:
            deneme = input(f"Girdiğiniz şifre yanlış {deneme_sayisi} deneme hakkınız kaldı: ")

            if deneme == satir:
                print("Oturum açıldı ^^")
                print("1-Şifre değiştirme\n2-Kitap ekleme\n3-Kitap silme\n4-Kitap durumu güncelleme")
                islem = int(input("Yapmak istediğiniz işlemi giriniz: "))

                if islem == 1:  # Şifre değiştirme bloğu
                    yeni_sifre = input("Yeni şifreyi giriniz: ")
                    yeni_sifre_kontrol = input("Şifreyi tekrar gir: ")

                    if yeni_sifre == yeni_sifre_kontrol:  # Yeni şifreyi kullanıcıdan alıp şifrenin tutulduğu metin dosyasına yazma
                        dosya_guncelleme = open("admin_sifre.txt", "w")
                        dosya_guncelleme.write(yeni_sifre)
                        print("Şifre başarıyla değiştirildi")
                        dosya_guncelleme.close()
                    else:
                        while True:
                            deneme = input(f"Girilen şifreler uyuşmuyor, tekrar deneyin")
                            if deneme == yeni_sifre:
                                print("Şifreniz güncellendi ^^")
                                break
                elif islem == 2:  # Kitap ekleme bloğu
                    isim = input("Eklemek istediğiniz kitabın ismini giriniz: ") + "\n"
                    tur = input("Eklemek istediğiniz kitabın türünü giriniz: ") + "\n"
                    yayinevi = input("Eklemek istediğiniz kitabın yayınevini giriniz: ") + "\n"
                    yayin_yili = input("Eklemek istediğiniz kitabın yayın yılını giriniz: ") + "\n"
                    isbn = input("Eklemek istediğiniz kitabın ISBN numarasını giriniz: ") + "\n"

                    with open("kitap_bilgileri.txt", "a+", encoding="utf-8") as dosya:
                        dosya.write(isim)
                        dosya.write(tur)
                        dosya.write(yayinevi)
                        dosya.write(yayin_yili)
                        dosya.write(isbn)
                        print("Bilgiler başarıyla eklendi")

                elif islem == 3:  # Kitap silme bloğu
                    silinen_kitap = input("Hangi kitabı silmek istiyorsunuz? ")
                    kitap_sil.kitap_sil(silinen_kitap, "kitap_bilgileri.txt")

            else:  # Şifreler uyuşmuyorsa
                deneme_sayisi -= 1  # Her yanlış girişte deneme sayısını azalt

        if deneme_sayisi == 0:  # Deneme hakkı tükendiyse
            print("Üç deneme hakkınızı kullandınız. Oturum açılamadı :(")
