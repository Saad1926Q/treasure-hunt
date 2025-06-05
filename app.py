import streamlit as st

st.set_page_config(page_title="Object Hunt", page_icon=":material/search:")

pages = [
    st.Page("landing.py", title="Home", icon=":material/home:"),
    st.Page("play.py", title="Play", icon=":material/sports_esports:"),
]

pg = st.navigation(pages)

with st.sidebar.container(height=220):
    if pg.title == "Home":
        st.subheader("🏠 Home")
        st.write("Welcome to Object Hunt!")
        st.write("Learn how the game works and get started.")
    elif pg.title == "Play":
        st.subheader("🎮 Play")
        st.write("Start the treasure hunt game using your webcam.")
        st.write("Find real-world objects using YOLOv8.")
    else:
        st.subheader("📄 Info")
        st.write("Select a page from above to view its content.")


pg.run()

