import astropy.coordinates as coord
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "test"

if __name__ == '__main__':
    app.run()
