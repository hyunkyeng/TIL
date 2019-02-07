# 16_homework (2019.01.31)



1. 다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.

   id (INTEGER) 	name (TEXT) 	location (TEXT)

2. 해당 테이블에 다음과 같이 데이터를 입력한다.

   id (INTEGER) name (TEXT) location (TEXT)
   1	 Justin 	Seoul
   2 	Simon	 New York
   3 	Chang 	Las Vegas
   4 	John 	Sydney

3. 스키마를 다음과 같이 변경한다.

   id (INTEGER)	 name (TEXT)	 location (TEXT) 	married (INTEGER)

4. 데이터를 다음과 같이 추가한다.

   id (INTEGER) name (TEXT) location (TEXT) married (INTEGER)
   1	 Justin	 LA 	1
   2	 Simon	 New York 	0
   3 	Chang 	LasVegas 	0
   4	 John 	Sydney	 1

5. married 가 0 인 데이터를 모두 삭제한다.

   id (INTEGER) name (TEXT) location (TEXT) married (INTEGER)
   1	 Justin	 LA 		1
   4	 John	 Sydney	 1



```sql
CREATE TABLE friends (
id INTEGER PRIMARY KEY,
name TEXT,
location TEXT
);

INSERT INTO friends VALUES (1, 'Justin', 'Seoul');
INSERT INTO friends VALUES (2, 'Simon', 'New York');
INSERT INTO friends VALUES (3, 'Chang', 'Las Vegas');
INSERT INTO friends VALUES (4, 'John', 'Sydney');

--ALTER TABLE
--1. Rename Table
--2. Add new column to Table

ALTER TABLE friends ADD COLUMN married INTEGER;
--ALTER TABLE friends
--RENAME TO new_table_name;

UPDATE friends SET location="LA", married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;
UPDATE friends SET married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;


DELETE FROM friends WHERE married=0;

DROP TABLE friends;
```

