# Evaluation and Metrics

This section provides an overview of the evaluation metrics and procedures used to assess the performance of the recommendation models.

## Precision, Recall, and F1-Score Calculation

The evaluation of recommendation models is based on three primary metrics: precision, recall, and F1-score.

- **Precision**: The ratio of relevant items recommended to the total recommended items. It indicates the accuracy of the recommendations.
  - Formula: 
    ```markdown
    Precision = (Number of relevant items recommended) / (Total recommended items)
    ```

- **Recall**: The ratio of relevant items recommended to the total relevant items. It measures the completeness of the recommendations.
  - Formula: 
    ```markdown
    Recall = (Number of relevant items recommended) / (Total relevant items)
    ```

- **F1-Score**: The harmonic mean of precision and recall. It provides a single metric that balances both precision and recall.
  - Formula: 
    ```markdown
    F1-Score = 2 * (Precision * Recall) / (Precision + Recall)
    ```

- The `precision_recall_f1` function calculates these metrics at k, where k is the number of top recommendations considered.
