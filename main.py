import personel_girisi
from kitap_bilgisi import kitap_bilgisi
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

        secim = int(input("Lütfen bir işlem seçiniz:"))

        if secim == 1:
           personel_girisi.personel_girisi()
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