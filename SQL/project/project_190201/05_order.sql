--1. 누적관객수 상위 5개 화의 모든 데이터를 출력하세요. 
SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
--2. 장르가 애니메이션인 화를 제작국가(오름차순), 누적관객수(내림차순)순으로 정렬하여 10개 만 출력하세요.
SELECT * FROM movies WHERE 장르="애니메이션" ORDER BY 제작국가 ASC, 누적관객수 DESC LIMIT 10;
--3. 상영시간이 긴 화를 만든 감독의 이름을 10개만 출력하세요. 
SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;