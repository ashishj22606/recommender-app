# recommender-app

## Project Structure
```
- recommendation_system/
  - README.md
  - main.py
  - notebooks/
    - data_exploration.ipynb
    - model_development.ipynb
  - src/
    - data_processing/
      - __init__.py
      - data_generation.py
      - data_cleaning.py
      - feature_engineering.py
    - model/
      - __init__.py
      - recommendation_model.py
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
    - test_model.py
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
```
