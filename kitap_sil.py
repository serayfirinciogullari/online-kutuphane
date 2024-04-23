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
