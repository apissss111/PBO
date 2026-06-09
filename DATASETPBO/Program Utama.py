
# Program Utama
service = DataService()

data = service.loadCSV("hantavirus.csv")

analyzer = HantavirusAnalyzer(data)

print("=== ANALISIS HANTAVIRUS ===")

print("Total Cases :", analyzer.totalCases())
print("Average Cases :", analyzer.averageCases())
print("Maximum Cases :", analyzer.maxCases())