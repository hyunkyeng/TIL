from flask import Flask, render_template, request, redirect
import os
import datetime
import requests  #pip install requests
import csv
from bs4 import BeautifulSoup   #bash 창에 pip install bs4

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'
    
#5월 20일부터 D-day 카운트 출력
@app.route('/dday')
def dday():
    start_time = datetime.datetime(2019, 5, 20)
    how_long = start_time - datetime.datetime.now()
    
    
    return f'D - {how_long.days}'

#조건문 사용 
#variable routing (주소창에 /hi/이현경   이라고 친다.)
@app.route('/hi/<string:name>')
def greeting(name):
    # return f'안녕, {name}'
    
    # greeting.html 로 위처럼 안녕 누구누구를 출력
    return render_template("greeting.html", html_name=name)
    
    
    
@app.route('/cube/<int:num>')
def cube(num):
    return f'{num**3}'
    
#반복문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)
    
    
# fake google
@app.route('/google')
def google():
    return render_template('google.html')
    
    
# 핑퐁    
@app.route('/ping')
def ping():
    return render_template('ping.html')
    
@app.route('/pong')
def pong():
    #name = request.args['name']   #이거를 써도 되지만 에러가 나올 수 있다. 
    name = request.args.get('name')    #하지만 get은 에러가 안나고 값이 없으면 none 값을 리턴한다. 
    msg = request.args.get('msg')
    return render_template('pong.html', pong_name=name, msg=msg)


#이제까지 GET방식을 사용한것. GET방식 : url에 우리가 검색한게 나온다.
#POST방식 : url에 우리가 검새한것을 숨긴다.

@app.route("/ping_new")
def ping_new():
    return render_template('ping_new.html')

@app.route("/pong_new", methods=['POST'])
def pong_new():
    # name = request.form['name']
    name = request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)


@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
    
@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')    #'username' 받아온걸 username에 저장
    response = requests.get(url+username).text    #받아온 username 을 url뒤에 붙인다. 
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)


#CSV - timeline.csv 만들기 (csv파일에서 띄어쓰기 쓰면 안된다.)
#username과 message를 timeline에서 받아서 create에서 출력
@app.route('/timeline')
def timeline():
    #지금까지 기록되어있는 방명록들을 보여주기
    L = []
    with open('timeline.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            L.append(row)
        
    return render_template('timeline.html', L=L)

@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    # w : 덮어쓰기, a: append 덮어쓰기, newline='' : 다음줄에 추가
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writerow({
            'username': username, 'message': message
        })
     
    return redirect('/timeline')   
    # redirect : 이페이지를 처리하고 /timeline 로 돌아간다. (import redirect 해야한다.)
    #return render_template('timeline_create.html', username=username, message=message)






if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)