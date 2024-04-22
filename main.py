import tur_sec
import personel_girisi
import linecache

dosya="kitap_bilgileri.txt"
print("Giriş yapacak kullanıcıyı seçiniz")
kullanici = int(input("1-Personel Giriş\n2-Kullanıcı Giriş\n3-Yönetici Giriş ")) #kullanıcı tipi belirleme

if kullanici == 1: # admin girişi
    sifre = input("Şifre giriniz:")
    personel_girisi.personel_girisi(sifre)
    


elif kullanici == 2: # kullanıcı girişi

    print("\nFelsefe\nBilim\nHukuk\nSağlık\nKurgu")

    kategori = input("Lütfen bir kategori seçin ").upper()

    if kategori == "FELSEFE":
        tur_sec.tur_sec(1)
    elif kategori == "BILIM":
        tur_sec.tur_sec(2)
    elif kategori == "HUKUK":
        tur_sec.tur_sec(3)
    elif kategori == "SAĞLIK":
        tur_sec.tur_sec(4)
    elif kategori == "KURGU":
        tur_sec.tur_sec(5)
    else:
        print("Geçersiz kategori girişi.")


else:
    print("Lütfen var olan işlemlerden birini seçiniz :(") 



