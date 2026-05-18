import streamlit as st
import pandas as pd
import numpy as np
import random
import os
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="성적 관리 시스템", layout="wide")

# --- 데이터 생성 함수 ---
def generate_mock_data():
    last_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황", "안", "송", "전", "홍"]
    first_names = ["민준", "서준", "도윤", "예준", "시우", "하준", "주원", "지호", "지후", "준서", "서연", "서윤", "지우", "서현", "하은", "하윤", "민서", "지유", "윤서", "지아"]
    
    data = []
    for i in range(100):
        name = random.choice(last_names) + random.choice(first_names)
        kor = random.randint(40, 100)
        eng = random.randint(40, 100)
        math = random.randint(40, 100)
        sci = random.randint(40, 100)
        
        total = kor + eng + math + sci
        avg = total / 4
        
        # 등급 부여
        if avg >= 90: grade = 'A'
        elif avg >= 80: grade = 'B'
        elif avg >= 70: grade = 'C'
        elif avg >= 60: grade = 'D'
        else: grade = 'E'
        
        data.append([name, kor, eng, math, sci, total, avg, grade])
    
    df = pd.DataFrame(data, columns=['이름', '국어', '영어', '수학', '과학', '총점', '평균', '등급'])
    df.to_csv("score.csv", index=False, encoding="utf-8-sig")
    return df

# 파일 존재 여부 확인 및 로드
def load_data():
    if os.path.exists("score.csv"):
        return pd.read_csv("score.csv")
    else:
        return None

# --- 사이드바 메뉴 ---
st.sidebar.title("📑 성적처리 시스템")
menu = st.sidebar.selectbox("메뉴를 선택하세요", ["HOME", "성적테이블조회", "성적시각화"])

# --- 메인 화면 로직 ---

# 1. HOME 메뉴
if menu == "HOME":
    st.title("🏠 성적 처리 시스템 HOME")
    st.write("본 애플리케이션은 학생들의 성적 데이터를 관리하고 시각화하는 도구입니다.")
    
    st.subheader("데이터 초기화 및 다운로드")
    if st.button("새로운 100명의 데이터 생성하기"):
        df = generate_mock_data()
        st.success("100명의 성적 데이터가 생성되어 score.csv로 저장되었습니다.")
        st.dataframe(df.head())
    
    if os.path.exists("score.csv"):
        with open("score.csv", "rb") as file:
            st.download_button(
                label="CSV 파일 다운로드",
                data=file,
                file_name="score.csv",
                mime="text/csv"
            )
    else:
        st.info("데이터가 없습니다. 위 버튼을 눌러 데이터를 먼저 생성해 주세요.")

# 2. 성적테이블조회 메뉴
elif menu == "성적테이블조회":
    st.title("🔍 성적 테이블 조회")
    df = load_data()
    
    if df is not None:
        # 검색 기능
        search_name = st.text_input("이름으로 검색")
        if search_name:
            display_df = df[df['이름'].str.contains(search_name)]
        else:
            display_df = df
            
        st.dataframe(display_df, use_container_width=True)
        
        # 간단한 통계
        col1, col2, col3 = st.columns(3)
        col1.metric("전체 인원", f"{len(df)}명")
        col2.metric("전체 평균", f"{df['평균'].mean():.2f}점")
        col3.metric("최고 점수(총점)", f"{df['총점'].max()}점")
    else:
        st.error("데이터 파일이 없습니다. HOME 메뉴에서 데이터를 먼저 생성해 주세요.")

# 3. 성적시각화 메뉴
elif menu == "성적시각화":
    st.title("📊 성적 데이터 시각화")
    df = load_data()
    
    if df is not None:
        tab1, tab2, tab3 = st.tabs(["등급 분포", "과목별 평균", "상위 10명"])
        
        with tab1:
            st.subheader("등급별 인원 분포")
            grade_counts = df['등급'].value_counts().sort_index()
            fig1 = px.pie(values=grade_counts.values, names=grade_counts.index, title="등급 분포 비율",
                          color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig1)
            
        with tab2:
            st.subheader("과목별 평균 점수")
            subjects = ['국어', '영어', '수학', '과학']
            avg_scores = df[subjects].mean()
            fig2 = px.bar(x=subjects, y=avg_scores.values, labels={'x': '과목', 'y': '평균 점수'},
                          range_y=[0, 100], color=subjects)
            st.plotly_chart(fig2)
            
            st.subheader("과목별 점수 분포 (Box Plot)")
            fig3 = px.box(df, y=subjects)
            st.plotly_chart(fig3)
            
        with tab3:
            st.subheader("총점 기준 상위 10명")
            top10 = df.nlargest(10, '총점')
            fig4 = px.bar(top10, x='이름', y='총점', color='평균', text='총점')
            st.plotly_chart(fig4)
            
    else:
        st.error("데이터 파일이 없습니다. HOME 메뉴에서 데이터를 먼저 생성해 주세요.")