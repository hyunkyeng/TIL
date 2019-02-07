--1. 상시간이 150분 이상인 화이름만 출력하세요.
SELECT 영화이름 FROM movies WHERE 상영시간 >= 150;
--2. 장르가 애니메이션인 화코드와 화이름를 출력하세요. 
SELECT 영화코드, 영화이름 FROM movies WHERE 장르='애니메이션';
--3. 제작국가가 덴마크이고 장르가 애니메이션인 화이름을 출력하세요.
SELECT 영화이름 FROM movies WHERE 제작국가='덴마크' and 장르='애니메이션';
--4. 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 화이름과 누적관객수를 출력하세 요. 
SELECT 영화이름, 누적관객수 FROM movies WHERE 관람등급='청소년관람불가' and 누적관객수>1000000;
-- SELECT * FROM movies WHERE 개봉연도 >= 200001010 and 개봉연도 <=20091231;

--5. 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 화를 출력하세요. 
SELECT * FROM movies WHERE 개봉연도 LIKE '200%';
--6. 장르를 중복 없이 출력하세요.
SELECT DISTINCT 장르 FROM movies;
