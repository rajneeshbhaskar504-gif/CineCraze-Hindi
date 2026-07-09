import streamlit as st

st.set_page_config(
    page_title="CineCraze Hindi",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 CineCraze Hindi")
st.markdown("### Latest Movie Explained Videos")

search = st.text_input("🔍 Search Movie")

movies = [
    {
        "title": "Avengers: Endgame",
        "category": "Hollywood",
        "youtube": "https://www.youtube.com/"
    },
    {
        "title": "KGF Chapter 2",
        "category": "South",
        "youtube": "https://www.youtube.com/"
    }
]

for movie in movies:
    if search.lower() in movie["title"].lower():
        st.subheader(movie["title"])
        st.write("Category:", movie["category"])
        st.link_button("▶ Watch on YouTube", movie["youtube"])
        st.divider()
