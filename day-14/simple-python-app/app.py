from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'ALHAMDULILLAH:) '

if __name__ == '__main__':
    app.run()

