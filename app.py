import streamlit as st

st.set_page_config(page_title="Object Hunt", page_icon=":material/search:")

pages = [
    st.Page("landing.py", title="Home", icon=":material/home:"),
    st.Page("play.py", title="Play", icon=":material/sports_esports:"),
]

pg = st.navigation(pages)


pg.run()

