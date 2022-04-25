#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
    
class Music_Recommendation:
    
    def __init__(self):
        self.label = []
        self.music = pd.read_csv("music_scores.csv")
     
    def Label_Normalize(self, labels):
        from sklearn.preprocessing import MinMaxScaler
        transformer = MinMaxScaler(feature_range=(-1, 1))

        self.label = np.array(labels).reshape(-1, 1)
        transformer.fit(self.label)
        self.label = transformer.transform(self.label)
        
        return self.label
        
        
    ### 장르 반영
    def recommendation_g(self, labels):
        from operator import itemgetter
        recommend = []

        for idx, data in enumerate(range(len(self.music))):
            label = self.Label_Normalize(labels)

            from scipy.spatial import distance
            distance_l = distance.euclidean(sum(label.tolist(), []), self.music.iloc[idx, -16:-8].tolist())
            distance_t = distance.euclidean(sum(label.tolist(), []), self.music.iloc[idx, -8:].tolist())
            distance = 0.6*distance_l + 0.4*distance_t

            recommend.append((idx, distance))

        recommend.sort(key=itemgetter(1))
        print(self.music.iloc[pd.Series(recommend[:5]).apply(lambda x: x[0]).values]['Title'])