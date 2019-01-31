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

```

