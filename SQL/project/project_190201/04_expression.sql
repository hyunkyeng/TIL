-- 1. 모든 화의 총 누적관객수를 출력하세요. 
SELECT SUM(누적관객수) FROM movies;
-- 2. 가장 많은 누적관객수인 화이름과 누적관객수를 출력하세요. 
SELECT 영화이름, max(누적관객수) FROM movies;
-- 3. 가장 상시간이 짧은 화의 장르와 상시간을 출력하세요. 
SELECT 장르, min(상영시간) FROM movies;
-- 4. 제작국가가 한국인 화의 평균 누적관객수를 출력하세요. 
SELECT AVG(누적관객수) FROM movies WHERE 제작국가="한국";
-- 5. 관람등급이 청소년관람불가인 화의 개수를 출력하세요. 
SELECT COUNT(*) FROM movies WHERE 관람등급='청소년관람불가';
-- 6. 상시간이 100분 이상이고 장르가 애니메이션인 화의 개수를 출력하세요.
SELECT COUNT(*) FROM movies WHERE 상영시간 >= 100 and 장르="애니메이션";