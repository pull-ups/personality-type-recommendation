# Psychological Test-Based Film/Music Recommendation System
## 프로젝트 개요

- 심리테스트를 통하여 사용자의 취향이 입력되면 영화와 음악을 추천해주는 시스템
- `Python` `Recommendation System` `NLP` `Django` 

## 프로젝트 과정
1. Data Collection
    - 영화의 경우, 네이버 영화의 영화 랭킹에서 평점순으로 상위 1000개의 영화 데이터 수집
    - 영화 제목, 장르, 개봉연도, 평점, 줄거리, 리뷰, 이미지 url 수집
    - 음악의 경우, 벅스의 뮤직PD 앨범에서 테마별로 플레이리스트의 음악 데이터 수집
    - 음악 테마, 제목, 가수, 앨범명, 가사, 앨범 커버 수집
2. Data Preprocessing & EDA
    - 음악 데이터 중 가사 전체가 외국어일 경우, 외국 음악으로 간주하여 제외
    - 토큰화 후 pretrained된 `Word2Vec` 에 전이학습
    - 하나의 영화에 해당하는 리뷰 데이터(200개)에 나오는 단어들의 벡터의 평균으로 영화 벡터 계산
    - 음악은 가사에 나오는 단어들의 벡터의 평균으로 계산
3. Modeling
    - 각 영화/음악의 벡터와 8개의 성향 단어 사전과의 Cosine Similarity 계산
    - 각 영화 장르/음악 테마에 대해서는 성향과의 유사도를 휴리스틱하게 계산
    - 각 영화/음악이 가지고 있는 텍스트 데이터 0.8/장르 0.2 비중으로 반영하여 -1 ~ 1로 정규화
    - 사용자의 응답을 -1 ~ 1로 정규화하여 각 영화/음악 성향 축과의 Euclidean Distance 계산 후 거리 짧은 순으로 추천
4. Web Implemention
![muflix](https://user-images.githubusercontent.com/59776953/165169028-46ed4c5d-7241-48da-aa60-d7a371481180.png)
	- `Django` 로 웹사이트 구현
	- `AWS`의 `Lightsail`을 통하여 배포
