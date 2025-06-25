import os
import json
import shutil

# Orijinal etiketler
with open("cookie_etiketleri.json", "r", encoding="utf-8") as f:
    original_labels = json.load(f)

# Augmented görsellerin bulunduğu klasör
augmented_folder = "augmented_cookie"

# Etiketleri yazacağımız JSON dosyası
augmented_labels = []

# Her bir görseli etiketleme
for cookie in original_labels:
    cookie_name = cookie["cookie"]  # Orijinal pizza ismi (pizza1.jpg, pizza2.jpg, vb.)
    
    # Augmented görsellerin isimlerini belirleyelim
    for i in range(1, 21):  # 20 augmented görsel
        augmented_image_name = f"{cookie_name.split('.')[0]}_aug_{i}.jpg"
        
        # Augmented etiketleri oluştur
        augmented_label = {
            "cookie": augmented_image_name,
            "az_pismis": cookie["az_pismis"],
            "orta_pismis": cookie["orta_pismis"],
            "cok_pismis": cookie["cok_pismis"]
        }
        
        # Augmented etiketleri listeye ekleyelim
        augmented_labels.append(augmented_label)

# Yeni etiketleri JSON dosyasına yazalım
with open("augmented_cookie_etiketleri.json", "w", encoding="utf-8") as f:
    json.dump(augmented_labels, f, ensure_ascii=False, indent=4)

print("Augmented etiketler başarıyla kaydedildi!")


