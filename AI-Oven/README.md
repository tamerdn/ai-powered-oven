# ai-powered-oven
# 🔥 AI-Oven: Yapay Zeka Destekli Akıllı Fırın / AI-Oven: AI-Powered Smart Oven

Bu proje, fırına yerleştirilen yemeğin **görselinden yola çıkarak** pişirme sıcaklığı ve süresini tahmin eden bir yapay zeka sistemini ve onun web arayüzünü içerir.  
>>>
This project includes an AI system and web interface that predicts the **cooking temperature and duration** from an image of food placed in an oven.

## 🚀 Projenin Amacı / Project Goal

Yemeklerin ideal sürede ve sıcaklıkta pişmesini sağlamak için **bilgisayarla görü ve derin öğrenme** kullanılmıştır.
>>>
To ensure food is cooked at the ideal time and temperature, **computer vision and deep learning** were utilized.

---
# Yapay Zekalı Fırın Asistanı (AI-Powered Oven Assistant) 🤖🔥


Mutfaktaki en büyük yardımcınız! Bu proje, pişmemiş bir yemeğin fotoğrafını analiz ederek, o yemek için en uygun pişirme sıcaklığını ve süresini yapay zeka kullanarak öneren bir web uygulamasıdır. Artık "acaba kaç derecede pişirmeliyim?" derdine son!
>>>
Your greatest assistant in the kitchen! This project is a web application that analyzes a photo of an uncooked meal and suggests the most suitable cooking temperature and time for that meal using artificial intelligence. No more "how many degrees should I cook it at?" worries!

---

## 🎯 Projenin Amacı (Purpose Of The Project)

Bu projenin temel amacı, bilgisayarlı görü ve derin öğrenme tekniklerini kullanarak mutfaktaki pişirme sürecini otomatikleştirmek ve basitleştirmektir. Kullanıcıların yemeklerini her seferinde mükemmel bir şekilde pişirmelerine yardımcı olarak tahmine dayalı pişirmeyi ortadan kaldırmayı hedefler.
>>>
The main goal of this project is to automate and simplify the cooking process in the kitchen using computer vision and deep learning techniques. It aims to eliminate guesswork in cooking by helping users cook their meals perfectly every time.

## ✨ Özellikler (Features)

* **Görüntü Yükleme:** Kullanıcı dostu web arayüzü üzerinden pişmemiş yemek fotoğrafı yükleme.
* **Yapay Zeka Destekli Tahmin:** Yüklenen fotoğrafı analiz eden derin öğrenme modeli ile:
    * Yiyeceğin türünü tanıma (örn: Balık, Pizza, Büftek).
    * Optimum **pişirme sıcaklığını** (°C) önerme.
    * Optimum **pişirme süresini** (dakika) önerme.
* **Sonuç Ekranı:** Analiz sonuçlarını net ve anlaşılır bir şekilde kullanıcıya sunma.
>>>
* **Image Upload:** Upload uncooked food photos via user-friendly web interface.
* **Artificial Intelligence Supported Prediction:** Deep learning model analyzes uploaded photo and:
    * Recognize food type (e.g. Fish, Pizza, Buffet).
    * Recommend optimum **cooking temperature** (°C).
    * Recommend optimum **cooking time** (minutes).
* **Result Screen:** Present analysis results to user in a clear and understandable manner.

## 🛠️ Kullanılan Teknolojiler (Technologies Used)

* **Backend:** Python, Flask
* **Deep Learning:** TensorFlow, Keras
* **Image Processing:** OpenCV, Pillow
* **Model Structure:** CNN + Resnet50 based multiple output regression model
* **Frontend:** HTML, CSS, JavaScript
* **Version Control:** Git, GitHub


**Eğitilmiş Modeli İndirin: (Download Trained Model:)**
Eğitilmiş model dosyası (`oven_model.keras`) büyük olduğu için repoya dahil edilmemiştir. Aşağıdaki linkten indirip projenin ana klasörüne kopyalayın.
> **[Modeli İndir](https://drive.google.com/file/d/1PBA6WnHDFD2hFkNfJOb4B98BT3l2MAPL/view?usp=sharing)**
>>>
The trained model file (`oven_model.keras`) is not included in the repo because it is large. Download it from the link below and copy it to the main folder of the project.
> **[Download Model](https://drive.google.com/file/d/1PBA6WnHDFD2hFkNfJOb4B98BT3l2MAPL/view?usp=sharing)**

Uygulama çalışmaya başladığında, terminalde yazan adresi (genellikle `http://127.0.0.1:5000`) tarayıcınıza yapıştırarak projeyi görebilirsiniz.
>>>
Once the application is running, you can see the project by pasting the address written in the terminal (usually `http://127.0.0.1:5000`) into your browser.

## 📂 Proje Yapısı (Project Structure)

```
.
├── website/                # Web arayüzü dosyaları (HTML, CSS, JS) / Web interface files (HTML, CSS, JS)
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   └── templates/
│       └── index.html
├── app.py                  # Ana Flask uygulama dosyası / Main Flask application file
├── oven_model.keras        # Eğitilmiş derin öğrenme modelini indirin / Download the trained deep learning model
├── requirements.txt        # Gerekli Python kütüphaneleri / Required Python libraries
├── .gitignore              # Git tarafından görmezden gelinecek dosyalar / Files to be ignored by Git
└── README.md               # Bu dosya / This file
```

## 📜 Lisans (Licence)

Bu proje, [MIT Lisansı](LICENSE) ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.
>>>
This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.
