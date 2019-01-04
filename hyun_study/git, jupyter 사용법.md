

- git 에 올리면 안되는 파일이 있을 때

1. `touch .gitignore`
2. ls -al 로 확인하면 .gitignore이 생김
3. ` echo "test.txt" >> .gitignore`
4. ` cat .gitignore`
5. `vi .gitignore`
6.  vim 에 들어가짐
7. i 누르면 insert모드 esc누르면 command모드
8. :wq누르면 나가짐



- git bash 에 jupyter notebook 을 jp로 불러올 때

1. `vi ~/.bash_`    +tab+tab

2. ` vi ~/.bash_profile`    +enter

3. insert 모드에서 alias jp="jupyter notebook" 입력후 command모드에서 :wq 입력

4. ` source ~/.bash_profile`
