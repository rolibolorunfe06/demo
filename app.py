from flask import Flask,render_template
app=Flask(__name__)
@app.route("/index")
def hello():
	return render_template("index.html")
@app.route("/aboutus")
def hire():
	return render_template("aboutus.html")
if __name__=="__main__":
	app.run()


