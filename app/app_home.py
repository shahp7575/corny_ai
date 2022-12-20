import streamlit as st
from streamlit_lottie import st_lottie
from lottie import lottie_book

st.set_page_config(layout='centered', page_title='Corny AI')

st_lottie(lottie_book, speed=0.9, height=200, key="initial")
st.markdown("<h1 style='text-align: center;'>Corny AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>AI which is sometimes very funny</h4>", unsafe_allow_html=True)

prompt = st.text_input(label="dad_joke_prompt", 
                    placeholder="What was so badly broken in Breaking Bad?", 
                    label_visibility="collapsed")

temp = st.slider(label="temperature", 
                min_value=0.0, 
                max_value=1.0,
                value=0.75,
                label_visibility="collapsed")

generate = st.button("Generate")

