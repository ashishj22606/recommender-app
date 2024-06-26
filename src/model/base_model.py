class BaseModel:
    def __init__(self, data):
        self.data = data

    def fit(self):
        raise NotImplementedError("Each model must implement this method.")

    def get_recommendations(self, item_id, num_recommendations):
        raise NotImplementedError("Each model must implement this method.")
