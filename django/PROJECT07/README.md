07 Django - 데이터베이스 설계

1. 목표 
 - 데이터를 생성 조회, 삭제, 수정할 수 있는 Web Application 제작
 - 데이터베이스 데이블간 관계 설정 (1:N)

2. Tree

├── README.md
├── crud
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── genre.csv
├── manage.py
├── movie.csv
└── movies
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── admin.cpython-36.pyc
    │   ├── apps.cpython-36.pyc
    │   ├── models.cpython-36.pyc
    │   ├── urls.cpython-36.pyc
    │   └── views.cpython-36.pyc
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-36.pyc
    │       └── __init__.cpython-36.pyc
    ├── models.py
    ├── templates
    │   └── movies
    │       ├── base.html
    │       ├── detail.html
    │       └── index.html
    ├── tests.py
    ├── urls.py
    └── views.py