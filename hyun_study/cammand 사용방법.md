



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