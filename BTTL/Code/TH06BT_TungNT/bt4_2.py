import pandas as pd

# Đọc dữ liệu từ file TXT (phân tách bằng tab)
df_station = pd.read_csv("data_lc.txt", sep="\t")

# Hiển thị 10 dòng đầu tiên
print(df_station.head(10))
