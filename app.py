import json
from pathlib import Path

# Dosya yolunu 
dosya_yolu = Path(r"C:\Users\ramaz\Desktop\akademiqProje2\data.json")

# Dosyayı açıp JSON verisini yükleyin
with open(dosya_yolu, "r") as dosya:
    veri = json.load(dosya)

ders_notlari = veri.get("ders_notlari", [])

toplam_not = 0
not_sayısı = 0

# ders_notlari indekslerinde dolaş
for index, ders in enumerate(ders_notlari):
    toplam_not += ders
    not_sayısı += index


ortalama = toplam_not / not_sayısı

print(ortalama)