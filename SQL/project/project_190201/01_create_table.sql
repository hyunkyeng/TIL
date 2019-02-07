--1. 아래와 같은 스키마를 가진 movies 테이블을 만드세요.
CREATE TABLE movies (
'영화코드' INTEGER PRIMARY KEY,
'영화이름' TEXT,
'관람등급' TEXT,
'감독' TEXT,
'개봉연도' INTEGER,
'누적관객수' INTEGER,
'상영시간' INTEGER,
'제작국가' TEXT,
'장르' TEXT
);

--2. header와 mode 설정을 적절하게 하세요.
.mode csv
.import boxoffice.csv movies
.headers on
.made column

--3. 전체 데이터를 출력하세요.
SELECT * FROM movies;