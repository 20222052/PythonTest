import requests
import pandas as pd

# URL API
url = "http://api.plos.org/search?q=title:VIRUS&fl=id,eissn,author_display,abstract,title_display,score"

# Gửi yêu cầu GET đến API
response = requests.get(url)

data = response.json()

# Trích xuất danh sách bài báo
docs = data.get("response", {}).get("docs", [])

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(docs)

# Lưu vào file CSV
df.to_csv("./TH06BT_TungNT/Paper.csv", index=False, encoding="utf-8")

print("Dữ liệu đã được lưu vào Paper.csv")