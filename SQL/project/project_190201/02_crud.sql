INSERT INTO movies
VALUES (20182530, '극한직업', '15세이상관람가', '이병헌', 20190123, 3138467, 111, '한국', '코미디')
SELECT * FROM movies WHERE 영화코드=20040521;
DELETE FROM movies WHERE 영화코드=20040521;
SELECT * FROM movies WHERE 영화코드=20185124;
UPDATE movies SET 감독='없음' WHERE 영화코드=2018512
