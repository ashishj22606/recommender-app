import matplotlib.pyplot as plt

def plot_evaluation_metrics(evaluation_results):
    """
    Plot evaluation metrics for different models.
    
    Args:
        evaluation_results (dict): Dictionary with model names as keys and evaluation metrics as values.
    """
    metrics = ['precision', 'recall', 'f1_score']
    
    for metric in metrics:
        plt.figure(figsize=(10, 5))
        for model_name, metrics in evaluation_results.items():
            plt.bar(model_name, metrics[metric], label=model_name)
        
        plt.xlabel('Model')
        plt.ylabel(metric.capitalize())
        plt.title(f'{metric.capitalize()} for Different Models')
        plt.legend()
        plt.show()
