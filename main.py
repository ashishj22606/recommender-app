# main.py

from src.data_processing import data_generation, data_cleaning, feature_engineering
from src.model import recommendation_model
from src.evaluation import metrics_calculation, visualization
from src.deployment import deployment_script

def main():
    # Generate data
    data_generation.generate_data()

    # Clean and preprocess data
    data_cleaning.clean_data()
    feature_engineering.engineer_features()

    # Train recommendation model
    recommendation_model.train_model()

    # Evaluate model performance
    metrics = metrics_calculation.calculate_metrics()
    visualization.visualize_metrics(metrics)

    # Deploy recommendation system
    deployment_script.deploy()

if __name__ == "__main__":
    main()
