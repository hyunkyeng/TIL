# 15_homework (2019.01.30)



1. 우리가 사용하는 SQLite 는 RDBMS 에 속한다. RDBMS 의 특징을 2가지만 작성하 세요.

> RDBMS(Relational Database Management System)
>
> : RDBMS는 관계형 데이터베이스를 생성하고 수정하고 관리할 수 있는 소프트웨어라고 정의할 수 있습니다.
>
>
>
> (특징)
>
> - 모든 데이터를 2차원 테이블로 표현
>
> - 테이블은 row(record, tuple)과 column(field, item)으로 이루어진 기본 데이터 저장 단위
>
> - 상호관련성을 가진 테이블(table)의 집합
>
> - 만들거나 이용하기도 비교적 쉽지만, 무엇보다도 확장이 용이하다는 장점을 가짐
>
> - 데이터베이스의 설계도를 ER(Entity Relationship) 모델
>
> - ER모델에 따라, 데이터베이스가 만들어지며, 데이터베이스는 하나 이상의 테이블로 구성 됨. ER모델에서 엔티티를 기반으로 테이블이 만들어짐



2. True False 

   2.1. RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [ T ]

   2.2. SQL 에서 명령어는 대문자로 써야만 동작한다. [ F - 소문자도 가능하지만 대문자 권장] 

   2.3. 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [ T ] 

   2.4. SQLite 에서 dot(.) 으로 시작하는 명령어는 SQL 이 아니다.[ T ] 

   2.5. 한 개의 DB 에는 한개의 테이블만 존재한다. [ F ]



3. 다음 코드의 실행결과로 나타나는 값을 작성하세요. 



   ```sql
   sqlite> .nullvalue “NULL” 
   
   sqlite> CREATE TABLE ssafy (
   
   	 …> id INTEGER,
   
   	 …> location TEXT,
   
   	 …> class INTEGER …> ); 
   
   sqlite> INSERT INTO ssafy (id, location) 
   
   	…> VALUES (1, ‘JEJU’);
   
   sqlite> SELECT class FROM ssafy WHERE id=1;
   ```

   > NULL
