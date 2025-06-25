import json

# JSON dosyasını oku
with open("pizza_pisirme_profilleri.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Pizza adlarını güncelle
for i, profile in enumerate(data):
    profile["pizza"] = f"pizza{i+1}.jpg"

# Yeni dosyayı kaydet
with open("pizza_pisirme_profilleri_dosya_adli.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
