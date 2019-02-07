# ORM

#### # 장점

1. 객체지향적인 코드로 인해 직관적이고 비즈니스로직에 더 집중할 수 있게 한다.
2. 재사용/유지보수가 증가
3. DB에 대한 종속성이 줄어듬

#### # 단점

1. 오로지 ORM 으로만은 거대한 서비스를 구현하기가 어렵다.
2. 어느정도의 속도 저하 



#### # 설치, 환경설정

```sql
(flask-venv) hyunkyeng:~/workspace/orm $ pip install flask_sqlalchemy
(flask-venv) hyunkyeng:~/workspace/orm $ pip install flask_migrate
```

```sql
-- <app.py>

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# flask app 에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#'SQLALCHEMY_TRACK_MODIFICATIONS'] = True가 기본값인데 sqlalchemy 데이터베이스 객체 수정 및
# 신호 방출 등을 추적합니다. 과도한 메모리를 사용하기 때문에 False

#sqlalchemy 초기화
db = SQLAlchemy(app)

migrate = Migrate(app, db)
```

```sql
-- <app.py> 위의 환경설정 아래에 계속 작성
# 클래스 만들고, id, username, email column을 만든 것
# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User '{self.username}'>"
```

```sql
(flask-venv) hyunkyeng:~/workspace/orm $ flask db init
(flask-venv) hyunkyeng:~/workspace/orm $ flask db migrate
(flask-venv) hyunkyeng:~/workspace/orm $ flask db upgrade
```





```sql
(flask-venv) hyunkyeng:~/workspace/orm $ python
>>> from app import *
>>> user = User(username='hyunkyeng', email='hyunk4593@gmail.com')
>>> db.session.add(user)
>>> db.session.commit()
>>> user.username
'hyunkyeng'
>>> user.email
'hyunk4593@gmail.com'
>>> users = User.query.all()
>>> users
[<User 'hyunkyeng'>]
```



#### # sql과 orm비교

```sql
--CREATE
INSERT INTO users (username, email) Value ('hyunkyeng', 'hyunk4593@gamil.com');
user = User(username='hyunkyeng', email='hyunk4593@gmail.com') 


--READ
SELECT * FROM users;
users = User.query.all()

--None
miss = USer.query.filter_by(username='ssafy').first()

--Get one by id
--primary key만 GET으로 가져올 수 있음.
SELECT * FROM users WHERE id=1;
user = User.query.get(1)

--Like
users = User.query.filter(User.email.like('%hyun%')).all()
users = User.query.limit(1).offset(2).all()


--UPDATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username

--DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()

```

------------------

오늘의 할일

- CREATE -> READ -> DELETE -> UPDATE(기존의 값을 불러온 다음에 새로운 값을 넣고 이걸 다시 넣어줘야한다.)