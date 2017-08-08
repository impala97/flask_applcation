
#import required lib
from flask import Flask,render_template,url_for

#create a instance of our web application to
app = Flask(__name__)

#now whenever the client reach this url python server will call index() function.
@app.route('/')
def index():
    return render_template('client/index.html')

#this will use to start our local server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
