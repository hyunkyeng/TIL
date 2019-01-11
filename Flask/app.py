from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕하세요!!!'

@app.route('/html')
def html():
    return render_template('chicken.html')     #templates 안에 있는 것을 가져오는 것이므로 templates폴더를 만들어서 그안에  치킨사진을 넣는다. 
#chicken.html 페이지를 띄워주세요.

@app.route('/html_name/<string:name>')
def html_name(name):
    return render_template('chicken.html', your_name = name)


# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    word_dict = {"apple": "사과", "banana": "바나나"}
    return render_template('word.html', word = word, word_dict = word_dict)