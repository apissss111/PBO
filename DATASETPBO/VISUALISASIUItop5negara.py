import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hantavirus.csv")

top_country = df["country"].value_counts().head(5)

plt.figure(figsize=(8,5))
top_country.plot(kind="bar")
plt.title("Top 5 Negara dengan Kasus Hantavirus Terbanyak")
plt.xlabel("Negara")
plt.ylabel("Jumlah Kasus")
plt.tight_layout()
plt.show()