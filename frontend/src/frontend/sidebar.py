"""
Create page sidebar with user inputs.
"""
import os
from typing import Tuple

import streamlit as st
from constants import MyEnum
from frontend.backend_client import BackendClient


def user_inputs_from_sidebar() -> Tuple[dict, MyEnum, bool, float]:
    """
    Displays app' sidebar with various user inputs.

    Returns: Tuple[NamedTuple, MyEnum, bool, float]
        user (dict): a dict with keys 'user_id' (int) and 'user_name' (str)
        first_param (MyEnum): selected value from a custom enumeration
        second_param (bool): some boolean input
        third_param (float): some float input

    """
    st.sidebar.title("Demo app")

    user: dict = st.sidebar.selectbox(
        'Choose a user from database:',
        options=BackendClient().fetch_users(),
        format_func=lambda _user: f'{_user["user_name"]} (id={_user["user_id"]})'
    )

    with st.sidebar.container():
        st.sidebar.subheader('Set some params: ')

        first_param: MyEnum = st.sidebar.radio(
            label='A radio param',
            options=MyEnum.__members__.values(),
            format_func=lambda v: v.value
        )

        second_param: bool = st.sidebar.checkbox(
            label='A boolean param',
            value=True
        )

        third_param = st.sidebar.slider(
            'A slider param',
            min_value=0.0, max_value=1.0, step=0.1,
            value=float(os.getenv('MY_FRONTEND_PARAM', 1.0))
        )

    return user, first_param, second_param, third_param
