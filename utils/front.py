import base64
import streamlit as st

def get_img_as_base64(img_path):
    with open(img_path, 'rb') as f:
        img = f.read()
    return base64.b64encode(img).decode()


def generate_frontend_backgrounds():
    side_bg = get_img_as_base64('constants/static/background.jpg')
    main_bg = get_img_as_base64('constants/static/main_background.jpg')
    # page_img_background = f"""
    #     <style>
    #     [data-testid="stAppViewContainer"] > .main {{
    #     background-image: url("data:image/jpg;base64,{main_bg}");
    #     background-size: 100%;
    #     background-position: cover;
    #     background-repeat: no-repeat;
    #     background-attachment: fixed;
    #     }}
    #     [data-testid="stHeader"] {{
    #     background-color: rgba(0, 0, 0, 0);
    #     }}
    #     [data-testid="stToolbar"] {{
    #     right: 2rem;
    #     }}
    #     [data-testid="stSidebar"] > div:first-child {{
    #     background-image: url("data:image/jpg;base64,{side_bg}");
    #     background-size: 100%;
    #     background-position: cover;
    #     background-repeat: no-repeat;
    #     background-attachment: fixed;
    #     }}
    #     </style>
    #     """
    page_img_background = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main{{
    background-color: #08120a;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/jpg;base64,{side_bg}");
    background-size: 100%;
    background-position: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}
    </style>
    """
    return page_img_background

def progress_bar(streamlit_call=False, progress=None, value=0):
    if not streamlit_call:
        pass
    elif streamlit_call and value == 0:
        progress = st.progress(value)
    elif streamlit_call and value != 0:
        progress.progress(value)
    return progress