import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

class FirinArayuz:
    def __init__(self, root):
        self.root = root
        self.root.title("Yapay Zekalı Fırın Asistanı")
        self.root.geometry("800x600")
        
        # Model yükleme
        self.model = load_model("firin_modeli.keras")
        
        # Ana frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Fotoğraf yükleme butonu
        self.yukle_buton = ttk.Button(self.main_frame, text="Fotoğraf Yükle", command=self.fotograf_yukle)
        self.yukle_buton.grid(row=0, column=0, pady=10)
        
        # Görüntü önizleme alanı
        self.onizleme_label = ttk.Label(self.main_frame)
        self.onizleme_label.grid(row=1, column=0, pady=10)
        
        # Sonuçlar için frame
        self.sonuc_frame = ttk.LabelFrame(self.main_frame, text="Pişirme Önerileri", padding="10")
        self.sonuc_frame.grid(row=2, column=0, pady=10, sticky=(tk.W, tk.E))
        
        # Sonuç etiketleri
        self.sonuc_labels = {}
        pisirme_seviyeleri = ["Az Pişmiş", "Orta Pişmiş", "Çok Pişmiş"]
        for i, seviye in enumerate(pisirme_seviyeleri):
            ttk.Label(self.sonuc_frame, text=f"{seviye}:").grid(row=i*2, column=0, sticky=tk.W, pady=5)
            self.sonuc_labels[seviye] = {
                "sicaklik": ttk.Label(self.sonuc_frame, text=""),
                "sure": ttk.Label(self.sonuc_frame, text="")
            }
            self.sonuc_labels[seviye]["sicaklik"].grid(row=i*2, column=1, padx=20)
            self.sonuc_labels[seviye]["sure"].grid(row=i*2, column=2, padx=20)
        
        # Stil ayarları
        self.root.configure(bg='#f0f0f0')
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12))
        style.configure('TLabel', font=('Arial', 11))
        style.configure('TLabelframe.Label', font=('Arial', 12, 'bold'))
        
    def fotograf_yukle(self):
        # Dosya seçme dialogu
        dosya_yolu = filedialog.askopenfilename(
            filetypes=[("Resim Dosyaları", "*.jpg *.jpeg *.png")]
        )
        
        if dosya_yolu:
            # Görüntüyü yükle ve önizle
            self.goruntu_goster(dosya_yolu)
            
            # Tahmin yap
            sonuclar = self.tahmin_yap(dosya_yolu)
            
            # Sonuçları göster
            self.sonuclari_goster(sonuclar)
    
    def goruntu_goster(self, dosya_yolu):
        # Görüntüyü yükle ve boyutlandır
        img = Image.open(dosya_yolu)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        # Önizleme alanını güncelle
        self.onizleme_label.configure(image=photo)
        self.onizleme_label.image = photo
    
    def tahmin_yap(self, fotograf_yolu):
        # Fotoğrafı yükle ve ön işle
        img = load_img(fotograf_yolu, target_size=(256, 256))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        
        # Tahmin yap
        tahminler = self.model.predict(img_array)[0]
        
        # Sonuçları düzenle
        return {
            "Az Pişmiş": {
                "Sıcaklık": round(tahminler[0], 1),
                "Süre": round(tahminler[1], 1)
            },
            "Orta Pişmiş": {
                "Sıcaklık": round(tahminler[2], 1),
                "Süre": round(tahminler[3], 1)
            },
            "Çok Pişmiş": {
                "Sıcaklık": round(tahminler[4], 1),
                "Süre": round(tahminler[5], 1)
            }
        }
    
    def sonuclari_goster(self, sonuclar):
        for seviye, degerler in sonuclar.items():
            self.sonuc_labels[seviye]["sicaklik"].configure(
                text=f"Sıcaklık: {degerler['Sıcaklık']}°C"
            )
            self.sonuc_labels[seviye]["sure"].configure(
                text=f"Süre: {degerler['Süre']} dakika"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = FirinArayuz(root)
    root.mainloop() 