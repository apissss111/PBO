import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("global_hantavirus_surveillance_dataset_2026.csv")

fatality = df["fatality"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(fatality,
        labels=fatality.index,
        autopct='%1.1f%%')
plt.title("Distribusi Fatality")
plt.show()