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
