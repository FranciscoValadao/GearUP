import streamlit as st
from constants.constants import LEFT_LOGO_PATH, RIGHT_DARK_LOGO_PATH
from utils.front import generate_frontend_backgrounds

st.set_page_config(page_title='Home Page', page_icon=':herb:')

page_img_background =  generate_frontend_backgrounds()
st.markdown(page_img_background, unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image(LEFT_LOGO_PATH, width=100)
with col2:
    st.header('Bem Vind@!')
    st.write('Este é o sistema de análise de faturas em pdf')
with col3:
    st.image(RIGHT_DARK_LOGO_PATH)
st.write('Aqui você pode subir uma fatura em pdf e analisar os dados utilizando AI')
st.write('Para começar, acesse o menu ao lado')
st.write('Versâo 0.0.1')
