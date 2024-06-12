# Python (Flask)
from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Assuming 'mobdatabase' is a directory with .wav files
    files = os.listdir('mobdatabase')
    selected_file = random.choice(files)
    return render_template('index.html', music_file=selected_file)

if __name__ == '__main__':
    app.run(debug=True)
