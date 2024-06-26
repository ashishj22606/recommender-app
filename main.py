from src.data_processing import data_generation, data_cleaning, feature_engineering
from src.models import tfidf_model, word2vec_model, deep_learning_model
from src.evaluation import metrics_calculation, visualization

def main():
    # Step 1: Data Generation
    print("Generating data from Oracle...")
    oracle_data = data_generation.generate_data_oracle()

    print("Generating data from Snowflake...")
    snowflake_data = data_generation.generate_data_snowflake()

    # Combine data from both sources
    data = pd.concat([oracle_data, snowflake_data])

    # Step 2: Data Cleaning
    print("Cleaning data...")
    cleaned_data = data_cleaning.clean_data(data)

    # Step 3: Feature Engineering
    print("Performing feature engineering...")
    feature_data = feature_engineering.create_features(cleaned_data)

    # Step 4: Initialize Models
    print("Initializing models...")
    models = {
        'TF-IDF': tfidf_model.TFIDFModel(feature_data, 'description'),
        'Word2Vec': word2vec_model.Word2VecModel(feature_data, 'description'),
        'DeepLearning': deep_learning_model.DeepLearningModel(feature_data, 'description')
    }

    # Step 5: Train and Evaluate Models
    evaluation_results = {}
    for model_name, model in models.items():
        print(f"Training {model_name} model...")
        model.fit()
        print(f"Evaluating {model_name} model...")
        evaluation_metrics = metrics_calculation.evaluate_model(model, feature_data)
        evaluation_results[model_name] = evaluation_metrics
        print(f"{model_name} evaluation metrics: {evaluation_metrics}")

    # Step 6: Visualize Evaluation Results
    print("Visualizing evaluation results...")
    visualization.plot_evaluation_metrics(evaluation_results)
    
    return models

if __name__ == "__main__":
    main()
