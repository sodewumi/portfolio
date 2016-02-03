import os

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

PORT = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=PORT)