#!/usr/bin/env python
# coding: utf-8


import pickle
import numpy as np
import pandas as pd
    
class Movie_Recommendation:
    
    def __init__(self):
        self.label = []
        self.movie = pd.read_csv("movie_mbti_similarity_200.csv")
        with open('movie_genre_200.pickle', 'rb') as f:
            self.genre_score = pickle.load(f)
     
    def Label_Normalize(self, labels):
        from sklearn.preprocessing import MinMaxScaler
        transformer = MinMaxScaler(feature_range=(-1, 1))

        self.label = np.array(labels).reshape(-1, 1)
        transformer.fit(self.label)
        self.label = transformer.transform(self.label)
        
        return self.label

    
    ### 장르 반영 x
    def recommendation(self, labels):
        from operator import itemgetter
        recommend = []

        for idx, data in enumerate(range(len(self.movie))):
            label = self.Label_Normalize(labels)

            from scipy.spatial import distance
            distance = distance.euclidean(sum(label.tolist(), []), self.movie.iloc[idx, -8:].tolist())
            recommend.append((idx, distance))

        recommend.sort(key=itemgetter(1))
        print(self.movie.iloc[pd.Series(recommend[:5]).apply(lambda x: x[0]).values]['title'])
        
        
    ### 장르 반영
    def recommendation_g(self, labels):
        from operator import itemgetter
        recommend = []

        for idx, data in enumerate(range(len(self.movie))):
            label = self.Label_Normalize(labels)

            from scipy.spatial import distance
            dis = distance.euclidean(sum(label.tolist(), []), self.movie.iloc[idx, -8:].tolist())

            # 장르 점수 계산
            genre = self.genre_score['genre_score'][idx]
            dis += distance.euclidean(sum(label.tolist(), []), sum(genre.tolist(), []))
            
            recommend.append((idx, dis))

        recommend.sort(key=itemgetter(1))
        print(self.movie.iloc[pd.Series(recommend[:5]).apply(lambda x: x[0]).values]['title'])