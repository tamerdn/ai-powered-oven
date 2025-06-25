import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input

def tahmin_yap(fotograf_yolu):
    # Modeli yükle
    model = load_model("firin_modeli.keras")
    
    # Fotoğrafı yükle ve ön işle
    img = load_img(fotograf_yolu, target_size=(256, 256))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Tahmin yap
    tahminler = model.predict(img_array)[0]
    
    # Sonuçları düzenle
    sonuclar = {
        "Az Pişmiş": {
            "Sıcaklık": round(tahminler[0], 1),
            "Süre (dakika)": round(tahminler[1], 1)
        },
        "Orta Pişmiş": {
            "Sıcaklık": round(tahminler[2], 1),
            "Süre (dakika)": round(tahminler[3], 1)
        },
        "Çok Pişmiş": {
            "Sıcaklık": round(tahminler[4], 1),
            "Süre (dakika)": round(tahminler[5], 1)
        }
    }
    
    return sonuclar

if __name__ == "__main__":
    # Kullanıcıdan fotoğraf yolunu al
    fotograf_yolu = input("Lütfen tahmin yapılacak fotoğrafın yolunu girin: ")
    
    try:
        # Tahminleri al
        sonuclar = tahmin_yap(fotograf_yolu)
        
        # Sonuçları göster
        print("\n=== Pişirme Önerileri ===")
        for pisirme_seviyesi, degerler in sonuclar.items():
            print(f"\n{pisirme_seviyesi}:")
            print(f"  Sıcaklık: {degerler['Sıcaklık']}°C")
            print(f"  Süre: {degerler['Süre (dakika)']} dakika")
            
    except Exception as e:
        print(f"Hata oluştu: {e}") 