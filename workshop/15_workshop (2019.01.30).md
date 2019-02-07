# 15_workshop (2019.01.30)

1. 아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 Data 를 입력해 봅시다.

>  Table Name : bands

id(INTEGER) 	name(TEXT) 	debut(INTEGER) 

1	 Queen	 1973 

2	 Coldplay 	1998 

3	 MCR	 2001



```sql
CREATE TABLE bands (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
debut INTRGER
);

INSERT INTO bands (name, debut)
VALUES ('Queen', 1973),('Coldplay', 1998),('MCR', 2001);
```





2. bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.

```sql
SELECT id, name FROM bands;
```





3.  bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.

```sql
SELECT name FROM bands WHERE debut<2000;
```

