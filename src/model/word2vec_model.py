from gensim.models import Word2Vec
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .base_model import BaseModel

class Word2VecModel(BaseModel):
    def __init__(self, data, feature_column):
        super().__init__(data)
        self.feature_column = feature_column

    def fit(self):
        sentences = [row.split() for row in self.data[self.feature_column]]
        self.model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        self.vectors = np.array([self.model.wv[word] for word in self.model.wv.key_to_index])

    def get_recommendations(self, item_id, num_recommendations=5):
        idx = self.data[self.data['item_id'] == item_id].index[0]
        item_vector = np.mean([self.model.wv[word] for word in self.data[self.feature_column].iloc[idx].split() if word in self.model.wv], axis=0)
        similarities = cosine_similarity([item_vector], self.vectors)
        sim_scores = list(enumerate(similarities[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        item_indices = [i[0] for i in sim_scores]
        return self.data.iloc[item_indices]
