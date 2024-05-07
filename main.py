from src.data_processing import data_generation, data_cleaning, feature_engineering
# from src.model import recommendation_model
# from src.evaluation import metrics_calculation, visualization
# from src.deployment import deployment_script


def main():

    # Generate data from Oracle
    data_generation.generate_data_oracle()

    # Generate data from Snowflake
    data_generation.generate_data_snowflake()

if __name__ == "__main__":
    main()
