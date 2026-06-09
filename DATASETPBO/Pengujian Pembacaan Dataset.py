# Pengujian Pembacaan Dataset
import pandas as pd

class DataService:
    def loadCSV(self, filename):
        return pd.read_csv(filename)


service = DataService()

data = service.loadCSV("hantavirus.csv")

print(data.head())
