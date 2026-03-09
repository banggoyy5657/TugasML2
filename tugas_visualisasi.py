import pandas as pd
import matplotlib.pyplot as plt

# Membaca data CSV
data = pd.read_csv("tips.csv")

# Menampilkan 5 data pertama
print("5 data pertama:")
print(data.head())

# Mengelompokkan total tip berdasarkan hari
tips_per_day = data.groupby("day")["tip"].sum()

# Menampilkan hasil total tip per hari
print("\nTotal tip berdasarkan hari:")
print(tips_per_day)

# Menentukan hari dengan tip terbesar
hari_terbesar = tips_per_day.idxmax()
jumlah_terbesar = tips_per_day.max()

print(f"\nHari dengan total tip terbesar adalah {hari_terbesar} dengan total tip {jumlah_terbesar:.2f}")

# Membuat visualisasi bar chart
tips_per_day.plot(kind="bar")

plt.title("Total Tips Berdasarkan Hari")
plt.xlabel("Hari")
plt.ylabel("Total Tip")
plt.xticks(rotation=0)
plt.show()