"""
Create dashboard app'
"""

import streamlit as st

from backend_client import BackendClient
from sidebar import user_inputs_from_sidebar

# Connect to Backend REST API
backend_client = BackendClient()

# Set page config and hide hamburger menu
st.set_page_config(page_title='Demo Python app', initial_sidebar_state="expanded")
st.markdown("""<style>#MainMenu {visibility: hidden;}</style>""", unsafe_allow_html=True)

# Get user inputs from page sidebar
user, first_param, second_param, third_param = user_inputs_from_sidebar()

# Page header
st.subheader(f'Data of {user["user_name"]}')


# Fetch some data from database and cache results
@st.cache(show_spinner=False)
def fetch_user_data(user_id: int):
    return backend_client.fetch_data(user_id=user_id)


with st.spinner(text="Load user data..."):
    user_data = fetch_user_data(user_id=user['user_id'])

with st.expander(f"Display user data"):
    st.table(user_data)

with st.expander(f"Display processed data"):
    processed_data = backend_client.process_data(
        user_id=user['user_id'],
        measurements=user_data,
        some_param=third_param
    )
    st.table(processed_data)

with st.expander(f"Params"):
    st.markdown(f'First param is {first_param.value}')
    st.markdown(f'Second param is {second_param}')
    st.markdown(f'Third param is {third_param}')
