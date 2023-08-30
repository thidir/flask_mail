from flask import Flask

app = Flask(__name__)

@app.route('/mail')
def index():
    return 'send mail'
 
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')