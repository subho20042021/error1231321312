import streamlit as st
import pandas as pd
import pickle
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def getresponse(id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=7e24300fc9f72f2bd7977f808cbcd06f")
    data = response.json()
    st.write(data['poster_path'])
    return "https:image.tmdb.org/t/p/w500/" + data['poster_path']


def recomend(name):
    movie_index = movies[movies['title'] == name].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    movie_poster = []
    for i in movie_list:
        movie_poster.append(getresponse(movies['id'][i[0]]))
        recommend_movies.append(movies['title'][i[0]])

    return recommend_movies, movie_poster


movies = pd.DataFrame(movies)

st.title("MOVIE RECOMMENDER SYSTEM")

movie_select = st.selectbox(
    'MOVIES',
    movies['title'])

if st.button("RECOMMEND"):
    name, path = recomend(movie_select)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(path[0])

    with col2:
        st.text(name[1])
        st.image(path[1])

    with col3:
        st.text(name[2])
        st.image(path[2])

    with col3:
        st.text(name[3])
        st.image(path[3])

    with col3:
        st.text(name[4])
        st.image(path[4])
