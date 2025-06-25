from PIL import Image
import os
# Görselinizin yolu
input_image_path = 'pic01.jpg'
output_folder = 'output_pic'

# Çıktı klasörü yoksa oluştur
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Görseli aç
img = Image.open(input_image_path)

# Görseli yeniden boyutlandır
img_resized = img.resize((450, 500))

# Yeni görseli kaydet
output_image_path = os.path.join(output_folder, 'resized_beyazfırın2.jpg')
img_resized.save(output_image_path)

print("Görsel başarıyla dönüştürüdü!")  
