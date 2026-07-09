import streamlit as st

st.set_page_config(
    page_title="CineCraze Hindi",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0f1117;
}
.title {
    text-align: center;
    color: #ff4b4b;
    font-size: 45px;
    font-weight: bold;
}
.movie-card {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎬 CineCraze Hindi")
    page = st.radio(
        "📂 Menu",
        [
            "🏠 Home",
            "🔥 Trending",
            "🎭 Categories",
            "📞 Contact"
        ]
    )

movies = [
    {
        "title": "Avengers: Endgame",
        "category": "Hollywood",
        "poster": "https://placehold.co/300x450?text=Avengers",
        "youtube": "https://www.youtube.com/watch?v=TcMBFSGVi1c"
    },
    {
        "title": "KGF Chapter 2",
        "category": "South Indian",
        "poster": "https://placehold.co/300x450?text=KGF+2",
        "youtube": "https://www.youtube.com/watch?v=JKa05nyUmuQ"
    },
    {
        "title": "Train To Busan",
        "category": "Korean",
        "poster": "https://placehold.co/300x450?text=Train+To+Busan",
        "youtube": "https://www.youtube.com/watch?v=pyWuHv2-Abk"
    },
    {
        "title": "The Wandering Earth",
        "category": "Chinese",
        "poster": "https://placehold.co/300x450?text=Wandering+Earth",
        "youtube": "https://www.youtube.com/watch?v=0TDII5IkI3Y"
    }
]

if page == "🏠 Home":

    st.markdown("<h1 class='title'>🎬 CineCraze Hindi</h1>", unsafe_allow_html=True)

    search = st.text_input("🔍 Search Movie")

    for movie in movies:
        if search.lower() in movie["title"].lower():

            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

            col1, col2 = st.columns([1,2])

            with col1:
                st.image(movie["poster"])

            with col2:
                st.subheader(movie["title"])
                st.write("🎭 Category:", movie["category"])
                st.video(movie["youtube"])

            st.markdown("</div>", unsafe_allow_html=True)

elif page == "🔥 Trending":

    st.title("🔥 Trending Movies")

    for movie in movies:
        st.subheader(movie["title"])
        st.image(movie["poster"], width=180)

elif page == "🎭 Categories":

    st.title("🎭 Categories")

    category = st.selectbox(
        "Choose Category",
        [
            "Hollywood",
            "South Indian",
            "Korean",
            "Chinese"
        ]
    )

    for movie in movies:
        if movie["category"] == category:
            st.subheader(movie["title"])
            st.image(movie["poster"], width=180)
            st.video(movie["youtube"])

elif page == "📞 Contact":

    st.title("📞 Contact")

    st.write("Email : cinecraze@gmail.com")
    st.write("YouTube : CineCraze Hindi")
    st.write("Made with ❤️ using Streamlit")
