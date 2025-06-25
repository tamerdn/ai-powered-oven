from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
import time

# Global model değişkeni
_model = None

def get_model():
    global _model
    if _model is None:
        try:
            _model = load_model(os.path.join(os.path.dirname(os.path.dirname(__file__)), "firin_modeli.keras"))
        except Exception as e:
            print(f"Model yüklenirken hata oluştu: {str(e)}")
            return None
    return _model

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit

# Uploads klasörünü oluştur
os.makedirs('uploads', exist_ok=True)

# İzin verilen dosya uzantıları
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_float(x):
    return float(x)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/tahmin', methods=['POST'])
def tahmin():
    model = get_model()
    if model is None:
        return jsonify({'error': 'Model yüklenemedi. Lütfen sistem yöneticisiyle iletişime geçin.'}), 500

    if 'imageUpload' not in request.files:
        return jsonify({'error': 'Dosya yüklenmedi'}), 400
    
    file = request.files['imageUpload']
    if file.filename == '':
        return jsonify({'error': 'Dosya seçilmedi'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Geçersiz dosya formatı. Lütfen PNG, JPG veya JPEG formatında bir resim yükleyin.'}), 400
    
    if file:
        try:
            # Dosyayı kaydet
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Görüntüyü yükle ve ön işle
            img = load_img(filepath, target_size=(256, 256))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            
            # Tahmin yap
            tahminler = model.predict(img_array, verbose=0)[0]
            
            # Sonuçları düzenle ve float32'yi float'a dönüştür
            sonuclar = {
                "az_pismis": {
                    "sicaklik": convert_to_float(round(tahminler[0], 1)),
                    "sure": convert_to_float(round(tahminler[1], 1))
                },
                "orta_pismis": {
                    "sicaklik": convert_to_float(round(tahminler[2], 1)),
                    "sure": convert_to_float(round(tahminler[3], 1))
                },
                "cok_pismis": {
                    "sicaklik": convert_to_float(round(tahminler[4], 1)),
                    "sure": convert_to_float(round(tahminler[5], 1))
                },
                "image_url": f"/uploads/{filename}"
            }
            
            return jsonify(sonuclar)
            
        except Exception as e:
            print(f"Hata oluştu: {str(e)}")
            return jsonify({'error': f'Tahmin yapılırken bir hata oluştu: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True) 