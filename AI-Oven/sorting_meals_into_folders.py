import os
import shutil

# Kaynak klasör yolu
source_folder = "labels"  # Kendi dizinine göre düzenle

# Klasördeki tüm dosyaları kontrol et
for filename in os.listdir(source_folder):
    if filename.endswith(".json"):
        # Örneğin: bread8_aug_6.jpg -> önce '_' ile ayır: ['bread8', 'aug', '6.jpg']
        # Sonra sayı karakterlerini temizle: 'bread8' -> 'bread'
        first_part = filename.split('_')[0]
        food_type = ''.join([c for c in first_part if not c.isdigit()])

        # Hedef klasör yolu (örneğin images/bread)
        target_folder = os.path.join(source_folder, food_type)

        # Eğer aynı isimde bir dosya varsa klasör oluşturulamaz, o yüzden dosya değilse kontrol et
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Dosya yolları
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(target_folder, filename)

        # Dosyayı hedef klasöre taşı
        shutil.move(src_path, dst_path)

print("Tüm dosyalar başarıyla yemek türlerine göre klasörlere taşındı.")
