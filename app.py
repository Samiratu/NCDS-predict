import about
import diabetes
import heart
import streamlit as st

PAGES = {
    "Diabetes": diabetes,
    "Heart": heart,
    "About": about,
}

st.sidebar.title('Supported NCDs')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()