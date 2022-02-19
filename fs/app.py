from flask import Flask, send_from_directory, request, redirect
import os

UPLOAD_FOLDER = '/videos'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/videos/<filename>')
def get_video(filename):
    try:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename
        )
    except:
        return ''


@app.route('/uploads', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'Success'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
