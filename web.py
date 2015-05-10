from flask import Flask
app = Flask(__name__)

@app.route('/')
def potato():
    return 'Go eat potato!'

if __name__ == "__main__":
    app.run()
