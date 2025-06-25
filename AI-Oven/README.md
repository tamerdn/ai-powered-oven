
# 🔥 AI-Oven: Yapay Zeka Destekli Akıllı Fırın / AI-Oven: AI-Powered Smart Oven

Bu proje, fırına yerleştirilen yemeğin **görselinden yola çıkarak** pişirme sıcaklığı ve süresini tahmin eden bir yapay zeka sistemini ve onun web arayüzünü içerir.  
This project includes an AI system and web interface that predicts the **cooking temperature and duration** from an image of food placed in an oven.

## 🚀 Projenin Amacı / Project Goal

Yemeklerin ideal sürede ve sıcaklıkta pişmesini sağlamak için **bilgisayarla görü ve derin öğrenme** kullanılmıştır.  
To ensure food is cooked at the ideal time and temperature, **computer vision and deep learning** were utilized.

---

## 🧠 Yapay Zeka Özellikleri / AI Features

- Derin öğrenme kullanarak **et görüntüsünden**:  
  - Sıcaklık tahmini (°C)  
  - Pişme seviyesi tahmini (az pişmiş, orta, iyi pişmiş)

- Using deep learning on **meat images**:  
  - Temperature prediction (°C)  
  - Doneness level prediction (rare, medium, well-done)

---

## 🌐 Web Arayüzü / Web Interface

- Görsel yükleme  
- Yapay zeka tahmin sonuçlarını gösterme  
- Duyarlı ve kullanıcı dostu arayüz  

- Image upload  
- Displaying AI prediction results  
- Responsive and user-friendly interface

---

## 🗂️ Klasör Yapısı / Folder Structure

```
ai-oven/
│
├── website/              # Web arayüzü / Web interface
│   └── index.html, style.css, app.js
│
├── ai_model/             # Eğitim ve model dosyaları / Training and model files
│   ├── train.py
│   ├── model.py
│   ├── predict.py
│   └── model.pt
│
├── data/                 # Örnek veriler / Sample data
│   └── sample_images/, annotations.json
│
├── requirements.txt      # Gereken kütüphaneler / Required packages
├── .gitignore
└── README.md
```

---

## ⚙️ Kurulum / Installation

```bash
git clone https://github.com/kullaniciadi/ai-oven.git
cd ai-oven/ai_model
pip install -r requirements.txt
```

---

## ▶️ Kullanım / Usage

1. `predict.py` dosyasını çalıştırarak modeli kullanabilirsiniz.  
2. `website/index.html` dosyasını tarayıcıda açarak görsel yükleyebilirsiniz.

1. Run `predict.py` to use the model.  
2. Open `website/index.html` in your browser to upload an image.

---

## 🧪 Model Performansı / Model Performance

- Eğitim Doğruluğu / Training Accuracy: %XX  
- Test Hatası / Test Error: XX MSE  
- Kullanılan metrikler / Used metrics: MSE, Accuracy

---

## 📁 Veri Seti / Dataset

Veri seti telif nedeniyle paylaşılmamaktadır. Ancak örnek görseller `data/` klasöründe mevcuttur.  
The dataset is not shared due to copyright. However, sample images are available in the `data/` folder.

---

## 📌 Notlar / Notes

- Bu proje **TÜBİTAK 2209-A** başvurusu için hazırlanmıştır.  
- Eğitim amaçlıdır. Gerçek cihazlarda kullanmadan önce test edilmelidir.

- This project was prepared for the **TÜBİTAK 2209-A** research grant.  
- It is for educational purposes. Must be tested before using in real ovens.
