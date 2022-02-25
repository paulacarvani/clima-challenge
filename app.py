from flask import Flask
from flask import render_template, request, url_for
from flask_mysqldb import MySQL

from api import getInfo, getNews, render


app = Flask(__name__)

# Connection MySQL
mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'clima-challenge'
cur = mysql.connection.cursor()

# Start Connection MySQL
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/home', methods=['POST'])
def Search():
    city = request.form['city'] or None
    if city is not None:
        DictCity = getInfo(city)
        DictCity['MoreData'] = render(DictCity)

        DictNews = getNews(city)
        return render_template('index.html',
                               DictCity=DictCity,
                               DictNews=DictNews)
    return render_template('home.html')


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')


@app.route("/login", methods=['POST'])
def login_admin():
    check_user = request.form['user']
    if check_user == 'admin':
        user = request.form['name']
        password = request.form['password']

        return render_template('boards.html', check_user=check_user)
    elif check_user == 'guest':
        return render_template('boards.html', check_user=check_user)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
