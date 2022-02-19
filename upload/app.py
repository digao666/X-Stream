import os
from flask import Flask, flash, request, redirect, url_for, session, render_template
from werkzeug.utils import secure_filename
import requests
import uuid
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


UPLOAD_DEST = 'http://3495_project1_fs_1:5000/uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
AUTH_TOKEN_KEY = 'auth_token'

app.config['UPLOAD_DEST'] = UPLOAD_DEST
config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'assets'
}


def is_logged_in():
    return True if AUTH_TOKEN_KEY in session else False


def save_metadata_to_db(id, name, path):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO videos (id, name, path) VALUES ('{id}', '{name}', '{path}')")
    connection.commit()
    cursor.close()
    connection.close()
    return True


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if not is_logged_in():
        return redirect('http://localhost/auth/google/login')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            video_id = ''.join(str(uuid.uuid4()).split('-'))
            filename = secure_filename(file.filename)
            filepath = video_id+filename
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            # r = requests.post(app.config['UPLOAD_DEST'], files={
            #                   'file': (filename, open(filename, 'rb'))})
            r = requests.post(app.config['UPLOAD_DEST'], files={
                              'file': (filepath, file)})

            if save_metadata_to_db(video_id, filename, filepath):
                flash(
                    f"Your file has been successfully uploaded. Your file ID is {video_id}")
            # return f'{r.status_code}'
            return redirect('http://localhost')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
