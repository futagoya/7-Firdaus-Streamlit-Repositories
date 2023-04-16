import streamlit as st

def set_background():
    page_bg = '''
    <style>
    body {
    background-color: #444444;
    color: white;
    }
    </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)
