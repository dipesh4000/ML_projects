import streamlit as st
import pandas as pd
import requests
import pickle
st.title('Movie Recommendation system')
movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similar.pkl', 'rb'))
movies_list = pd.DataFrame.from_dict(movies)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/search/movie/{}?api_key=616d7b2205f1f542a77fe4773c8f0553&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie, movies_list):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lis = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return movies_lis



movies_name = st.selectbox("Select Movie", movies_list['title'].values)


if st.button("Predict"):
    recommendations = recommend(movies_name, movies_list)
    for i in recommendations:
        fetch_poster(i[0])
        st.write(movies_list.loc[i[0]]['title'])
