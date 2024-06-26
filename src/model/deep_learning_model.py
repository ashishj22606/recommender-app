import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from .base_model import BaseModel

class DeepLearningModel(BaseModel):
    def __init__(self, data, feature_column):
        super().__init__(data)
        self.feature_column = feature_column

    def fit(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

        def embed_text(text):
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
            outputs = self.model(**inputs)
            return outputs.last_hidden_state.mean(dim=1).detach().numpy()

        self.embeddings = np.array([embed_text(text) for text in self.data[self.feature_column]])

    def get_recommendations(self, item_id, num_recommendations=5):
        idx = self.data[self.data['item_id'] == item_id].index[0]
        item_embedding = self.embeddings[idx]
        similarities = cosine_similarity([item_embedding], self.embeddings)
        sim_scores = list(enumerate(similarities[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        item_indices = [i[0] for i in sim_scores]
        return self.data.iloc[item_indices]
