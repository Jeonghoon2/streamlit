import streamlit as st
from login import login
from intro import intro


def main():
    if 'is_login' not in st.session_state:
        st.session_state['is_login'] = False

    # 로그인 상태 확인
    if st.session_state['is_login']:
        intro()
    else:
        if login():
            st.session_state['is_login'] = True
            st.rerun()


if __name__ == '__main__':
    main()
