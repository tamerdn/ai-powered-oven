import json
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.utils import Sequence
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# --- VERİ YÜKLEYİCİ ---
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
                # Görseli yükle
                img = load_img(path, target_size=(256, 256))
                img = img_to_array(img)
                img = preprocess_input(img)
                batch_images.append(img)

                # JSON etiketi yükle
                label_path = path.replace("images", "labels").replace(".jpg", ".json")
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

# --- MODELİ OLUŞTUR ---
input_layer = Input(shape=(256, 256, 3))
base_model = ResNet50(include_top=False, weights='imagenet', input_tensor=input_layer, pooling='avg')
x = base_model.output
x = Dense(128, activation='relu')(x)
output = Dense(6)(x)  # 6 çıkış: 3 pişme seviyesi x (sıcaklık, süre)

model = Model(inputs=input_layer, outputs=output)
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.summary()

# --- VERİ SETLERİNİ YÜKLE ---
train_gen = CustomDataGenerator("train/images", "train/labels", batch_size=16)
val_gen = CustomDataGenerator("validation/images", "validation/labels", batch_size=16)

# --- EĞİT ---
history = model.fit(train_gen, validation_data=val_gen, epochs=20)

# --- MODELİ KAYDET (opsiyonel) ---
model.save("firin_modeli.h5")
model.save("firin_modeli.keras")