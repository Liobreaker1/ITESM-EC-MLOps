from models.wine_model import WineQualityModel

if __name__ == "__main__":
    path = "data/raw/wine_quality_df.csv"
    model = WineQualityModel(path)
    model.run_all()

# PYTHONPATH=src python scripts/main.py
