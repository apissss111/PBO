
# Pengujian HantavirusAnalyzer
class HantavirusAnalyzer:
    def __init__(self, data):
        self.data = data

    def totalCases(self):
        return self.data["Cases"].sum()

    def averageCases(self):
        return self.data["Cases"].mean()

    def maxCases(self):
        return self.data["Cases"].max()


analyzer = HantavirusAnalyzer(data)

print("Total Cases :", analyzer.totalCases())
print("Average Cases :", analyzer.averageCases())
print("Maximum Cases :", analyzer.maxCases())