from PIL import Image
import os
import numpy as np
from imgaug import augmenters as iaa
import imageio

# Augmentasyon uygulanacak klasör yolu
input_folder = "cookie"
output_folder = "augmented_cookie"

# Çıkış klasörünü oluştur
os.makedirs(output_folder, exist_ok=True)

# Augmentations listesi
augmentations = iaa.Sequential([
    iaa.Fliplr(0.5),
    iaa.Affine(rotate=(-20, 20), scale=(0.9, 1.1)),
    iaa.Multiply((0.8, 1.2)),
    iaa.GaussianBlur(sigma=(0.0, 1.2)),
    iaa.AdditiveGaussianNoise(scale=(5, 15)),
    iaa.LinearContrast((0.7, 1.3)),
    iaa.Sharpen(alpha=(0, 0.5), lightness=(0.75, 1.25)),
])

# Her görsel için 20 augmentasyon üret
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(input_folder, filename)
        image = imageio.v2.imread(image_path)
        images = [image] * 20  # aynı görselden 20 kopya

        # Augmentasyonları uygula
        augmented_images = augmentations(images=images)

        base_name = os.path.splitext(filename)[0]
        for i, aug_img in enumerate(augmented_images):
            out_path = os.path.join(output_folder, f"{base_name}_aug_{i+1}.jpg")
            imageio.imwrite(out_path, aug_img)

output_folder  # Augment edilmiş görsellerin klasörü döndürülüyor.


