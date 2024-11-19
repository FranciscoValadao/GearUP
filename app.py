import streamlit as st
import debugpy

pg = st.navigation([st.Page("navigation/home_page.py", title="Home Page"),
                    st.Page("navigation/loadout_page.py", title="Loadout"),
                    st.Page("navigation/wishlist_page.py", title="Wishlist"),
                    st.Page("navigation/config_page.py", title="Configurações e acesso")
                     ])
pg.run()

try:
    debugpy.listen(5678)
    debugpy.wait_for_client()
except:
    pass
