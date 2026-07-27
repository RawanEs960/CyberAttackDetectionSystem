import pandas as pd
import joblib
import requests

pipeline = joblib.load("../notebooks/pipeline.pkl")

model = pipeline["model"]
features = pipeline["features"]

df = pd.read_csv("../data/cicids2017_cleaned.csv")

df = df[features]

sample = df.iloc[100000].tolist()  

url = "http://127.0.0.1:5000/predict"
response = requests.post(url, json={"features": sample})

# print(response.json())

print(response.status_code)
print(response.text)


# import requests

# url = "http://127.0.0.1:5000/predict_csv"

# files = {
#     "file": open("../data/cicids2017_cleaned.csv", "rb")
# }

# response = requests.post(url, files=files)

# print(response.json())