from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath





app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER





# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    files = os.listdir('./files')
    print(files)
    return render_template('index.html', files=files)


# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file
      return redirect(url_for('index'))


@app.route('/files/')
def getFiles():
     # Set The upload HTML template '\templates\index.html'
    filenames = os.listdir('./files')
    print(filenames)
    return render_template('index.html', files=filenames)

# if (__name__ == "__main__"):
#      app.run(port = 5000)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5055, host='0.0.0.0')
