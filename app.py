from flask import Flask
from flask import render_template, request, url_for, redirect, g, session
# from flaskext.mysql import MySQL

from api import getInfo, getNews, render
from models.functions import CheckUser, CheckPassword

app = Flask(__name__)

# # Connection MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'clima-challenge'

# # Start Connection MySQL
# mysql = MySQL()
# mysql.init_app(app)
# cur = mysql.connect().cursor()

# Check User Session
app.secret_key = 'EsoEst@do'
username = ''
user = CheckUser()


@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        g.user = ['username']
        return render_template('admin.html', message='HELLO ADMIN!')
    else:
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


@app.route("/login", methods=['POST', 'GET'])
def login_admin():
    if request.method == 'POST':
        session.pop('username', None)
        areyouser = request.form['username']
        pwd = CheckPassword(areyouser)

        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    # check_user = request.form['user']
    # if check_user == 'admin':
    #     user = request.form['name']
    #     password = request.form['password']

    #     return render_template('boards.html', check_user=check_user)
    # elif check_user == 'guest':
    #     return render_template('boards.html', check_user=check_user)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
