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