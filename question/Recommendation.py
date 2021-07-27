import pickle
import numpy as np
import pandas as pd

class Recommendation:
    
    def __init__(self):
        self.label = []
        self.movie = pd.read_csv("question/movie_data.csv")
        with open('question/movie_genre_data.pickle', 'rb') as f:
            self.genre_score = pickle.load(f)
        #self.music = pd.read_csv("music_data.csv") 
        
    def Label_Normalize(self, labels):
        from sklearn.preprocessing import MinMaxScaler
        transformer = MinMaxScaler(feature_range=(-1, 1))

        self.label = np.array(labels).reshape(-1, 1)
        transformer.fit(self.label)
        self.label = transformer.transform(self.label)
        
        return self.label

    
    ### 영화 추천
    def movie_recommendation(self, labels, num=4):
        from operator import itemgetter
        recommend = []

        for idx, data in enumerate(range(len(self.movie))):
            label = self.Label_Normalize(labels)

            from scipy.spatial import distance
            dis_mbti = distance.euclidean(sum(label.tolist(), []), self.movie.iloc[idx, -8:].tolist())
            genre = self.genre_score['genre_score'][idx]
            dis_genre = distance.euclidean(sum(label.tolist(), []), sum(genre.tolist(), []))
            
            dis = 0.8*dis_mbti + 0.2*dis_genre
            recommend.append((idx, dis))

        recommend.sort(key=itemgetter(1))
        index = pd.Series(recommend[:num]).apply(lambda x: x[0]).values
        
        return self.movie.loc[index, ['movie_id', 'title', 'user_rating', 'summary']]

    
    ### 음악 추천
    def music_recommendation(self, labels, num=4):
        from operator import itemgetter
        recommend = []

        for idx, data in enumerate(range(len(self.music))):
            label = self.Label_Normalize(labels)

            from scipy.spatial import distance
            dis_mbti = distance.euclidean(sum(label.tolist(), []), self.music.iloc[idx, -16:-8].tolist())
            dis_genre = distance.euclidean(sum(label.tolist(), []), self.music.iloc[idx, -8:].tolist())
            
            dis = 0.8*dis_mbti + 0.2*dis_genre
            recommend.append((idx, dis))

        recommend.sort(key=itemgetter(1))
        index = pd.Series(recommend[:num]).apply(lambda x: x[0]).values
        
        return self.music.loc[index, ['Title', 'Artist', 'Album', 'Lyric']]