### < C9, Bash 사용방법 >



- echo 는 뒤에 있는 것을 출력해준다. 

```python
hyunkyeng:~/workspace $ echo hello
hello
hyunkyeng:~/workspace $ echo 'hello'
hello
hyunkyeng:~/workspace $ echo "hello"
hello
```

- '' 은 문자열 출력만해주고 "" 은 선언된 문자열을 출력해준다.

```python
hyunkyeng:~/workspace $ MYVAR=sometext
hyunkyeng:~/workspace $ echo 'single $MYVAR'
single $MYVAR
hyunkyeng:~/workspace $ echo "double $MYVAR"
double sometext
hyunkyeng:~/workspace $ echo "i'm double"
i'm double
hyunkyeng:~/workspace $ echo 'i'm single'
> ^C   # '' 안에 ' 는 출력이 안된다. 따라서 ctrl + C 를 눌러서 나온다. 
```

- ### ctrl + a 누르면 커서가 맨 앞으로 이동한다. 

- ### ctrl + e 누르면 커서가 맨 뒤로 이동한다. 

- ### 줄 전체삭제 : ctrl + u

- 이전명령어는 화살표 위, 아래로 이동한다. 

- 현재 커서 기준으로 

- 명령어 설명볼 때는 man 을 쓰면된다.  설명에서 나갈 때는 Q누른다.

```python
hyunkyeng:~/workspace $ man
What manual page do you want?
hyunkyeng:~/workspace $ man echo
```

- 현재 커서가 위치한 단어를 지울 때 : ctrl + w

- ### ctrl + L : 커맨드 깨끗하게

- 메모장를 만들면서 메모를 남기고 싶을때 : echo "Someone Like You" > adele.txt

- 만들어진 메모장에 메모를 남기고 싶을때 : hyunkyeng:~/workspace $ echo "Rolling in the Deep" >> adele.txt

- cat 은 command 창에서 메모장 내용을 보여준다. 

```python
hyunkyeng:~/workspace $ cat adele.txt
Someone Like You
```



- 유사한 두가지 파일을 비교할때는 diff

```python
hyunkyeng:~/workspace $ diff adele.txt adele_2.txt
2c2
< Rolling in the Deep
---
> rolling in the deep
```

- line.txt 에 있던 내용을 song.txt를 만들면서 내용을 복사하고 싶으면 : cat line.txt > song.txt

- song_reverse.txt 를 만들면서 line_2.txt에 있는 내용 먼저, line.txt 에 있는 내용을 추가하려면 :  cat line_2.txt line.txt > song_reverse.txt

- ls : 현재 무슨 파일들이 있는지 보여준다. 
- ls *.txt : 확장자가 txt인 파일들만 보여준다. 

- ls s*.txt : 확장자가 s 로 시작하면서 txt인 파일들을 보여준다. 
- ls -l : 롱포멧으로 파일을 보여준다. 

- ls -a : 숨긴파일도 나온다. 
- ls -al : 롱포멧으로 숨긴파일까지 보여준다.
- ls -r : 최근 순으로 파일이 나온다. 

- ls -rl : 최근 순으로 롱포멧으로 보여준다. 

> 조합이 가능 ( 위에 다 조합한 것)

- ls a* : a로 시작하는 확장자 상관없이 모든파일을 보여준다. 
- 파일명에 "el" 문자열이 포함된 모든 파일 및 디렉토리를 파일이 변경된 시간의 역순으로 정렬해서 longformat으로 보는 명령어 : ls -rl *el*

- test 라는 파일명을 test test_file.txt 로 이름변경 :  mv test test_file.txt

- 같은 파일을 복사해서 만들려면 : cp test_file.txt copy_file.txt
- 파일 지울때  : rm copy_file.txt 

- 파일 지울 때 한번 더 확인 :  rm -i test_file.txt 
- - -> y, Y를 써야만 지워진다.

- 폴더 만들기 : mkdir cli_test
- 한번에 여러개의 파일 만들기 : touch a.txt b.txt c.txt d.txt e.txt

- 한번에 모든 txt파일 지울때 : rm *.txt

- curl 이 설치되어있는지 확인 : which curl

- 파일을 복사해 올 때  : curl -OL edujunho.github.io/files/sonnets.txt

> -O :  원본파일을 그대로 쓰겠다. 
>
> -L : 원본주소가 잘못되었을 때 서브 주소에서 받아 오겠다. 

- 용량 보는 것 : ls -lh
- 파일이 큰경우 앞에 10 줄만 보는 것 : head sonnets.txt
- 파일이 큰경우 뒤에 10 줄만 보는 것 : tail sonnets.txt
- 파일이 몇 줄 , 몇 단어, 몇 바이트 인지 보는 것 : wc sonnets.txt

--------------

### # 심화 ( | 사용)



- head sonnets.txt 를 몇 줄, 몇 단어, 몇 바이트인지 보는 것 : head sonnets.txt | wc

- >  좌측의 출력을 오른쪽의 입력으로 보내는것 !!

- tail sonnets.txt 를 몇 줄, 몇 단어, 몇 바이트인지 보는 것 : tail sonnets.txt | wc

- 앞부분의 10줄이 아니라 13줄만 보이게 하는 것 : head -13 sonnets.txt /  head -n 13 sonnets.txt 

- sonnet의 챕터 1만을 보여주되, 챕터 1의 뒤에서 14줄 만을 출력 : head -18 sonnets.txt | tail -14

