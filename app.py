import astropy.coordinates as coord

app = Flask(__name__)

@app.route('/')
def home():
    return "test"

if __name__ == '__main__':
    app.run()
