import functools
from typing import List, Dict
from flask import Flask, render_template, redirect, session
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
AUTH_TOKEN_KEY = 'auth_token'

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'assets'
}


def is_logged_in():
    return True if AUTH_TOKEN_KEY in session else False


def list_videos() -> List[Dict]:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM videos')
    results = [{id: [name, path]} for (id, name, path) in cursor]
    cursor.close()
    connection.close()

    return results


def find_video_path_from_db(id) -> str:
    videos = list_videos()
    filename = ''
    for video in videos:
        if id in video.keys():
            filename = video[id][1]

    return filename


@app.route('/')
def index():
    if not is_logged_in():
        return redirect('/auth/google/login')
    return render_template('index.html', videos=list_videos())

@app.route('/login')
def login():
    if not is_logged_in():
        return redirect('/auth/google/login')
    return render_template('index.html', videos=list_videos())


@app.route('/logout')
def logout():
    return redirect('/auth/google/logout')


@app.route('/video/<id>')
def video(id):
    if not is_logged_in():
        return redirect('/auth/google/login')
    filename = find_video_path_from_db(id)
    url = f'http://localhost:5001/videos/{filename}'
    return render_template('video.html', url=url)


@app.route('/upload')
def upload():
    return redirect('upload')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
