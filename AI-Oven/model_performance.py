import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, median_absolute_error, explained_variance_score
import os
import json
import numpy as np
from tensorflow.keras.utils import Sequence
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input

class CustomDataGenerator(Sequence):
    def __init__(self, image_dir, label_dir, batch_size=32, shuffle=True):
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.image_paths = self._get_image_paths()
        self.on_epoch_end()

    def _get_image_paths(self):
        all_paths = []
        for root, _, files in os.walk(self.image_dir):
            for f in files:
                if f.endswith(".jpg") or f.endswith(".png"):
                    all_paths.append(os.path.join(root, f))
        return all_paths

    def __len__(self):
        return int(np.ceil(len(self.image_paths) / self.batch_size))

    def on_epoch_end(self):
        if self.shuffle:
            np.random.shuffle(self.image_paths)

    def __getitem__(self, idx):
        batch_paths = self.image_paths[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_images, batch_labels = [], []

        for path in batch_paths:
            try:
                img = load_img(path, target_size=(256, 256))
                img = img_to_array(img)
                img = preprocess_input(img)
                batch_images.append(img)

                label_path = path.replace("images", "labels").replace(".jpg", ".json").replace(".png", ".json")
                with open(label_path, 'r') as f:
                    label_json = json.load(f)

                label_vector = [
                    label_json["az_pismis"]["sicaklik"],
                    label_json["az_pismis"]["sure"],
                    label_json["orta_pismis"]["sicaklik"],
                    label_json["orta_pismis"]["sure"],
                    label_json["cok_pismis"]["sicaklik"],
                    label_json["cok_pismis"]["sure"]
                ]
                batch_labels.append(label_vector)

            except Exception as e:
                print(f"Hata oluştu: {e} - {path}")
                continue

        return np.array(batch_images), np.array(batch_labels)



# Test verisini yükle
test_gen = CustomDataGenerator("test/images", "test/labels", batch_size=16, shuffle=False)

# Modeli yükle (eğer eğitim sonrası tekrar çalışıyorsan)
from tensorflow.keras.models import load_model
model = load_model("firin_modeli.keras")

# Tüm test verisi için tahmin al
y_true_all = []
y_pred_all = []

for X_batch, y_batch in test_gen:
    y_pred_batch = model.predict(X_batch)
    y_true_all.append(y_batch)
    y_pred_all.append(y_pred_batch)

# Tüm değerleri birleştir
y_true_all = np.vstack(y_true_all)
y_pred_all = np.vstack(y_pred_all)

# --- METRİKLERİN HESAPLANMASI ---
print("Model Performans Metrikleri")
# 1. Mean Absolute Error (MAE)
mae = mean_absolute_error(y_true_all, y_pred_all)
print(f"✅ MAE (Ortalama Mutlak Hata): {mae:.2f}")
print("→ Tahminlerin gerçek değere ortalama uzaklığı. Küçük olması iyidir.\n")

# 2. Mean Squared Error (MSE)
mse = mean_squared_error(y_true_all, y_pred_all)
print(f"✅ MSE (Ortalama Kare Hata): {mse:.2f}")
print("→ Hataların karesi alınarak ortalaması. Büyük hataları daha çok cezalandırır.\n")

# 3. Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"✅ RMSE (Karekök Ortalama Kare Hata): {rmse:.2f}")
print("→ MSE'nin daha anlaşılır hali (aynı birimde). Küçük olması iyidir.\n")

# 4. R² Skoru (Determinasyon Katsayısı)
r2 = r2_score(y_true_all, y_pred_all)
print(f"✅ R² Skoru: {r2:.4f}")
print("→ 1'e ne kadar yakınsa o kadar iyi. 1: mükemmel, 0: kötü, <0: çok kötü.\n")

# 5. Mean Absolute Percentage Error (MAPE)
# Sıfır bölmeyi önlemek için küçük değerlerde klip uyguluyoruz
y_true_safe = np.where(y_true_all == 0, 1e-6, y_true_all)
mape = np.mean(np.abs((y_true_all - y_pred_all) / y_true_safe)) * 100
print(f"✅ MAPE (Ortalama Yüzde Hata): {mape:.2f}%")
print("→ Tahminlerin yüzde olarak ortalama hatası. Düşükse model iyidir.\n")

# 6. Median Absolute Error (MedAE)
medae = median_absolute_error(y_true_all, y_pred_all)
print(f"✅ MedAE (Ortanca Mutlak Hata): {medae:.2f}")
print("→ Ayıksız ortalama. Aykırı değerlerden etkilenmez.\n")

# 7. Explained Variance Score
evs = explained_variance_score(y_true_all, y_pred_all)
print(f"✅ Açıklanan Varyans Skoru: {evs:.4f}")
print("→ Tahminlerin varyansı ne kadar açıkladığı. 1'e yakınsa iyi.\n")


"""
Model Performans Metrikleri

✅ MAE (Ortalama Mutlak Hata): 4.30
→ Tahminlerin gerçek değere ortalama uzaklığı. Küçük olması iyidir.

✅ MSE (Ortalama Kare Hata): 37.95
→ Hataların karesi alınarak ortalaması. Büyük hataları daha çok cezalandırır.

✅ RMSE (Karekök Ortalama Kare Hata): 6.16
→ MSE'nin daha anlaşılır hali (aynı birimde). Küçük olması iyidir.
→ MSE'nin daha anlaşılır hali (aynı birimde). Küçük olması iyidir.

✅ R² Skoru: 0.9368
→ 1'e ne kadar yakınsa o kadar iyi. 1: mükemmel, 0: kötü, <0: çok kötü.

✅ MAPE (Ortalama Yüzde Hata): 9.04%
→ Tahminlerin yüzde olarak ortalama hatası. Düşükse model iyidir.

✅ MedAE (Ortanca Mutlak Hata): 3.37
→ Ayıksız ortalama. Aykırı değerlerden etkilenmez.

✅ Açıklanan Varyans Skoru: 0.9445
→ Tahminlerin varyansı ne kadar açıkladığı. 1'e yakınsa iyi.

"""














