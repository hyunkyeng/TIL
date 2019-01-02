

- git 에 올리면 안되는 파일이 있을 때

1. `touch .gitignore`
2. ls -al 로 확인하면 .gitignore이 생김
3. ` echo "test.txt" >> .gitignore`
4. ` cat .gitignore`
5. `vi .gitignore`
6.  vim 에 들어가짐
7. i 누르면 insert모드 esc누르면 command모드
8. :wq누르면 나가짐



## <jupyter 설치>

1. ` cd`
2. ` pip install jupyter`
3. `cd Desktop/TIL/python/`
4. `jupyter notebook`



## <jupyter 사용법>

> command  모드에서 

- shift enter : 실행하고 다음셀로 넘어간다. 

- ctrl enter : 실행만

- alt enter : 실행하고 새로운 셀을 만든다.

- a : 위에 새로운 셀 만들기

- b : 아래에 새로운 셀 만들기

- dd : 셀 지우기