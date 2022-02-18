from flask import Flask
from flask import render_template, request

from api import getInfo, getNews, render


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/home', methods=['POST'])
def Search():
    if request.form['city'] is not '':
        city = request.form['city']
        DictCity = getInfo(city)
        DictCity['MoreData'] = render(DictCity)

        DictNews = getNews(city)
        return render_template('index.html',
                               DictCity=DictCity,
                               DictNews=DictNews)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
