import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from sklearn.decomposition import TruncatedSVD

class RecommendationModel:
    def __init__(self, df):
        self.df = df
    
    def tfidf_vectorize(self, column):
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.df[column])
        return self.tfidf_matrix
    
    def calculate_cosine_similarity(self, matrix):
        self.cosine_sim = cosine_similarity(matrix, matrix)
        return self.cosine_sim
    
    def train_word2vec(self, sentences):
        self.word2vec_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        return self.word2vec_model
    
    def apply_svd(self, matrix, n_components=2):
        svd = TruncatedSVD(n_components=n_components)
        self.svd_matrix = svd.fit_transform(matrix)
        return self.svd_matrix
    
    def get_recommendations(self, item_id, num_recommendations=5):
        idx = self.df[self.df['item_id'] == item_id].index[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        item_indices = [i[0] for i in sim_scores]
        return self.df.iloc[item_indices]
