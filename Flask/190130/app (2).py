from flask import Flask, render_template
import os
import datetime
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



    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)