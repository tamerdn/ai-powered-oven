import os
import json
import shutil
from sklearn.model_selection import train_test_split

# --- 1. JSON etiket dosyalarını yükle ---
def load_json_labels(filepath, label_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    data_dict = {entry[label_name]: entry for entry in raw_data}
    return data_dict

# Etiket dosyalarının yolları
steak_labels = load_json_labels('augmented_steak_etiketleri.json', 'steak')
pizza_labels = load_json_labels('augmented_pizza_etiketleri.json', 'pizza')
fish_labels = load_json_labels('augmented_fish_etiketleri.json', 'fish')
cookie_labels = load_json_labels('augmented_cookie_etiketleri.json', 'cookie')
bread_labels = load_json_labels('augmented_bread_etiketleri.json', 'bread')

# --- 2. Tüm veriyi listeliyoruz ---
def create_data_list(label_dict, category, folder_path):
    return [{
        "image": image_name,
        "label": category,
        "folder": folder_path,
        "json": label_dict[image_name]
    } for image_name in label_dict.keys()]

steak_data = create_data_list(steak_labels, "steak", "augmented_steak")
pizza_data = create_data_list(pizza_labels, "pizza", "augmented_pizza")
fish_data = create_data_list(fish_labels, "fish", "augmented_fish")
cookie_data = create_data_list(cookie_labels, "cookie", "augmented_cookie")
bread_data = create_data_list(bread_labels, "bread", "augmented_bread")

all_data = steak_data + pizza_data + fish_data + cookie_data + bread_data

# --- 3. Train/Val/Test oranları ---
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

train_data, temp_data = train_test_split(all_data, train_size=train_ratio, random_state=42)
val_data, test_data = train_test_split(temp_data, test_size=test_ratio / (val_ratio + test_ratio), random_state=42)

# --- 4. Klasörleri oluştur ---
output_dirs = ['train', 'validation', 'test']
for dir in output_dirs:
    os.makedirs(os.path.join(dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(dir, 'labels'), exist_ok=True)

# --- 5. Kopyalama fonksiyonu ---
def copy_files(data, set_name):
    for item in data:
        image_name = item["image"]
        src_folder = item["folder"]
        json_data = item["json"]

        # Görseli kopyala
        image_src = os.path.join(src_folder, image_name)
        image_dst = os.path.join(set_name, 'images', image_name)
        shutil.copy(image_src, image_dst)

        # Etiketi kopyala
        json_dst = os.path.join(set_name, 'labels', f"{os.path.splitext(image_name)[0]}.json")
        with open(json_dst, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

# --- 6. Verileri setlere göre kopyala ---
copy_files(train_data, 'train')
copy_files(val_data, 'validation')
copy_files(test_data, 'test')

# --- 7. Bilgilendirme ---
print(f"Veriler başarıyla bölündü ve taşındı: {len(train_data)} train, {len(val_data)} validation, {len(test_data)} test")

