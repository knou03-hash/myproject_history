import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px  # 더 예쁜 차트를 위해 사용

# 1. 페이지 설정
st.set_page_config(page_title="중학생 한능검 응시 현황", layout="wide")

# 2. Mock Data 생성 함수 (캐싱 처리하여 속도 향상)
@st.cache_data
def get_mock_data():
    regions = ['서울', '경기', '부산', '대구', '광주', '대전', '울산', '인천', '강원', '충청', '전라', '경상', '제주']
    grades = ['1학년', '2학년', '3학년']
    data = []
    
    for i in range(1000): # 500명 데이터
        grade = np.random.choice(grades)
        # 학년별 평균 점수 차등
        if grade == '1학년': score = np.random.normal(55, 12)
        elif grade == '2학년': score = np.random.normal(65, 10)
        else: score = np.random.normal(72, 8)
        
        score = np.clip(score, 0, 100)
        status = '합격' if score >= 60 else '불합격'
        
        data.append({
            '이름': f"학생_{i+1}",
            '지역': np.random.choice(regions),
            '학년': grade,
            '점수': round(score, 1),
            '합격여부': status
        })
    return pd.DataFrame(data)

df = get_mock_data()

# 3. 사이드바 - 필터 설정
st.sidebar.header("📊 필터 설정")
selected_grade = st.sidebar.multiselect("학년 선택", options=df['학년'].unique(), default=df['학년'].unique())
df_filtered = df[df['학년'].isin(selected_grade)]

# 4. 메인 화면 타이틀
st.title("🇰🇷 중학생 한국사능력검정시험 응시 데이터")
st.markdown("가상으로 생성된 데이터를 바탕으로 한 응시 및 합격 현황 대시보드입니다.")

# 5. 주요 지표 (Metrics)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("총 응시자 수", f"{len(df_filtered)}명")
with col2:
    avg_score = df_filtered['점수'].mean()
    st.metric("평균 점수", f"{avg_score:.1f}점")
with col3:
    pass_count = len(df_filtered[df_filtered['합격여부'] == '합격'])
    st.metric("합격자 수", f"{pass_count}명")
with col4:
    pass_rate = (pass_count / len(df_filtered)) * 100 if len(df_filtered) > 0 else 0
    st.metric("전체 합격률", f"{pass_rate:.1f}%")

st.divider()

# 6. 시각화 섹션
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📌 학년별 합격/불합격 인원")
    # 학년별, 합격여부별로 그룹화하여 카운트
    chart_data = df_filtered.groupby(['학년', '합격여부']).size().reset_index(name='인원수')
    fig1 = px.bar(chart_data, x='학년', y='인원수', color='합격여부', barmode='group',
                  color_discrete_map={'합격': '#2ecc71', '불합격': '#e74c3c'})
    st.plotly_chart(fig1, use_container_width=True)

with row1_col2:
    st.subheader("📍 지역별 응시자 분포")
    region_data = df_filtered['지역'].value_counts().reset_index()
    region_data.columns = ['지역', '응시자수']
    fig2 = px.pie(region_data, values='응시자수', names='지역', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

# 7. 점수 분포도 (Histogram)
st.subheader("📈 점수 분포 현황")
fig3 = px.histogram(df_filtered, x='점수', nbins=20, color='학년', 
                   marginal="box", # 상단에 박스플롯 추가
                   title="전체 점수 분포 (60점 합격선)")
fig3.add_vline(x=60, line_dash="dash", line_color="red", annotation_text="합격선(60점)")
st.plotly_chart(fig3, use_container_width=True)

# 8. 상세 데이터 보기
with st.expander("📄 상세 데이터 확인하기"):
    st.dataframe(df_filtered, use_container_width=True)