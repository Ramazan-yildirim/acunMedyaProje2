import json
from pathlib import Path

# Dosya yolunu 
dosya_yolu = Path(r"C:\Users\ramaz\Desktop\akademiqProje2\data.json")

# Dosyayı açıp JSON verisini yüklendi
with open(dosya_yolu, "r") as dosya:
    veri = json.load(dosya)

ders_notlari = veri.get("ders_notlari", [])
devamsizlik_sayısı = veri.get("devamsizlik")

toplam_not = 0
not_sayısı = 0

# ders_notlari indekslerinde dolaş
for index, ders in enumerate(ders_notlari):
    toplam_not += ders
    not_sayısı += index


ortalama = toplam_not / not_sayısı

#öğrencinin kalma veya geçme durumu kontrol edildi
if 0 >= ortalama > 50 and 0 >= devamsizlik_sayısı < 10:
    print("öğrenci sınıfı geçti")
elif 0 >= devamsizlik_sayısı > 10:
    print("öğrenci devamsızlıktan kaldı")
elif 0 >= ortalama < 50:
    print("öğrenci dersten kaldı")
else:
    print("geçersiz giriş")