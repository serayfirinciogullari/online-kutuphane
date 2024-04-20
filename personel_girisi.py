def personel_girisi(sifre):
    
    dosya_sifre = open("admin_sifre.txt","r") #metin dosyasında tutulan şifreyi okuyup dosya_sifre değişkeninde tutat
    satir = dosya_sifre.readline()
    dosya_sifre.close()
    if sifre == satir:  #oturum açma
        print("Oturum açıldı ^^")
        sifre_degistirme = int(input("Şifre değiştirmek için 1, devam etmek için herhangi bir tuşa basınız:"))
        if sifre_degistirme == 1:
            yeni_sifre = input("Yeni şifreyi giriniz:")
            yeni_sifre_kontrol = input("Şifreyi tekrar gir:")

            if yeni_sifre == yeni_sifre_kontrol: #yeni şifreyi kullanıcıdan alıp şifrenin tutulduğu metin dosyasına yazma
                dosya_guncelleme = open("admin_sifre.txt","w")
                dosya_guncelleme.write(yeni_sifre)
                print("Şifre başarıyla değiştirildi")
                dosya_guncelleme.close()
            else:
                print("Lütfen tekrar deneyiniz")
        else:
            pass
    else:
        for i in range (3):
            deneme=input(f"Girdiğiniz şifre yanlış {3-i} deneme hakkınız kaldı")
            
            if deneme==satir:
                print("Oturum açıldı ^^")
        if deneme!=satir:
            print("Deneme hakkınız kalmadı, oturum sonlandırılıyor...")




        