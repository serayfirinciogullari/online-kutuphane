
def kitap_sil(kitap_adi, dosya_adi):
    try:
        with open(dosya_adi, "r") as dosya:
            satirlar = dosya.readlines() 

        # Kitap adını içeren satırın indeksini bul
        kitap_index = -1
        for i, satir in enumerate(satirlar): #satırlar adlı demet içinde kitap isminin bulunduğu satır değişkenini döngüyle arar
            if kitap_adi in satir:  #girilien kitap adı satır değişkeninde bulunursa
                kitap_index = i  #döngü sayesinde bulunan i değişkeni indexe eşitlenir
                break

        if kitap_index != -1: #index -1e eşit değilse (i ye eşit olunca)

            del satirlar[kitap_index:kitap_index + 6] #satırlar demetindeki indexle beraber kitabın bilgilerinin yazıldığı 6 satırı siler

            
            with open(dosya_adi, "w") as dosya: #Kitap silindikten sonra dosyayı günceller
                dosya.writelines(satirlar)
            print("Kitap başarıyla silindi.")

        else: #index -1e eşit olursa kitp adı satırda yoktur
            print("Belirtilen kitap bulunamadı.")

    except FileNotFoundError:
        print("Dosya bulunamadı.")

def kitap_ekle():

    isim = input("Eklemek istediğiniz kitabın ismini giriniz: ") + "\n"
    isbn = input("Eklemek istediğiniz kitabın ISBN numarasını giriniz: ") + "\n"
    yazar=input("Eklemek istediğiniz kitabın yazarını giriniz: ") + "\n"
    yayinevi = input("Eklemek istediğiniz kitabın yayınevini giriniz: ") + "\n"
    yayin_yili = input("Eklemek istediğiniz kitabın yayın yılını giriniz: ") + "\n"
    stok_adedi=input("Eklemek istediğiniz kitabın stok adedini giriniz: ") + "\n"
    tur = input("Eklemek istediğiniz kitabın türünü giriniz: ") + "\n"

    with open("kitap_bilgileri.txt", "a+", encoding="utf-8") as dosya:
        dosya.write(isim)
        dosya.write(isbn)
        dosya.write(yazar)
        dosya.write(yayinevi)
        dosya.write(yayin_yili)
        dosya.write(stok_adedi)
        dosya.write(tur)
        print("Bilgiler başarıyla eklendi")

def kitap_guncelleme():
    kitap_kontrol = False
    while not kitap_kontrol:
        kitap_ismi = input("Bilgileri güncellenecek kitabın ismini giriniz: ").strip().upper()
        sayac = 0
        with open("kitap_bilgileri.txt", "r+") as dosya:
            while True:
                satir = dosya.readline()
                sayac += 1
                if satir.strip() == kitap_ismi:
                    print("Girdiğiniz kitap kütüphane arşivinde mevcuttur.")
                    kitap_kontrol = True
                    while True:
                        secim = int(input("""
1.Kitabın ismi
2.Kitabın ISBN numarası
3.Kitabın yazarı
4.Kitabın yayınevi
5.Kitabın yayın yılı
6.Kitabın stok adedi
7.Kitabın Türü
\nKitabın değiştirmek istediğiniz bilgisinin numarasını giriniz:"""))
                        if secim >= 1 and secim <= 7:
                            break
                        else:
                            print("Lütfen var olan işlemlerdne birini giriniz")
                    for i in range(1, 8):
                        karakter = dosya.tell()
                        dosya.truncate()
                        satir = dosya.readline()
                        sayac += 1
                        if i == secim - 1:
                            guncel_kitap_bilgisi = input("Kitabın değiştirilecek bilgisini giriniz:")
                            kitap_guncelleme = input("Kitap bilgilerini güncellemk için e/E çıkış yapmak için herhangi bir harf giriniz: ")
                            if kitap_guncelleme.lower() == "e":
                                dosya.seek(karakter)
                                dosya.write(guncel_kitap_bilgisi)
                                print("Kitap bilgileri başarıyla değiştirildi ^^")
                            else:
                                print("Çıkış yapılıyor")
                if not satir:
                    break
            if kitap_kontrol:
                break
        if not kitap_kontrol:
            print("Girdiğiniz kitap kütüphane arşivinde bulunmamaktadır. Lütfen tekrar deneyiniz.")


def personel_girisi():
    sifre = input("Şifre giriniz:")
    dosya_sifre = open("admin_sifre.txt", "r")  # Metin dosyasında tutulan şifreyi okuyup dosya_sifre değişkeninde tutat
    satir = dosya_sifre.readline()
    dosya_sifre.close()
    deneme_sayisi = 0

    while sifre != satir:
        deneme_sayisi += 1
        if deneme_sayisi == 4:
            print("Bütün deneme haklarınız doldu... Lütfen daha sonra tekrar deneyiniz")
            break
        else:
            print("Girdiğiniz şifre yanlış. Lütfen tekrar deneyiniz. Kalan deneme hakkı sayısı:",(4 - deneme_sayisi))
            sifre = input("Şifre giriniz:")


    if sifre == satir:  # Doğru şifre girilince çalışacak olan blok
        print("Oturum açıldı ^^")

        while True:
            print("1-Şifre değiştirme\n2-Kitap ekleme\n3-Kitap silme\n4-Kitap durumu güncelleme\n0-Ana menüye geri")

            islem = int(input("Yapmak istediğiniz işlemi giriniz:"))
            if islem == 1:  # Şifre değiştirme bloğu
                while True:
                    yeni_sifre = input("Yeni şifreyi giriniz:")
                    yeni_sifre_kontrol = input("Şifreyi tekrar gir:")

                    if yeni_sifre == yeni_sifre_kontrol:  # Yeni şifreyi kullanıcıdan alıp şifrenin tutulduğu metin dosyasına yazma
                        dosya_guncelleme = open("admin_sifre.txt", "w")
                        dosya_guncelleme.write(yeni_sifre)
                        print("Şifre başarıyla değiştirildi")
                        dosya_guncelleme.close()
                        break
                    else:
                        print("Girilen şifreler uyuşmuyor. Lütfen tekrar deneyiniz.")

            elif islem == 2:  # Kitap ekleme bloğu
                kitap_ekle()

            elif islem == 3:  # Kitap silme bloğu
                silinen_kitap = input("Hangi kitabı silmek istiyorsunuz? ")
                kitap_sil(silinen_kitap, "kitap_bilgileri.txt")
        
            elif islem == 4:
                kitap_guncelleme()
            elif islem == 0:
                break
            else:
                print("lütfen geçerli bir işlem giriniz:")