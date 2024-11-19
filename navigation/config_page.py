import streamlit as st
import dotenv
import os
from constants.constants import LOGS_PATH
from utils.front import generate_frontend_backgrounds
import utils.tools as tools
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

st.set_page_config(page_title='Configurações', page_icon=':gear:')
page_img_background =  generate_frontend_backgrounds()
st.markdown(page_img_background, unsafe_allow_html=True)

st.header('Configurações e Acesso')
creds = {}
st.write('Aqui você pode configurar o acesso ao Streamlit Debugger e outras configurações.')
tab1, tab2, tab3 = st.tabs(["Credenciais", "Logs", "Relatórios"])

with tab1:
     col1, col2 = st.columns(2)
     with col1:
          st.write("Credenciais do OJS")
          on = st.toggle("Editar credenciais privadas", key='ojs_creds')
          if st.session_state.ojs_creds:
               creds['ojs_url'] = st.text_input("URL do OJS", placeholder=os.getenv('OJS'), key='ojs_url')
               creds['ojs_user'] = st.text_input("Usuário", placeholder=os.getenv('OJS_user'), key='ojs_user')
               creds['ojs_pass'] = st.text_input("Senha", placeholder=os.getenv('OJS_pass'), key='ojs_pass')
               creds['ojs_key'] = st.text_input("Chave de Acesso", placeholder=os.getenv('OJS_key'), key='ojs_key')
     with col2:
          st.write("Credenciais do Dspace")
          st.toggle("Editar credenciais privadas", key='dspace_creds')
          if st.session_state.dspace_creds:
               creds['dspace_url'] = st.text_input("URL do Dspace", placeholder=os.getenv('DSPACE'), key='dspace_url')
               creds['dspace_user'] = st.text_input("Usuário", placeholder=os.getenv('DSPACE_user'), key='dspace_user')
               creds['dspace_pass'] = st.text_input("Senha", placeholder=os.getenv('DSPACE_pass'), key='dspace_pass')

     if st.button('Salvar novas credenciais'):
          if creds.get('ojs_url'):
               dotenv.set_key(dotenv_file, "OJS", st.session_state.ojs_url)
          if creds.get('ojs_user'):
               dotenv.set_key(dotenv_file, "OJS_user", st.session_state.ojs_user)
          if creds.get('ojs_pass'):
               dotenv.set_key(dotenv_file, "OJS_pass", st.session_state.ojs_pass)
          if creds.get('ojs_key'):
               dotenv.set_key(dotenv_file, "OJS_key", st.session_state.ojs_key)
          if creds.get('dspace_url'):
               dotenv.set_key(dotenv_file, "DSPACE", st.session_state.dspace_url)
          if creds.get('dspace_user'):
               dotenv.set_key(dotenv_file, "DSPACE_user", st.session_state.dspace_user)
          if creds.get('dspace_pass'):
               dotenv.set_key(dotenv_file, "DSPACE_pass", st.session_state.dspace_pass)
          dotenv.load_dotenv(dotenv_file, override=True)
with tab2:
     st.write("Logs")
     logs_content = tools.get_file_content_as_bytes(LOGS_PATH)
     st.download_button(
          label="Download Logs",
          data=logs_content,
          file_name="logs.log",
          mime="text/plain"
     )
with tab3:
     st.write("Relatórios")