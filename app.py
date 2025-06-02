import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Başlık
st.title("🔌 Ion Switching Tahmin Uygulaması")

# Modeli yükle
model = joblib.load("ion_switch_model.pkl")

# Rolling feature fonksiyonu
def add_rolling_features(df, window_sizes=[10, 50, 100]):
    for window in window_sizes:
        df[f'signal_mean_{window}'] = df['signal'].rolling(window=window, min_periods=1, center=True).mean()
        df[f'signal_std_{window}'] = df['signal'].rolling(window=window, min_periods=1, center=True).std()
        df[f'signal_min_{window}'] = df['signal'].rolling(window=window, min_periods=1, center=True).min()
        df[f'signal_max_{window}'] = df['signal'].rolling(window=window, min_periods=1, center=True).max()
    return df

# CSV yükleme
uploaded_file = st.file_uploader("📤 Lütfen sinyal içeren CSV dosyasını yükleyin (signal sütunu olmalı)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("📄 İlk 5 satır:")
    st.write(data.head())

    if 'signal' in data.columns:
        # Özellikleri ekle
        data_feat = add_rolling_features(data.copy())

        # Tahmin
        feature_cols = [col for col in data_feat.columns if 'signal_' in col]
        X_input = data_feat[feature_cols].fillna(0)
        preds = model.predict(X_input)

        # Sonuç göster
        data['predicted_open_channels'] = preds
        st.success("✅ Tahminler tamamlandı!")
        st.write(data[['signal', 'predicted_open_channels']].head())

        # İndirilebilir hale getir
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Tahmin Sonuçlarını İndir", csv, "ion_switch_predictions.csv", "text/csv")

    else:
        st.warning("❗ 'signal' sütunu bulunamadı.")
