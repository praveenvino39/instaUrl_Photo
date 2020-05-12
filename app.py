from flask import Flask, jsonify
import instadownload as ig

app = Flask(__name__)

@app.route('/<path:url>')
def index(url):
    photo_url = {'photo_url': ig.main(url)}
    return jsonify(photo_url)

if __name__ == '__main__':
    app.run(debug=True)
