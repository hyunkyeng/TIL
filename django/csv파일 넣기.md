

csv파일 django에 넣기

```
 $ sqlite3 db.sqlite3 
 sqlite> .tables    #table이름을 확인한다. 내 table이름은 movies_movie
 sqlite> .mode csv
 sqlite> .import data.csv movies_movie
 sqlite> SELECT * FROM movies_movie;
```

