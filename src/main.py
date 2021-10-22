from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Tutorial 6 by Joyce Ejumu (EJMJOY001) and Samoei Oloo (OLXSAM001)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
