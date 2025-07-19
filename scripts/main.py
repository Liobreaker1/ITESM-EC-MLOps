from models.wine_model import WineQualityModel

if __name__ == "__main__":
    path = "data/raw/wine_quality_df.csv"
    model = WineQualityModel(path)
    model.run_all()
    model.save_pipeline()

# PYTHONPATH=src python scripts/main.py
