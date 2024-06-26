from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from .base_model.py import BaseModel

class TFIDFModel(BaseModel):
    def __init__(self, data, feature_column):
        super().__init__(data)
        self.feature_column = feature_column

    def fit(self):
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.data[self.feature_column])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, item_id, num_recommendations=5):
        idx = self.data[self.data['item_id'] == item_id].index[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        item_indices = [i[0] for i in sim_scores]
        return self.data.iloc[item_indices]
