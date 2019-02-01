# SQL

```bash
hyunkyeng:~/workspace $ sqlite3
.mode csv
----------------------------설정

.import hellodb.csv examples
.tables
SELECT * FROM examples;   #SELECT 문 :  내용을 반환한다. 

-----------------------------
.exit     #종료
```

```bash
# 테이블 만들기
CREATE TABLE classmate (
id INT PRIMARY KEY,
name TEXT,
age INT,
address TEXT
);
#테이블 있는지 확인
.tables
#테이블 읽어오기
.read class_table.sql
#테이블 지우기
DROP TABLE classmate;
#
.schema classmate


#테이블 값 모두 가져오기
SELECT * FROM classmate;
#테이블의 특정 컬럼만 가져오기
SELECT id, name FROM classmate;
#가져오는 ROW(레코드) 개수를 지정하기 (제일 앞부터 가져온다.)
SELECT id, name FROM classmate LIMIT 2;
#가져오는 ROW(레코드) 의 시작점 지정
SELECT * FROM classmate LIMIT 1 OFFSET 2;
#특정한 값을 가진 row만 조회하기
SELECT * FROM classmate WHERE address='서울';
SELECT * FROM classmate WHERE id=2;
#서울에 사는 사람의 이름은?
SELECT name FROM classmate WHERE address='서울';


#보통 값을 지울 때는 유니크한 값인 id를 지운다 ( 3번 값을 지우면 그 후에는 3번은 추가되지 않는다.)
DELETE FROM classmate WHERE id=3;

#값을 바꿀때 ( 원래 홍길동, 서울 -> 홍홍홍, 제주)
UPDATE classmate
SET name='홍홍홍', address='제주'
WHERE id=4;
#id값이 4이거나 6인애를 바꾼다. (--id값은 유니트한 값이므로 1개만 가진다. 따라서 and는 사용안됨. )
UPDATE classmate
SET name='박성주', address='제주'
WHERE id=4 or id=6;


#중복없이 조회
SELECT DISTINCT age FROM classmate;

## 처음 파일 가져올 때 ##
sqlite> .headers on
sqlite> .mode column
sqlite> .mode csv
sqlite> .import users.csv users   # users.csv 를 users 이름으로 가져온다 (테이블이름정하기)

#전체에서 나이가 30이상인 사람만 가져오기
SELECT * FROM users WHERE age>=30;   # * : 전체
#나이가 30이상인 사람의 이름만 가져오기
SELECT first_name FROM users WHERE age>=30;   
#나이가 30이상, 성이 김씨인 사람의 성과 나이만 조회
SELECT last_name, age FROM users WHERE age>=30 and last_name="김";
#users에 들어있는 숫자 세기
SELECT COUNT(*) FROM users;  # * : 전체를 가르킴
#나이가 30이상인 사람들의 평균나이
SELECT AVG(age) FROM users WHERE age>=30;
#balance가 가장 높은 사람의 이름과 balance
SELECT first_name, MAX(balance) FROM users;
#나이가 30이상인 사람들의 평균 잔액
SELECT AVG(balance) FROM users WHERE age>=30;

##Like 사용

#나이가 2로 시작하는 사람(20대)
SELECT * FROM users WHERE age LIKE '2%';
#번호가 02- 로 시작하는 사람
SELECT * FROM users WHERE phone LIKE '02-%';
#이름이 준으로 끝나는 사람
SELECT * FROM users WHERE first_name LIKE '%준';
#번호 중간번호가 5113인 사람
SELECT * FROM users WHERE phone LIKE '%5114%';
#1로 시작하고 4자리인 값
LIKE 1___

##오름차순, 내림차순 

#오름차순으로 정렬하여 상위 10개만 가져오기
SELECT * FROM users ORDER BY age ASC LIMIT 10;
#오름차순으로 정렬하여 상위 10개의 나이롸 성만 가져오기
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
#계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개만 조회.
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
```

