import linecache
 
def kitap_bilgisi(kitap_numarasi):
    try:
        dosya = "kitap_bilgileri.txt"
        ilk_satir = (kitap_numarasi - 1) * 5 + 1
        son_satir = ilk_satir + 4

        for satir_numarasi in range(ilk_satir, son_satir + 1):
            satir = linecache.getline(dosya, satir_numarasi)
            print(satir.strip())  # Okunan satırları yazdır

    except FileNotFoundError:
        print("Dosya bulunamadı.")

