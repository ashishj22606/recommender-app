import numpy as np

def precision_recall_f1(y_true, y_pred, k=5):
    """
    Calculate precision, recall, and F1-score at k.
    
    Args:
        y_true (list of list of int): List of true relevant items for each query.
        y_pred (list of list of int): List of predicted items for each query.
        k (int): Number of top-k items to consider for evaluation.
        
    Returns:
        precision (float): Precision at k.
        recall (float): Recall at k.
        f1_score (float): F1-score at k.
    """
    precision = 0.0
    recall = 0.0
    for true_items, pred_items in zip(y_true, y_pred):
        true_items_set = set(true_items)
        pred_items_set = set(pred_items[:k])
        intersection = true_items_set & pred_items_set
        precision += len(intersection) / min(k, len(pred_items_set))
        recall += len(intersection) / len(true_items_set)
    
    precision /= len(y_true)
    recall /= len(y_true)
    if precision + recall > 0:
        f1_score = 2 * (precision * recall) / (precision + recall)
    else:
        f1_score = 0.0
    
    return precision, recall, f1_score

def evaluate_model(model, data, k=5):
    """
    Evaluate the recommendation model.
    
    Args:
        model: The recommendation model to evaluate.
        data: The dataset used for evaluation.
        k (int): Number of top-k items to consider for evaluation.
        
    Returns:
        evaluation_metrics (dict): Dictionary with precision, recall, and F1-score.
    """
    y_true = []
    y_pred = []
    
    for item_id in data['item_id']:
        true_items = data[data['item_id'] == item_id]['related_items'].values[0]
        recommendations = model.get_recommendations(item_id, k)
        recommended_items = recommendations['item_id'].tolist()
        
        y_true.append(true_items)
        y_pred.append(recommended_items)
    
    precision, recall, f1_score = precision_recall_f1(y_true, y_pred, k)
    evaluation_metrics = {
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }
    
    return evaluation_metrics
