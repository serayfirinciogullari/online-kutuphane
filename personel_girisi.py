def personel_girisi(sifre):

    
    dosya_sifre = open("admin_sifre.txt","r") #metin dosyasında tutulan şifreyi okuyup dosya_sifre değişkeninde tutat
    satir = dosya_sifre.readline()
    dosya_sifre.close()
    if sifre == satir:  #oturum açma
        print("Oturum açıldı ^^")

        print("1-Şifre değiştirme\n2-Kitap ekleme\n3-Kitap silme\n4-Kitap durumu güncelleme")

        islem = int(input("Yapmak istediğiniz işlemi giriniz:"))

        if islem == 1: #şifre değiştirme bloğu
            yeni_sifre = input("Yeni şifreyi giriniz:")
            yeni_sifre_kontrol = input("Şifreyi tekrar gir:")

            if yeni_sifre == yeni_sifre_kontrol: #yeni şifreyi kullanıcıdan alıp şifrenin tutulduğu metin dosyasına yazma
                dosya_guncelleme = open("admin_sifre.txt","w")
                dosya_guncelleme.write(yeni_sifre)
                print("Şifre başarıyla değiştirildi")
                dosya_guncelleme.close()
            else:
                while True:
                    deneme=input(f"Girilen şifreler uyuşmuyor, tekrar deneyin")
                    if deneme==satir:
                        print("Şifreniz güncellendi ^^")

        
        elif islem==2: #kitap ekleme bloğu
            isim = input("Eklemek istediğiniz kitabın ismini giriniz: ") + "\n"
            tur = input("Eklemek istediğiniz kitabın türünü giriniz: ") + "\n"
            yayinevi = input("Eklemek istediğiniz kitabın yayınevini giriniz: ") + "\n"
            yayin_yili = input("Eklemek istediğiniz kitabın yayın yılını giriniz: ") + "\n"
            isbn = input("Eklemek istediğiniz kitabın ISBN numarasını giriniz: ") + "\n"

            try:
                with open("kitap_bilgileri.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(isim)
                    dosya.write(tur)
                    dosya.write(yayinevi)
                    dosya.write(yayin_yili)
                    dosya.write(isbn)
                print("Bilgiler başarıyla eklendi")
            except:
                print("Bir hata oluştu")




        
        




    else: #yanlış şifre girişi olunca çalışacak blok
        for i in range (3):
            deneme=input(f"Girdiğiniz şifre yanlış {3-i} deneme hakkınız kaldı")
            
            if deneme==satir:
                print("Oturum açıldı ^^")
        if deneme!=satir:
            print("Deneme hakkınız kalmadı, oturum sonlandırılıyor...")




        
