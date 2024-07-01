import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import plotly.express as px
import random

# Database setup
conn = sqlite3.connect('advanced_movies.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS movies
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              director TEXT NOT NULL,
              release_year INTEGER NOT NULL,
              language TEXT NOT NULL,
              rating FLOAT NOT NULL,
              genre TEXT NOT NULL,
              runtime INTEGER NOT NULL,
              box_office REAL,
              added_date TEXT NOT NULL)''')
conn.commit()

# Helper functions
def add_movie(title, director, release_year, language, rating, genre, runtime, box_office):
    added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO movies (title, director, release_year, language, rating, genre, runtime, box_office, added_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (title, director, release_year, language, rating, genre, runtime, box_office, added_date))
    conn.commit()

def get_all_movies():
    return pd.read_sql_query("SELECT * FROM movies", conn)

def update_movie(id, title, director, release_year, language, rating, genre, runtime, box_office):
    c.execute("UPDATE movies SET title=?, director=?, release_year=?, language=?, rating=?, genre=?, runtime=?, box_office=? WHERE id=?",
              (title, director, release_year, language, rating, genre, runtime, box_office, id))
    conn.commit()

def delete_movie(id):
    c.execute("DELETE FROM movies WHERE id=?", (id,))
    conn.commit()

def filter_movies(criteria, value):
    if criteria in ['release_year', 'rating', 'runtime', 'box_office']:
        return pd.read_sql_query(f"SELECT * FROM movies WHERE {criteria} = ?", conn, params=(value,))
    else:
        return pd.read_sql_query(f"SELECT * FROM movies WHERE {criteria} LIKE ?", conn, params=('%' + value + '%',))

def count_movies_by_language(language):
    return c.execute("SELECT COUNT(*) FROM movies WHERE language=?", (language,)).fetchone()[0]

def get_top_rated_movies(limit=10):
    return pd.read_sql_query(f"SELECT * FROM movies ORDER BY rating DESC LIMIT {limit}", conn)

def get_movies_by_decade(decade):
    start_year = decade * 10
    end_year = start_year + 9
    return pd.read_sql_query("SELECT * FROM movies WHERE release_year BETWEEN ? AND ?", conn, params=(start_year, end_year))

# Add default movies
default_movies = [
    ("The Shawshank Redemption", "Frank Darabont", 1994, "English", 9.3, "Drama", 142, 58.3),
    ("The Godfather", "Francis Ford Coppola", 1972, "English", 9.2, "Crime", 175, 134.9),
    ("Pulp Fiction", "Quentin Tarantino", 1994, "English", 8.9, "Crime", 154, 107.9),
    ("The Dark Knight", "Christopher Nolan", 2008, "English", 9.0, "Action", 152, 1004.6),
    ("12 Angry Men", "Sidney Lumet", 1957, "English", 9.0, "Drama", 96, 0.5),
    ("Schindler's List", "Steven Spielberg", 1993, "English", 9.0, "Biography", 195, 96.9),
    ("The Lord of the Rings: The Return of the King", "Peter Jackson", 2003, "English", 9.0, "Adventure", 201, 1146.0),
    ("Inception", "Christopher Nolan", 2010, "English", 8.8, "Sci-Fi", 148, 836.8),
    ("Goodfellas", "Martin Scorsese", 1990, "English", 8.7, "Crime", 146, 46.8),
    ("The Matrix", "Lana Wachowski", 1999, "English", 8.7, "Sci-Fi", 136, 463.5),
    ("Forrest Gump", "Robert Zemeckis", 1994, "English", 8.8, "Drama", 142, 678.2),
    ("City of God", "Fernando Meirelles", 2002, "Portuguese", 8.6, "Crime", 130, 7.6),
    ("Seven Samurai", "Akira Kurosawa", 1954, "Japanese", 8.6, "Action", 207, 0.3),
    "Spirited Away", "Hayao Miyazaki", 2001, "Japanese", 8.6, "Animation", 125, 355.5),
    ("Saving Private Ryan", "Steven Spielberg", 1998, "English", 8.6, "War", 169, 482.3),
    ("Life Is Beautiful", "Roberto Benigni", 1997, "Italian", 8.6, "Comedy", 116, 57.6),
    ("The Usual Suspects", "Bryan Singer", 1995, "English", 8.5, "Crime", 106, 23.3),
    ("Léon: The Professional", "Luc Besson", 1994, "English", 8.5, "Action", 110, 19.5),
    ("The Lion King", "Roger Allers", 1994, "English", 8.5, "Animation", 88, 968.5),
    ("American History X", "Tony Kaye", 1998, "English", 8.5, "Drama", 119, 6.7),
    ("Terminator 2: Judgment Day", "James Cameron", 1991, "English", 8.5, "Action", 137, 519.8),
    ("Cinema Paradiso", "Giuseppe Tornatore", 1988, "Italian", 8.5, "Drama", 155, 11.9),
    ("Back to the Future", "Robert Zemeckis", 1985, "English", 8.5, "Adventure", 116, 380.6),
    ("Raiders of the Lost Ark", "Steven Spielberg", 1981, "English", 8.4, "Action", 115, 389.9),
    ("Apocalypse Now", "Francis Ford Coppola", 1979, "English", 8.4, "War", 147, 83.5),
    ("Alien", "Ridley Scott", 1979, "English", 8.4, "Sci-Fi", 117, 104.9),
    ("The Great Dictator", "Charlie Chaplin", 1940, "English", 8.4, "Comedy", 125, 0.3),
    ("Modern Times", "Charlie Chaplin", 1936, "English", 8.5, "Comedy", 87, 0.2),
    ("City Lights", "Charlie Chaplin", 1931, "English", 8.5, "Comedy", 87, 0.02),
    ("Casablanca", "Michael Curtiz", 1942, "English", 8.5, "Drama", 102, 1.0)
]

# Add default movies if the table is empty
if c.execute("SELECT COUNT(*) FROM movies").fetchone()[0] == 0:
    for movie in default_movies:
        add_movie(*movie)

# Streamlit app
st.set_page_config(page_title="Advanced Movie List Application", layout="wide")

st.title("🎬 Advanced Movie List Application")

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Add Movie", "Filter Movies", "Update Movie", "Delete Movie", "Analytics"])

if page == "Home":
    st.header("📋 All Movies")
    movies = get_all_movies()
    st.dataframe(movies)

    st.subheader("🔢 Movie Count by Language")
    language = st.selectbox("Select Language", movies['language'].unique())
    count = count_movies_by_language(language)
    st.write(f"Number of movies in {language}: {count}")

    st.subheader("🌟 Top Rated Movies")
    top_movies = get_top_rated_movies()
    st.dataframe(top_movies)

elif page == "Add Movie":
    st.header("➕ Add a New Movie")
    title = st.text_input("Title")
    director = st.text_input("Director")
    release_year = st.number_input("Release Year", min_value=1800, max_value=datetime.now().year, step=1)
    language = st.text_input("Language")
    rating = st.slider("Rating", 0.0, 10.0, 5.0, 0.1)
    genre = st.text_input("Genre")
    runtime = st.number_input("Runtime (minutes)", min_value=1, step=1)
    box_office = st.number_input("Box Office (million $)", min_value=0.0, step=0.1)

    if st.button("Add Movie"):
        add_movie(title, director, release_year, language, rating, genre, runtime, box_office)
        st.success("Movie added successfully!")

elif page == "Filter Movies":
    st.header("🔍 Filter Movies")
    filter_option = st.selectbox("Filter by", ["Title", "Director", "Release Year", "Language", "Rating", "Genre", "Runtime", "Box Office"])
    filter_value = st.text_input("Enter filter value")

    if st.button("Filter"):
        filtered_movies = filter_movies(filter_option.lower().replace(" ", "_"), filter_value)
        st.dataframe(filtered_movies)

elif page == "Update Movie":
    st.header("✏️ Update Movie")
    movies = get_all_movies()
    movie_to_update = st.selectbox("Select Movie to Update", movies['title'])
    movie_data = movies[movies['title'] == movie_to_update].iloc[0]

    title = st.text_input("Title", movie_data['title'])
    director = st.text_input("Director", movie_data['director'])
    release_year = st.number_input("Release Year", min_value=1800, max_value=datetime.now().year, step=1, value=movie_data['release_year'])
    language = st.text_input("Language", movie_data['language'])
    rating = st.slider("Rating", 0.0, 10.0, float(movie_data['rating']), 0.1)
    genre = st.text_input("Genre", movie_data['genre'])
    runtime = st.number_input("Runtime (minutes)", min_value=1, step=1, value=movie_data['runtime'])
    box_office = st.number_input("Box Office (million $)", min_value=0.0, step=0.1, value=movie_data['box_office'])

    if st.button("Update Movie"):
        update_movie(movie_data['id'], title, director, release_year, language, rating, genre, runtime, box_office)
        st.success("Movie updated successfully!")

elif page == "Delete Movie":
    st.header("🗑️ Delete Movie")
    movies = get_all_movies()
    movie_to_delete = st.selectbox("Select Movie to Delete", movies['title'])

    if st.button("Delete Movie"):
        movie_id = movies[movies['title'] == movie_to_delete]['id'].iloc[0]
        delete_movie(movie_id)
        st.success("Movie deleted successfully!")

elif page == "Analytics":
    st.header("📊 Movie Analytics")

    st.subheader("Movies by Decade")
    decades = list(range(1920, datetime.now().year // 10 * 10 + 1, 10))
    selected_decade = st.selectbox("Select Decade", decades)
    decade_movies = get_movies_by_decade(selected_decade // 10)
    st.dataframe(decade_movies)

    st.subheader("Rating Distribution")
    fig = px.histogram(get_all_movies(), x="rating", nbins=20, title="Rating Distribution")
    st.plotly_chart(fig)

    st.subheader("Top Box Office Performers")
    top_box_office = get_all_movies().sort_values("box_office", ascending=False).head(10)
    fig = px.bar(top_box_office, x="title", y="box_office", title="Top 10 Box Office Performers")
    st.plotly_chart(fig)

    st.subheader("Movies by Language")
    language_counts = get_all_movies()['language'].value_counts()
    fig = px.pie(values=language_counts.values, names=language_counts.index, title="Movies by Language")
    st.plotly_chart(fig)

# Close the database connection when the app is done
conn.close()