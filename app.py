import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
#from scraper_api import ScraperAPIClient

movies = pickle.load(open('movies.pkl', 'rb'))

v = pickle.load(open('v.pkl', 'rb'))
v1 = pickle.load(open('v1.pkl', 'rb'))
v2 = pickle.load(open('v2.pkl', 'rb'))
v3 = pickle.load(open('v3.pkl', 'rb'))
v4 = pickle.load(open('v4.pkl', 'rb'))
v5 = pickle.load(open('v5.pkl', 'rb'))
v6 = pickle.load(open('v6.pkl', 'rb'))
v7 = pickle.load(open('v7.pkl', 'rb'))

similarity = np.concatenate([v, v1, v2, v3, v4, v5, v6, v7], axis=0)


def getresponse(uid):
    client = ScraperAPIClient('2233b77a536cee35ec5b6a78411717ec')
    response = requests.get(f'https://api.themoviedb.org/3/movie/{uid}?api_key=7e24300fc9f72f2bd7977f808cbcd06f')
    data = response.json()
    return "https:image.tmdb.org/t/p/w500/" + data['poster_path'], data['overview']


def recommend(name):
    movie_index = movies[movies['title'] == name].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    movie_poster = []
    movie_overview = []
    for i in movie_list:
        recommend_movies.append(movies['title'][i[0]])
    for i in movie_list:
        a, b = getresponse(movies['id'][i[0]])
        movie_overview.append(b)
        movie_poster.append(a)

    return recommend_movies, movie_poster,movie_overview


movies = pd.DataFrame(movies)

st.title("MOVIE RECOMMENDER SYSTEM")


movie_select = st.selectbox(
    'MOVIES',
    movies['title'])

if st.button("RECOMMEND"):
    name, path, overview = recommend(movie_select)

    with st.container(border=True):
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.header("1.")
        with col2:
            st.header(name[0])
        st.image(path[0], width=350)
        st.write(':red[OVERVIEW :]', str(overview[0]))

    with st.container(border=True):
        col3, col4 = st.columns([0.1, 3])
        with col3:
            st.header("2.")
        with col4:
            st.header(name[1])
        st.image(path[1], width=350)
        st.write(':red[OVERVIEW :]', str(overview[1]))

    with st.container(border=True):
        col5, col6 = st.columns([0.1, 3])
        with col5:
            st.header("3.")
        with col6:
            st.header(name[2])
        st.image(path[2], width=350)
        st.write(':red[OVERVIEW :]', str(overview[2]))

    with st.container(border=True):
        col7, col8 = st.columns([0.1, 3])
        with col7:
            st.header("4.")
        with col8:
            st.header(name[3])
        st.image(path[3], width=350)
        st.write(':red[OVERVIEW :]', str(overview[3]))
    with st.container(border=True):
        col9, col10 = st.columns([0.1, 3])
        with col9:
            st.header("5.")
        with col10:
            st.header(name[4])
        st.image(path[4], width=350)
        st.write(':red[OVERVIEW :]', str(overview[4]))

