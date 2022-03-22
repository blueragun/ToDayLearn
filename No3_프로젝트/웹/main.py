from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register')
def register(): 
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass

@app.route('/mainpage')
def mainpage(): 
    return render_template("mainpage.html")

## 이미지 업로드
@app.route('/fileUpload', methods = ['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/uploads/' + secure_filename(f.filename))
        files = os.listdir("static/uploads")
 
        conn = mysql.connect()
        cursor = conn.cursor()
        # 파일명과 파일경로를 데이터베이스에 저장함
        sql = "INSERT INTO images (image_name, image_dir) VALUES ('%s', '%s')" % (secure_filename(f.filename), 'uploads/'+secure_filename(f.filename))
        cursor.execute(sql)
        data = cursor.fetchall()
 
        if not data:
            conn.commit()
            return redirect(url_for("mainpage"))
 
        else:
            conn.rollback()
            return '업로드 실패'
 
        cursor.close()
        conn.close()

## 이미지 보기
@app.route('/view', methods = ['GET', 'POST'])
def view():
    conn = mysql.connect()  # DB와 연결
    cursor = conn.cursor()  # connection으로부터 cursor 생성 (데이터베이스의 Fetch 관리)
    sql = "SELECT image_name, image_dir FROM images"  # 실행할 SQL문
    cursor.execute(sql)  # 메소드로 전달해 명령문을 실행
    data = cursor.fetchall()  # 실행한 결과 데이터를 꺼냄
 
    data_list = []
 
    for obj in data:  # 튜플 안의 데이터를 하나씩 조회해서
        data_dic = {  # 딕셔너리 형태로
            # 요소들을 하나씩 넣음
            'name': obj[0],
            'dir': obj[1]
        }
        data_list.append(data_dic)  # 완성된 딕셔너리를 list에 넣음
 
    cursor.close()
    conn.close()
 
    return render_template('mainpage.html', data_list=data_list)  # html을 렌더하며 DB에서 받아온 값들을 넘김

@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
