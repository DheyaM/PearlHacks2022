import pymongo

# https://www.fullstackpython.com/flask-helpers-make-response-examples.html
from flask import Flask, render_template,  request, jsonify, make_response, session, flash, redirect
from flask_pymongo import PyMongo
import os

app = Flask(__name__, static_url_path='')

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}


@app.route('/')
def index():
    return render_template("Main.html")


@app.route('/login')
def login():
    return render_template("Login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/additional')
def additional():
    return jsonify(message="under construction")


@app.route('/translate')
def translate():
    return render_template("translate.html")


@app.route('/processUpload', methods=['POST'])
def processingUpload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('init'))

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename

        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('init'))

        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            print(file.filename)

        #     processResume(user, file.filename)

        #     location = "./static/" + file.filename

        #     user['location'] = location

        #     # applicants.insert_one(user)

        # return render_template('displayPage.html', location=location), 200
        else:
            flash(f"{file.filename.split('.')[1]} is not allowed")
            return redirect(url_for('init'))


def allowed_file(filename):
    print(filename.split('.', 1))
    return '.' in filename and \
           filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
