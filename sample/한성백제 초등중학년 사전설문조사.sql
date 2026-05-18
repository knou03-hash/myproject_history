--- 1. 기존 테이블 삭제 (초기화용)
DROP TABLE IF EXISTS survey;

-- 2. survey 테이블 생성
CREATE TABLE survey (
    idx INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    gender TEXT, -- 성별 (남, 여)
    q1 INTEGER,  -- 역사 공부/이야기 선호도
    q2 INTEGER,  -- 박물관/유적지 방문 즐거움
    q3 INTEGER,  -- 백제 한성 성립 지식 (1:예, 2:아니오)
    q4 INTEGER,  -- 주변 옛 성(풍납토성 등) 지식
    q5 INTEGER,  -- 유물 이름/모양 지식
    q6 INTEGER,  -- 발굴 과정 관심도
    q7 INTEGER,  -- 디지털 기기 활용 재미 기대감
    q8 INTEGER,  -- 태블릿/컴퓨터 사용 자신감
    q9 INTEGER,  -- 문화유산 더 알고 싶은 마음
    q10 INTEGER  -- 수업 참여 준비도
);

-- 3. 10개의 가상 데이터(Mock Data) 삽입
INSERT INTO survey (gender, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10) VALUES 
('남', 1, 2, 1, 2, 3, 1, 1, 1, 2, 1),
('여', 2, 1, 1, 3, 2, 2, 1, 2, 1, 1),
('남', 4, 5, 2, 5, 4, 3, 2, 1, 4, 3),
('여', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
('남', 3, 3, 2, 4, 4, 4, 2, 2, 3, 2),
('여', 2, 2, 1, 2, 2, 3, 1, 1, 2, 2),
('남', 5, 4, 2, 5, 5, 5, 3, 1, 5, 4),
('여', 3, 2, 1, 3, 3, 2, 2, 2, 2, 2),
('남', 1, 3, 1, 2, 3, 2, 1, 1, 1, 1),
('여', 2, 3, 2, 4, 3, 4, 2, 3, 3, 2);

-- 4. 전체 데이터 확인
SELECT * FROM survey;