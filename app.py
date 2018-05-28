from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def main(name):
	return 'hello %s' % name, 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
