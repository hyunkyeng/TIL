

### <처음 git 설정할 때 >

- `git clone https://github.com/hyunkyeng/TIL.git `    # 내 github에 올라간 폴더 가져오기
- `$ git credential reject                                                         
  protocol=https                                                                  
  host=github.com                                                                 `    # 기존 사용자 정보 날리는 것. 

- cd TIL
- ` git push`  =  > 로그인 창 뜨는 곳에 로그인하기
- ` git config --global user.name 'hyunkyeng'`
- ` git config --global user.email hyunk4593@gmail.com`
- ` git config --global --list`           #유저네임, 이메일 확인
- ` git config --global color.ui true`      # git 명령어 색칠해주는 것. 



-----



### < 연수원과 집에서 git 같이 쓸 때 >

ㅊㅇ 연수원 : TIL git push

집 : git pull  => add commit push

연수원 :  git pull => add commit push

