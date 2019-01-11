# 08Workshop
# Flask
#구미캠퍼스 1반 조영현
#190111

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/python')
def python():
    return 'Python is fun!'

@app.route('/dictionary/<string:word>')
def dictionary(word):
    d={'apple':'사과','banana':'바나나','pear':'배','watermelon':'수박'}
    result=d.get(word,'나만의 단어장에 없는 단어입니다!')
    return f'{word}은(는) {result}!'