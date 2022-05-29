from flask import Flask,render_template,request
import os
import webbrowser
from detection import detection1

app = Flask(__name__)
app.config['TESTING'] = True
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True

# Declaring the main page
@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        detection1()
        return render_template("index.html")
    else:
        return render_template("index.html")

#Running top-level code
def main():
    
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    # Otherwise, continue as normal
    app.run()

if __name__ == '__main__':
    main()

    
