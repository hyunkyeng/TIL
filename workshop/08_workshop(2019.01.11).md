08_workshop(2019.01.11)



app.py

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    word_dict = {"apple": "사과", "banana": "바나나"}
    return render_template('word.html', word = word, word_dict = word_dict)
```

word.html

```python
{% if word in word_dict %}
    <h1>{{ word}} 는 {{ word_dict[word] }} 입니다.</h1>
{% else %}
    <h3>{{ word }} 는 없는 단어입니다. </h3>
{% endif %}
```



