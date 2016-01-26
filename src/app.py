from flask import Flask, render_template
from api import mod

app = Flask(__name__)
app.register_blueprint(mod, url_prefix='/api')

# home / index
@app.route("/")
def index():
    return render_template('home.html', title="Home")

@app.route("/home")
def home():
    return render_template('home.html', title="Home")

# about
@app.route("/about")
def about():
    return render_template('aboutus.html', title="About")

# contact us
@app.route("/contact")
def contact():
    return render_template('contactus.html', title="Contact Us")

@app.route("/contacted", methods=["POST"])
def contacted():
	return render_template('contacted.html', title="Contacted")

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')
