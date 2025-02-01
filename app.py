import json
from pathlib import Path

# Dosya yolunu 
dosya_yolu = Path(r"C:\Users\ramaz\Desktop\akademiqProje2\data.json")

# Dosyayı açıp JSON verisini yüklendi
with open(dosya_yolu, "r") as dosya:
    veri = json.load(dosya)

#birden fazla öğrenci için çıktı elde edildi
for ogrenci in veri:
        ders_notlari = ogrenci.get("ders_notlari", [])
        devamsizlik_sayisi = ogrenci.get("devamsizlik")
        ogrenci_ad = ogrenci.get("ad", "Bilinmiyor")
        ogrenci_soyad = ogrenci.get("soyad", "Bilinmiyor")

        toplam_not = 0
        not_sayisi = 0

        # ders_notlari indekslerinde dolaş
        for index, ders in enumerate(ders_notlari):
                #ders notlarının sıfırdan küçük olma durumu kontrol edildi
                if ders < 0:
                        print("geçersiz not girişi")
                        exit()
                toplam_not += ders
                not_sayisi += index


        ortalama = toplam_not / not_sayisi

        #devamsızlık durumunun sıfırdan küçük olma durumu kontrol edildi
        if devamsizlik_sayisi < 0:
                print("geçersiz devamsızlık girişi")
                continue 

        #öğrencinin kalma veya geçme durumu kontrol edildi
        if ortalama > 50 and devamsizlik_sayisi < 10:
                print(f"{ogrenci_ad} {ogrenci_soyad} sınıfı geçti")
        elif devamsizlik_sayisi > 10:
                print(f"{ogrenci_ad} {ogrenci_soyad} devamsızlıktan kaldı")
        elif  ortalama < 50:
                print(f"{ogrenci_ad} {ogrenci_soyad} dersten kaldı")

        print("-" * 40)  # Ayrım çizgisi ekleyerek çıktıyı düzenleyelim