- less sonnets.txt : cat보다 더 잘보여주는 것. 터미널에 전체파일 내용을 보여준다. 

  - /찾고싶은 단어 : 단어를 찾아준다 -> enter 로 이동

  - 숫자g : 가고싶은 줄의 숫자를 입력하면 가고싶은 줄로 이동

  - shiftg : 마지막 줄로 이동

  - 한페이지 아래로 : f / 한페이지 위로 : b

  - 반페이지 아래로 : d / 반페이지 위로 : u

  - less창에서 나가기 : q


- grep All sonnets.txt : All 이 포함된 모든 문장을 출력
- grep All sonnets.txt | wc : All 이 몇번 등장하는지 알 수 있다.  ->  10      86     462 출력 -> 10번 등장
- grep -i rose sonnets.txt : 대소문자 구분없이 모든 rose가 들어간 문장을 출력
- ps aux : 전체 프로세스 확인
- ps aux | grep ubuntu : 실행중인 서버 중에서 우분투만 출력
- top : PID순으로 프로세스 정렬
- 강제 종료 명령어 : kill -15 1903 (1903 : 강제로 종료 하고 싶은 프로세스의 PID)
- pkill -15 ubuntu : ubuntu 인 애들을 전부 강제 종료



Q1. grep 매뉴얼에서 line number 를 검색하고 sonnets 에서 rose 문자열이 등장하는 줄의 번호를 출력하시오.

```python
hyunkyeng:~/workspace $ grep -n rose sonnets.txt
909:The rose looks fair, but fairer we it deem
912:As the perfumed tincture of the roses.
917:Die to themselves. Sweet roses do not so;
1135:Roses of shadow, since his rose is true?
1605:Which, like a canker in the fragrant rose,
1664:Nor praise the deep vermilion in the rose;
1679:The roses fearfully on thorns did stand,
1856:  Save thou, my rose, in it thou art my all.
2202:I have seen roses damask'd, red and white,
2203:But no such roses see I in her cheeks;
```



Q2. sonnet 에 등장하는 첫번째 rose 문장(그 줄의 번호가 포함된) 만을 출력하시오. 

```python
hyunkyeng:~/workspace $ grep -n rose sonnets.txt | head -1
909:The rose looks fair, but fairer we it deem
```



- history : 이제까지 입력한 명령어들이 나온다. 
- history | wc : 

```python
hyunkyeng:~/workspace $ history | wc
     55     237    1424
```

- history 상에서 man 을 몇번 썼는지 : history | grep -c man

```python
hyunkyeng:~/workspace $ history | grep -c man
11
```

- grep -c man : history 상에서 man 을 몇번 썼는지
- grep -n rose : rose 문자열이 등장하는 줄의 번호

- /경로 : 절대 경로 ( 경로는 웬만하면 / 쓰고 쓰는 것이 좋다. )
- 경로 : 상대 경로 

- ~ : 홈 디렉토리

- pwd : 숨겨진 경로를 알려줌  => /home/ubuntu == ~

```python
hyunkyeng:~ $ ls
lib/  workspace/
hyunkyeng:~ $ pwd
/home/ubuntu
```

> /home/ubuntu/workspace 랑 ~/workspace 은 같은 것.



- txt파일 전부를 text_files 폴더로 이동 : mv *.txt text_files/



Q1. 현재 존재하지 않는 dir1 디렉토리 안에 dir2 를 만들고자한다. 

각각 생성하는 것이 아닌 한번 명령으로 생성하는 옵션을 mkdir 매뉴얼에서 찾아 사용.

```python
hyunkyeng:~/workspace $ mkdir -p  dir1/dir2
```



Q2. 1에서 알아낸 명령으로 foo/bar/baz (foo 폴더 안에 bar 폴더 안에 baz 폴더) 를 만드시오.

```python
hyunkyeng:~/workspace $ mkdir -p foo/bar/baz
```



- text_files 폴더를 cli_test 폴더로 이동

```python
hyunkyeng:~/workspace $ mv text_files/ cli_test/
```

- 홈 디렉토리와 하위에 있는 txt파일을 전부 다 찾기 : find . -name '*.txt'

- cd - : 바로 이전에 작업한 디렉토리로 이동

-------

<여러개의 명령이 실행>

- ; 앞에 명령어가 실행이 안돼도 뒤에 명령어가 실행 : ./configure ; make ; make install (3개의 명령어 실행)
- && 앞에 명령어가 실행이 안되면 뒤에 명령어가 실행되지 않는다. : ./configure && make && make install (3개의 명령어 실행)
  - git 한번에 실행

```python
hyunkyeng:~/workspace/cli_test $ cd .. && git add . && git commit -m "Asdasd" && git push && cd - 
```

------



- 폴더 이름 바꾸기 : mv foo/ bar/

- 상위 폴더 text_files를 아예 복사하기 : cp -r ../text_files .
- 상위 폴더 text_files 안에 있는 내용물을  복사하기(  / 를 붙여야 한다.) : cp -r ../text_files/ .

- 폴더 지우기 : rm -rf second_dir/
- long_word.txt를 만들면서 sesquipedalian 단어 넣기 : echo sesquipedalian > long_word.txt

- 어디에 있던(r) 원하는 문장이 들어간 파일을 찾는 방법 : grep -r sesquipedalian text_files/
- 대소문자 구별 없이(i) 어디에 있던(r) 원하는 문장이 들어간 파일을 찾는 방법 :  grep -ri sesquipedalian text_files/



Q. 명령어 한줄로 만들기. 

1. foo 라는 dir 을 만든다. 

2. foo 로 현재 위치를 바꾼다. 
3.  "baz" 라는 내용이 들어간 bar.txt 파일을 생성
4.  bar.txt 내용 출력
5.  이전에 왔던 디렉토리 이동

```python
hyunkyeng:~/workspace/cli_test $ mkdir foo && cd foo && echo baz > bar.txt && cat bar.txt && cd -
```

