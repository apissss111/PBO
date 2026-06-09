# Pengujian Class HantavirusCase
class HantavirusCase:
    def __init__(self, location, year,
                 transmission_type,
                 risk_level, cases):
        self.location = location
        self.year = year
        self.transmission_type = transmission_type
        self.risk_level = risk_level
        self.cases = cases

    def getRiskCategory(self):
        return self.risk_level


case = HantavirusCase(
    "Kalimantan Timur",
    2025,
    "Rodent-to-human",
    "High",
    45
)

print("Kategori Risiko:", case.getRiskCategory())





