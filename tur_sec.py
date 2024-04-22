"""import linecache #dosya satırlarını okumak için eklenen modül

def tur_sec(secim):
    if secim < 1 or secim > 5:
        print("Lütfen 1-5 arasında bir sayı giriniz:")
    else:
        try:
            dosya = "kitap_bilgileri.txt"
            ilk_satir = (secim - 1) * 16 + 1
            iki_satir=ilk_satir+5
            uc_satir=iki_satir+5

            satir1 = linecache.getline(dosya, ilk_satir) #dosyanın  satırının okunacağını belirtir
            satir2 = linecache.getline(dosya,iki_satir )
            satir3 = linecache.getline(dosya, uc_satir)

            print("\n")
            print(satir1.strip()) #okunan satırları yazdırır
            print(satir2.strip()) #okunan satırları yazdırır
            print(satir3.strip()) #okunan satırları yazdırır

        except FileNotFoundError:
            print("Dosya bulunamadı.")



import linecache

def tur_sec(secim):
    if secim < 1 or secim > 5:
        print("Lütfen 1-5 arasında bir sayı giriniz:")
    else:
        try:
            dosya = "kitap_bilgileri.txt"
            ilk_satir = (secim - 1) * 14 + 2
            iki_satir = ilk_satir + 5
            uc_satir = iki_satir + 10

            satir1 = linecache.getline(dosya, ilk_satir).strip()
            satir2 = linecache.getline(dosya, iki_satir).strip()
            satir3 = linecache.getline(dosya, uc_satir).strip()

            print("\n")
            print(satir1.split(" . ")[1])  # Kitap ismi kısmını al
            print(satir2.split(" . ")[1])  # Kitap ismi kısmını al
            print(satir3.split(" . ")[1])  # Kitap ismi kısmını al


        except FileNotFoundError:
            print("Dosya bulunamadı.")
"""

import linecache

def tur_sec(secim):
    if secim < 1 or secim > 5:
        print("Lütfen 1-5 arasında bir sayı giriniz:")
    else:
        try:
            dosya_adi = "kitap_bilgileri.txt"
            with open(dosya_adi, "r") as dosya:
                ilk_satir = (secim - 1) * 12 + 2
                ikinci_satir = ilk_satir + 4
                uc_satir = ikinci_satir + 4

                satir1 = linecache.getline(dosya, ilk_satir).strip()
                satir2 = linecache.getline(dosya, ikinci_satir).strip()
                satir3 = linecache.getline(dosya, uc_satir).strip()

                print(satir1)
                print(satir2)
                print(satir3)

        except FileNotFoundError:
            print("Dosya bulunamadı.")

kategori = input("Lütfen bir kategori seçin ").upper()

if kategori == "FELSEFE":
    tur_sec(1)
elif kategori == "BILIM":
    tur_sec(2)
elif kategori == "HUKUK":
    tur_sec(3)
elif kategori == "SAĞLIK":
    tur_sec(4)
elif kategori == "KURGU":
    tur_sec(5)
else:
    print("Geçersiz kategori girişi.")
