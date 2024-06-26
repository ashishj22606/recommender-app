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