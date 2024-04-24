from kitap_ekle import kitap_ekle
from kitap_sil import kitap_sil
from kitap_bilgisi import kitap_bilgisi
from personel_girisi import personel_girisi
from tur_sec import tur_sec
from kitap_iade_odunc import kitap_odunc_alma, kitap_iade


def main():
    while True:
        print("\nKütüphane Yönetim Paneli")
        print("1. Personel Girişi")
        print("2. Kitap Bilgilerini Göster")
        print("3. Kitap Kategorilerine Göre Listele")
        print("4. Kitap Ödünç Al")
        print("5. Kitap İade Et")
        print("0. Çıkış Yap")

        secim = int(input("Lütfen bir işlem seçiniz: "))

        if secim == 1:
            sifre = input("Şifre giriniz: ")
            if personel_girisi(sifre):
                while True:
                    print("1. Kitap Ekle")
                    print("2. Kitap Sil")
                    print("3. Geri Dön")
                    personel_secim = int(input("Seçim yapınız: "))
                    if personel_secim == 1:
                        kitap_ekle()
                    elif personel_secim == 2:
                        kitap_sil()
                    elif personel_secim == 3:
                        break
                    else:
                        print("Geçersiz seçim, lütfen tekrar deneyin.")
        elif secim == 2:
            kitap_bilgisi()
        elif secim == 3:
            kategori_numarasi = int(input("""
1. Kişisel Gelişim
2.Eğitim
3.Hukuk
4.Bilim
5.Tarih                                                                                    
                                    
Kategori numarası giriniz (1-5): """))
            tur_sec(kategori_numarasi)
        elif secim == 4:
            kitap_odunc_alma()
        elif secim == 5:
            kitap_iade()
        elif secim == 0:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == '__main__':
    main()