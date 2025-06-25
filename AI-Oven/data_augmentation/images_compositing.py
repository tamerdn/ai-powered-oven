from PIL import Image
import os

# Görsellerin bulunduğu klasör
klasor_yolu = ""
foto_sayisi = 5
sutun_sayisi = 3  # 3 sütun olacak
satir_sayisi = 2   # 2 satır olacak

# Sabit boyut (hepsini buna göre ayarlayacağız)
hedef_genislik = 200
hedef_yukseklik = 200

# Fotoğrafları yükle ve boyutlandır
fotolar = []
for i in range(1, foto_sayisi + 1):
    yol = os.path.join(klasor_yolu, f"bread{i}.jpg")
    img = Image.open(yol).resize((hedef_genislik, hedef_yukseklik))
    fotolar.append(img)

# Yeni büyük görüntü boyutu (3 sütun, 2 satır)
birlesik_genislik = sutun_sayisi * hedef_genislik
birlesik_yukseklik = satir_sayisi * hedef_yukseklik
birlesik = Image.new("RGB", (birlesik_genislik, birlesik_yukseklik), color=(255, 255, 255))

# Fotoğrafları yerleştir
for index, foto in enumerate(fotolar):
    # Fotoğrafın yerleştirileceği X, Y koordinatlarını hesapla
    x = (index % sutun_sayisi) * hedef_genislik
    y = (index // sutun_sayisi) * hedef_yukseklik
    
    # Her fotoğrafı merkeze hizalayacak şekilde yerleştir
    # X ve Y koordinatlarını ortalamak için hesaplamalar
    x_offset = (birlesik_genislik - (sutun_sayisi * hedef_genislik)) // 2
    y_offset = (birlesik_yukseklik - (satir_sayisi * hedef_yukseklik)) // 2
    
    # Fotoğrafı yerleştir
    birlesik.paste(foto, (x + x_offset, y + y_offset))

# Kaydet
birlesik.save("birlesik_ekmekler_simetrik.jpg")
print("✅ Fotoğraflar başarıyla simetrik şekilde birleştirildi!")
