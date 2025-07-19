import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataExplorer:
    """
    Utility class for basic data exploration and visualization.
    """

    @staticmethod
    def explore_data(data: pd.DataFrame) -> None:
        """
        Display head, description, and basic info of the dataset.
        """
        print(data.head().T)
        print(data.describe().T)
        data.info()

    @staticmethod
    def plot_histograms(data: pd.DataFrame) -> None:
        """
        Plot histograms for all numeric columns in the dataset.
        """
        data.hist(bins=15, figsize=(15, 10))
        plt.show()

    @staticmethod
    def plot_correlation_matrix(data: pd.DataFrame) -> None:
        """
        Plot a heatmap showing the correlation between variables.
        """
        plt.figure(figsize=(12, 8))
        sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
        plt.title("Feature Correlation Heatmap")
        plt.show()
