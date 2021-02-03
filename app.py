import os
import uuid
from process import generate_messages

from flask import Flask, render_template, request, send_from_directory, redirect, url_for, Response, send_file, abort, \
    flash
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'csv'}
UPLOADED_FILES = os.path.join('static', 'uploaded-files')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOADED_FILES
app.secret_key = os.getenv('SECRET_KEY')

# Check for valid file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    # return f"{uuid.uuid4()}"
    return render_template('index.html')

@app.route('/messages', methods = ['POST'])
def messages():
    #  grabbing the details submitted via form
    candidate_name = request.form['candidate_name']
    resume_link = request.form['resume_link']
    uploaded_file = request.files['file']

    if uploaded_file.filename !='':
        if allowed_file(uploaded_file.filename):
            #  avoid any security issues regarding file name
            uploaded_file_name = secure_filename(uploaded_file.filename)
            uploaded_file_name = f"{candidate_name}-{uuid.uuid4()}-{uploaded_file_name}"
            uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file_name)

            #  saving the uploaded image in the static/uploaded-images-folder
            uploaded_file.save(uploaded_file_path)

            #  process the uploaded csv file
            generated_file_name = generate_messages(file_path = uploaded_file_path, candidate_name = candidate_name, resume_link = resume_link)
            return redirect(url_for('get_file', file_name = generated_file_name))

        # if a non-csv file is uploaded
        else:
            flash("Not a csv file")
    return redirect(url_for('index'))


@app.route("/get-file/<file_name>")
def get_file(file_name):
    try:
        return send_from_directory(app.root_path, filename = file_name, as_attachment = True, cache_timeout = 0)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(port = 8000)