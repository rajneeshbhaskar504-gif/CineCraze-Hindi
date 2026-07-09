import streamlit as st

st.set_page_config(
    page_title="CineCraze Hindi",
    page_icon="🎬",
    layout="wide"
)

st.markdown(
    """
    <style>
    body{
        background-color:#0f1117;
    }
    .title{
        text-align:center;
        color:red;
        font-size:45px;
        font-weight:bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="title">🎬 CineCraze Hindi</p>', unsafe_allow_html=True)

st.write("### Latest Movie Explained Videos")

search = st.text_input("🔍 Search Movie")

movies = [
    {
        "title": "Avengers: Endgame",
        "category": "Hollywood",
        "youtube": "https://www.youtube.com/watch?v=TcMBFSGVi1c"
    },
    {
        "title": "KGF Chapter 2",
        "category": "South Indian",
        "youtube": "https://www.youtube.com/watch?v=JKa05nyUmuQ"
    },
    {
        "title": "Train to Busan",
        "category": "Korean",
        "youtube": "https://www.youtube.com/watch?v=pyWuHv2-Abk"
    },
    {
        "title": "The Wandering Earth",
        "category": "Chinese",
        "youtube": "https://www.youtube.com/watch?v=0TDII5IkI3Y"
    }
]

for movie in movies:
    if search.lower() in movie["title"].lower():
        st.markdown("---")
        st.subheader(movie["title"])
        st.write("🎭 Category:", movie["category"])
        st.video(movie["youtube"])
