import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("global_hantavirus_surveillance_dataset_2026.csv")

transmission = df["transmission_type"].value_counts()

plt.figure(figsize=(7,5))
transmission.plot(kind="bar")
plt.title("Distribusi Jenis Transmisi")
plt.xlabel("Jenis Transmisi")
plt.ylabel("Jumlah Kasus")
plt.tight_layout()
plt.show()