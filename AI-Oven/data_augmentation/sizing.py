from PIL import Image
import os

# Görsel klasörünüzün yolu
input_folder = 'augmented_cookie/'
output_folder = 'output_cookie/'

# Çıktı klasörü yoksa oluştur
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Klasördeki tüm görselleri al
for filename in os.listdir(input_folder):
    # Sadece görsel dosyalarını işleyelim
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Görseli aç
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Görseli yeniden boyutlandır
        img_resized = img.resize((256, 256))
        
        # Yeni görseli kaydet
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

        print(f"{filename} başarıyla dönüştürüldü!")
