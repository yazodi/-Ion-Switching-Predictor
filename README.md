---
title: Ion Switching Predictor
emoji: ⚡
colorFrom: gray
colorTo: blue
sdk: streamlit
sdk_version: "1.32.2"
app_file: app.py
pinned: false
---

# ⚡ Ion Switching - Sinyal Tabanlı Kanal Tahmini

Bu proje, Liverpool Üniversitesi tarafından sunulan zaman serisi tabanlı Kaggle yarışmasına dayanmaktadır.  
Amaç, sinyal verilerine dayanarak açık kanal sayısını (`open_channels`) tahmin etmektir.

## 📦 Kullanılan Veri Seti

- Yarışma: [University of Liverpool - Ion Switching](https://www.kaggle.com/competitions/liverpool-ion-switching)
- Girdi Özellikleri:
  - `time`: Zaman damgası
  - `signal`: Sinyal değeri
- Hedef:
  - `open_channels`: 0–10 arasında değişen kanal sınıfları

## 🧠 Kullanılan Yöntemler

- Rolling window tabanlı özellik mühendisliği:
  - Ortalama, standart sapma, min, max (pencere: 10, 50, 100)
- Makine öğrenmesi modeli:
  - `LightGBMClassifier`
- Model değerlendirme:
  - Accuracy: **%98**
  - Macro F1-score: **0.94**
  - Weighted F1-score: **0.99**

## 🚀 Streamlit Uygulaması

Kullanıcıdan yüklenen CSV dosyasındaki `signal` verilerine göre `open_channels` tahmini yapılır.  
Model, `.pkl` formatında yüklenir. Sonuçlar indirilebilir.

## 🧪 Örnek Kullanım

1. `signal` sütunu içeren CSV dosyanızı yükleyin
2. Model, rolling özellikleri ekleyerek tahmin yapar
3. `predicted_open_channels` sütunu ile sonuçları görebilir, indirilebilir CSV alabilirsiniz

## 🧰 Gereksinimler

```bash
pip install -r requirements.txt
```

## 🧾 Dosya Yapısı

```
📁 ion-switching-app/
├── app.py
├── ion_switch_model.pkl
├── requirements.txt
└── README.md
```

## 🤗 Model Paylaşımı

> Hugging Face Spaces + GitHub üzerinden dağıtılmıştır.  
> Model dosyası (`.pkl`) Hugging Face Model Hub'a yüklenebilir veya örnek JSON + açıklama ile paylaşılabilir.

## 📌 Geliştirilebilir Özellikler

- LSTM/CNN ile zaman serisi derin öğrenme modeli
- Kapsamlı rolling feature grid search
- Sinyal segmentasyonu ile daha hassas blok modelleri

## 📄 Lisans

MIT License
