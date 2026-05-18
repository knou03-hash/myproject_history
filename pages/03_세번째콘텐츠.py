import streamlit as st
st.subheader('세번째 컨텐츠')

name = st.text_input('Name:')
age = st.number_input('Age:', min_value=1, max_value=100, step=1)
email = st.text_input('Email:')
if st.button('방명록에 추가하기'):
    if all([name, age, email]):
        input_Data=f'{name},{age},{email}\n'
        with open('./guestbook.csv', 'a') as f: # 'r'이면 매번 새로 쓰기, 'a'이면 기존 데이터 뒤에 추가
            f.write(input_Data)
            f.close() 
else:
    st.error('모든 값은 필수입니다.')

###로그인 시스템을 만들 수 있음###



#아래에 방명록 테이블 보여주기
import pandas as pd
df_guest = pd.read_csv('./guestbook.csv', encoding='cp949')
st.write(df_guest)   