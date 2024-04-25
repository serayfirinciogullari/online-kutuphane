import kitap_bilgisi
def kitap_guncelleme():

    kitap_bilgisi.kitap_bilgisi()
    

    while True:
        satir=int(input("Bilgisini güncellemek istediğiniz satırı giriniz: "))
                   
        if 1<=satir<=7:
            if satir==1:
                guncel_isim=input("Kitabın güncel isim bilgisini giriniz: ")
                guncel_isim=guncel_isim.upper()

                with open("kitap_bilgileri.txt", "r+",encoding="utf-8") as dosya: #dosya okunur

                    satirlar = dosya.readlines() # dosyanın bütün satırlarını okur ve satırlar dizisinde tutar

                    satirlar[satir - 1] = guncel_isim + "\n" #satır değişkenini satılar dizisindeki indexine göre yeni isim değişkenine atanır
                    dosya.seek(0) #dosyannın başına gider ve satırları okur
                    dosya.writelines(satirlar) #satırlar tekrar yazdırılır
                    dosya.truncate() #güncellenen ismi eski isme göre kırpar 

                print("Kitabın ismi başarıyla güncellendi.")

            elif satir==2:
                guncel_ISBN=input("Kitabın güncel ISBN numara bilgisini giriniz: ")
                
                with open("kitap_bilgileri.txt", "r+",encoding="utf-8") as dosya: #dosya okunur

                    satirlar = dosya.readlines() # dosyanın bütün satırlarını okur ve satırlar dizisinde tutar

                    satirlar[satir - 1] = guncel_ISBN + "\n" #satır değişkenini satılar dizisindeki indexine göre yeni isim değişkenine atanır
                    dosya.seek(0) #dosyannın başına gider ve satırları okur
                    dosya.writelines(satirlar) #satırlar tekrar yazdırılır
                    dosya.truncate() #güncellenen ismi eski isme göre kırpar 

                print("Kitabın ISBN numarası başarıyla güncellendi.")

            elif satir==3:
                guncel_yazar=input("Kitabın güncel yazar bilgisini giriniz: ")

                with open("kitap_bilgileri.txt", "r+", encoding="utf-8") as dosya: #dosya okunur

                    satirlar = dosya.readlines() # dosyanın bütün satırlarını okur ve satırlar dizisinde tutar

                    satirlar[satir - 1] = guncel_yazar+ "\n" #satır değişkenini satılar dizisindeki indexine göre yeni isim değişkenine atanır
                    dosya.seek(0) #dosyannın başına gider ve satırları okur
                    dosya.writelines(satirlar) #satırlar tekrar yazdırılır
                    dosya.truncate() #güncellenen ismi eski isme göre kırpar 

                print("Kitabın yazar ismi başarıyla güncellendi.")

            elif satir==4:
                guncel_yayinevi=input("Kitabın güncel yayınevi bilgisini giriniz: ")

                with open("kitap_bilgileri.txt", "r+",encoding="utf-8") as dosya: #dosya okunur

                    satirlar = dosya.readlines() # dosyanın bütün satırlarını okur ve satırlar dizisinde tutar

                    satirlar[satir - 1] = guncel_yayinevi + "\n" #satır değişkenini satılar dizisindeki indexine göre yeni isim değişkenine atanır
                    dosya.seek(0) #dosyannın başına gider ve satırları okur
                    dosya.writelines(satirlar) #satırlar tekrar yazdırılır
                    dosya.truncate() #güncellenen ismi eski isme göre kırpar 

                print("Kitabın yayınevi bilgisi başarıyla güncellendi.")

            elif satir==5:
                guncel_sene=input("Kitabın güncel yayımlanma sene bilgisini giriniz: ")
                with open("kitap_bilgileri.txt", "r+",encoding="utf-8") as dosya: #dosya okunur

                    satirlar = dosya.readlines() # dosyanın bütün satırlarını okur ve satırlar dizisinde tutar

                    satirlar[satir - 1] = guncel_sene + "\n" #satır değişkenini satılar dizisindeki indexine göre yeni isim değişkenine atanır
                    dosya.seek(0) #dosyannın başına gider ve satırları okur
                    dosya.writelines(satirlar) #satırlar tekrar yazdırılır
                    dosya.truncate() #güncellenen ismi eski isme göre kırpar 

                print("Kitabın yayınlanma sene bilgisi başarıyla güncellendi.")

            elif satir==6:
                guncel_adet=input("Kitabın güncel stok adedi bilgisini giriniz: ")
                with open("kitap_bilgileri.txt", "r+",encoding="utf-8") as dosya: #dosya okunur

                    satirlar = dosya.readlines() # dosyanın bütün satırlarını okur ve satırlar dizisinde tutar

                    satirlar[satir - 1] = guncel_adet + "\n" #satır değişkenini satılar dizisindeki indexine göre yeni isim değişkenine atanır
                    dosya.seek(0) #dosyannın başına gider ve satırları okur
                    dosya.writelines(satirlar) #satırlar tekrar yazdırılır
                    dosya.truncate() #güncellenen ismi eski isme göre kırpar 

                print("Kitabın stok bilgisi başarıyla güncellendi.")


            elif satir==7:
                guncel_kategori=input("Kitabın güncel kategori bilgisini giriniz: ")
                with open("kitap_bilgileri.txt", "r+",encoding="utf-8") as dosya: #dosya okunur

                    satirlar = dosya.readlines() # dosyanın bütün satırlarını okur ve satırlar dizisinde tutar

                    satirlar[satir - 1] = guncel_kategori + "\n" #satır değişkenini satılar dizisindeki indexine göre yeni isim değişkenine atanır
                    dosya.seek(0) #dosyannın başına gider ve satırları okur
                    dosya.writelines(satirlar) #satırlar tekrar yazdırılır
                    dosya.truncate() #güncellenen ismi eski isme göre kırpar 

                print("Kitabın kategori bilgisi başarıyla güncellendi.")
        else:
            break

kitap_guncelleme()
