import streamlit as st

st.set_page_config(
    page_title="CineCraze Hindi",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 CineCraze Hindi")
st.subheader("Welcome to CineCraze Hindi")

st.write("यहाँ आपको Movie Explained वीडियो, मूवी की जानकारी और नई अपडेट्स मिलेंगी।")

st.text_input("🔍 Search Movie")

st.header("🔥 Trending Movies")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://placehold.co/300x450?text=Movie+1")
    st.write("Movie 1")

with col2:
    st.image("https://placehold.co/300x450?text=Movie+2")
    st.write("Movie 2")

with col3:
    st.image("https://placehold.co/300x450?text=Movie+3")
    st.write("Movie 3")
