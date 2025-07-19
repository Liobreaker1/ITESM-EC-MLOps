from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from explorer.data_explorer import DataExplorer

import joblib
import os


class WineQualityModel:
    """
    A class to encapsulate the machine learning workflow for predicting wine quality.
    """

    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath
        self.data: Optional[pd.DataFrame] = None
        self.X_train: Optional[pd.DataFrame] = None
        self.X_test: Optional[pd.DataFrame] = None
        self.y_train: Optional[pd.Series] = None
        self.y_test: Optional[pd.Series] = None
        self.model_pipeline: Pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("classifier", LogisticRegression(max_iter=1000)),
            ]
        )

    def load_data(self) -> "WineQualityModel":
        try:
            self.data = pd.read_csv(self.filepath)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            raise

        if self.data is None or self.data.empty:
            raise ValueError("Loaded data is empty.")

        if "quality" not in self.data.columns:
            raise ValueError("Column 'quality' not found in dataset.")

        DataExplorer.explore_data(self.data)
        return self

    def preprocess_data(self) -> "WineQualityModel":
        X = self.data.drop("quality", axis=1)
        y = self.data["quality"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        return self

    def train_model(self) -> "WineQualityModel":
        self.model_pipeline.fit(self.X_train, self.y_train)
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model_pipeline.predict(X)

    def evaluate_model(self) -> "WineQualityModel":
        y_pred = self.predict(self.X_test)

        cm = confusion_matrix(self.y_test, y_pred)
        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm, display_labels=np.unique(self.y_test)
        )
        disp.plot(cmap="Blues")
        plt.title("Confusion Matrix")
        plt.show()

        print("Classification Report:")
        print(classification_report(self.y_test, y_pred))

        return self

    def cross_validate_model(self) -> "WineQualityModel":
        scores = cross_val_score(self.model_pipeline, self.X_train, self.y_train, cv=5)
        print("Cross-validation scores:", scores)
        print("Average Accuracy:", np.mean(scores))

        plt.figure(figsize=(6, 4))
        sns.barplot(x=list(range(1, 6)), y=scores)
        plt.title("Cross-validation Accuracy per Fold")
        plt.xlabel("Fold")
        plt.ylabel("Accuracy")
        plt.ylim(0, 1)
        plt.show()

        return self

    def run_all(self) -> "WineQualityModel":
        return (
            self.load_data()
            .preprocess_data()
            .train_model()
            .evaluate_model()
            .cross_validate_model()
        )

    def save_pipeline(self, path: str = "models/wine_quality_pipeline.joblib") -> None:
        """
        Saves the trained pipeline to a file.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model_pipeline, path)
        print(f"Pipeline saved to {path}")

