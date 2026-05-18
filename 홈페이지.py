import streamlit as st
st.title('삼국전성기 어드벤처')

c1, c2 = st.columns((4,1))
with c1:
    with st.expander('Contents'):
        url='https://www.youtube.com/watch?v=Eg_Y-MD-MY4'
        st.video(url)
        st.info('오늘의 국은 삼국')    
        txt_data = '''삼국 시대 한강 유역은 한반도의 중앙에 위치하여 비옥한 평야와 서해 해상 교통로를 확보한 경제·군사·문화의 핵심 요충지였습니다. 한강을 차지한 나라가 우수한 농업 생산력과 중국의 선진 문물을 받아들여 전성기를 누렸기에(백제→고구려→신라), 삼국은 이 지역을 차지하기 위해 치열한 쟁탈전을 벌였습니다.'''
        st.markdown(txt_data)
      
        
with c2:
    with st.expander('Tips...'):
        imglink='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBUNJOOO5vUVs27OZ8_KV9awSAZvIX0ECiYA&s'
        st.image(imglink)
        st.info('삼국의 발전과정')
        
c3, c4 = st.columns((4,1))
with c3:
    with st.expander('Contents'):
        url='https://www.youtube.com/watch?v=VMqEFT29YLY'
        st.video(url)
        st.info('근초고왕과 후예들')    
        txt_data = '''4세기 백제는 근초고왕(재위 346~375) 대 전성기를 맞아 한반도 중서부를 넘어 마한 전역, 황해도 일부까지 영토를 확장하고 중국 요서, 산둥, 일본 규슈로 진출한 해상 강국이었습니다. 철기 문화를 바탕으로 중앙 집권 국가의 기틀을 확립했으며, 왜(일본)에 선진 문물을 전파했습니다. '''
        st.markdown(txt_data)
c3, c4 = st.columns((4,1))
    
        
with c4:
    with st.expander('Tips...'):
        imglink='https://contents.history.go.kr/data/img/ta/ta_m71/map_036_01.jpg'
        st.image(imglink)
        st.info('this is right!!')