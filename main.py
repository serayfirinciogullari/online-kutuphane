import tur_sec
import personel_girisi
print("\n")
print("Giriş yapacak kullanıcıyı seçiniz")
kullanici = int(input("1-Personel Giriş\n2-Kullanıcı Giriş ")) #kullanıcı tipi belirleme

if kullanici == 1: # admin girişi
    sifre = input("Şifre giriniz:")
    personel_girisi.personel_girisi(sifre)


elif kullanici == 2: # kullanıcı girişi

    print("1-Felsefe\n2-Bilim\n3-Hukuk\n4-Sağlık\n5-Kurgu")
    secim  = int(input("Hangi tür kitabın bilgilerine erişim sağlamak istiyorsunuz?"))
    print("\n")
    tur_sec.tur_sec(secim)

else:
    print("Lütfen var olan işlemlerden birini seçiniz :(") # 1 ya da 2 harici giriş yapılırsa programı sonlandırma
    
sec=int(input("Hangi kitabın bilgilerini öğrenmek istiyorsunuz?"))
if sec%3==1:
    ilk_satir = (secim - 1) * 16 + 1  
    for i in range(ilk_satir, ilk_satir + 5):
        satir = linecache.getline(dosya, i)
        print(satir.strip())

if sec%3==2:
    ilk_satir = (secim - 1) * 16 + 1+5 
    for i in range(ilk_satir, ilk_satir + 5):
        satir = linecache.getline(dosya, i)
        print(satir.strip())

if sec%3==0:
    ilk_satir = (secim - 1) * 16 + 1+10 
    for i in range(ilk_satir, ilk_satir + 5):
        satir = linecache.getline(dosya, i)
        print(satir.strip())
