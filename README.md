# recommender-app

## Project Structure
```
recommendation_system/
  - README.md
  - main.py
  - app.py  # Streamlit app
  - notebooks/
    - data_exploration.ipynb
    - model_development.ipynb
  - src/
    - data_processing/
      - __init__.py
      - data_generation.py
      - data_cleaning.py
      - feature_engineering.py
    - models/
      - __init__.py
      - base_model.py
      - tfidf_model.py
      - word2vec_model.py
      - deep_learning_model.py
    - evaluation/
      - __init__.py
      - metrics_calculation.py
      - visualization.py
    - deployment/
      - __init__.py
      - deployment_script.sh
    - utils/
      - __init__.py
      - snowflake.py
      - oracle.py
    - sql/
      - __init__.py
      - data_queries.sql
      - model_queries.sql
  - tests/
    - test_data_processing.py
    - test_models.py
    - test_evaluation.py
  - docs/
    - API_documentation.md
    - model_documentation.md
  - requirements.txt
  - LICENSE
  - .gitignore
  - CONTRIBUTING.md
  - CHANGELOG.md
  - docker/ (optional)
    - Dockerfile
    - docker-compose.yml
  - scripts/ (optional)
    - utility_script.py
```
## To run this Project
```
$ docker build -t <img-name> .
$ docker images
$ docker run -it b1 bash
export all env variables
$ python3 main.py
$ streamlit run app.py
```

## Features

- **Data Processing**: Modules for generating, cleaning, and engineering features from data.
- **Multiple Models**: Implementations of various content-based recommendation techniques:
  - TF-IDF Model (Uses TF-IDF (Term Frequency-Inverse Document Frequency) to vectorize text data and cosine similarity to find similar items.)
  - Word2Vec Model (Trains a Word2Vec model on item descriptions and uses cosine similarity to find similar items based on word embeddings.)
  - Deep Learning Model (using BERT for text embeddings and cosine similarity to find similar items.)
- **Evaluation**: Tools for evaluating model performance and visualizing results.
- **Streamlit App**: Interactive UI for testing and comparing different models.


Precision, Recall, and F1-Score Calculation:

The precision_recall_f1 function calculates precision, recall, and F1-score at k.
precision is the ratio of relevant items recommended to the total recommended items.
recall is the ratio of relevant items recommended to the total relevant items.
f1_score is the harmonic mean of precision and recall.
Model Evaluation:

The evaluate_model function takes a recommendation model and dataset as input.
For each item in the dataset, it retrieves the true relevant items and the recommended items.
It calculates precision, recall, and F1-score at k and returns these metrics in a dictionary.
Visualization:

The plot_evaluation_metrics function takes a dictionary of evaluation results.
It plots bar charts for precision, recall, and F1-score for different models.