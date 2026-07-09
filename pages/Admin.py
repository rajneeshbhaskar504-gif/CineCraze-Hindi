import streamlit as st

st.set_page_config(page_title="Admin Panel")

st.title("🔐 CineCraze Hindi - Admin Panel")

password = st.text_input("Admin Password", type="password")

if password == "admin123":
    st.success("Login Successful")

    movie_name = st.text_input("Movie Name")
    youtube_link = st.text_input("YouTube Video Link")
    category = st.selectbox(
        "Category",
        ["Hollywood", "Bollywood", "South", "Korean", "Chinese", "Anime"]
    )

    if st.button("Add Movie"):
        st.success(f"{movie_name} added successfully! (Database अगले स्टेप में जोड़ेंगे)")
else:
    if password:
        st.error("Wrong Password")
