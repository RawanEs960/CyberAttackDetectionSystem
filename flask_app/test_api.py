import pandas as pd
import joblib
import requests

# قراءة البيانات
df = pd.read_csv("../data/cicids2017_cleaned.csv")

# حذف العمود الهدف
df = df.drop("Attack Type", axis=1)

# تحميل النموذج
model = joblib.load("../models/xgboost_model.pkl")

# اختيار نفس الـ features
features = model.feature_names_in_
df = df[features]

# أخذ sample
#sample = df.iloc[2013869].tolist()

sample = df.iloc[432988].tolist()

# إرسال للـ API
url = "http://127.0.0.1:5000/predict"
response = requests.post(url, json={"features": sample})

print(response.json())

# print(response.status_code)
# print(response.text)

print(model.predict([sample]))


