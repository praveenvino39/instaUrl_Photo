from flask import Flask, jsonify
import instadownload as ig

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'It works'


@app.route('/<path:url>')
def index(url):
    #photo_url = {'photo_url': ig.main(url)}
    return jsonify(url)

if __name__ == '__main__':
    app.run()
