from flask import Flask

app = Flask(__name__)

from api import mod
app.register_blueprint(mod, url_prefix='/api')

@app.route('/')
def home():
	return 'Home'

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')
