# 16_workshop (2019.01.31)

저번 워크샵에서 아래 표와 같은 DB를 제작한 상태다.

1.  해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라.

   id(INTEGER) 	name(TEXT) 	debut(INTEGER) 	members(INTEGER) 

   1 	Queen 	1973 	4 

   2 	Coldplay 	1998 	5 

   3 	MCR 	2001 	9

```sql
ALTER TABLE bands ADD COLUMN members INTEGER;

UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=6 WHERE id=3;
```



2. Id 가 3인 레코드의 members 를 5로 수정하라.

```sql
UPDATE bands SET members=5 WHERE id=3;
```



3. Id 가 2인 레코드를 삭제하라

```sql
DELETE FROM bands WHERE id=2;
```

