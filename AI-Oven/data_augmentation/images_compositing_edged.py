from PIL import Image, ImageOps
import os

# Görsellerin bulunduğu klasör
klasor_yolu = "cookie"
foto_sayisi = 20
sutun_sayisi = 5
satir_sayisi = 4

# Sabit boyut (hepsini buna göre ayarlayacağız)
hedef_genislik = 200
hedef_yukseklik = 200
kenarlik = 2  # Kenarlık kalınlığı

# Fotoğrafları yükle, boyutlandır ve kenarlık ekle
fotolar = []
for i in range(1, foto_sayisi + 1):
    yol = os.path.join(klasor_yolu, f"cookie{i}.jpg")
    img = Image.open(yol).resize((hedef_genislik, hedef_yukseklik))
    img_border = ImageOps.expand(img, border=kenarlik, fill='black')
    fotolar.append(img_border)

# Yeni büyük görüntü boyutu
birlesik_genislik = sutun_sayisi * (hedef_genislik + 2 * kenarlik)
birlesik_yukseklik = satir_sayisi * (hedef_yukseklik + 2 * kenarlik)
birlesik = Image.new("RGB", (birlesik_genislik, birlesik_yukseklik), color=(255, 255, 255))

# Fotoğrafları yerleştir
for index, foto in enumerate(fotolar):
    x = (index % sutun_sayisi) * (hedef_genislik + 2 * kenarlik)
    y = (index // sutun_sayisi) * (hedef_yukseklik + 2 * kenarlik)
    birlesik.paste(foto, (x, y))

# Kaydet
birlesik.save("birlesik_kurabiyeler_kenarli.jpg")
print("✅ Fotoğraflar başarıyla kenarlıklı şekilde birleştirildi!")
