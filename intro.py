# intro.py
import streamlit as st

def intro():
    st.markdown("""
            # Hello 👋

            - **Git**
            - **Pyenv**
            - **Airflow**
            - **Streamlit**
        """)

    if st.button("로그아웃"):
        st.session_state['is_login'] = False
        st.experimental_rerun()  # 로그아웃 후 로그인 페이지로 이동
