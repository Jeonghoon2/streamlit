import streamlit as st


def login():
    st.title("암호키")
    password = st.text_input('암호키는 **"playdata"** 랍니다.', type="password")
    if st.button("확인"):
        if password == "playdata":
            return True  # 로그인 성공

    return False  # 버튼 클릭 시 로그인 실패
