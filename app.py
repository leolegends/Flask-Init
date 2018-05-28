from flask import Flask

app = Flask(__name__)

@app.route('/<string:name>/<int:age>', methods=['GET'])
def main(name, age):
	return 'hello %s and my age %s' % (name, age), 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
