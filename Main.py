from flask import Flask, redirect, url_for, render_template, request
 
app = Flask(__name__)
 

	
@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "POST":
		if request.form.get("Signup"):
			return redirect(url_for("/signup")
		elif request.form.get("Login"):
			return redirect(url_for("/login")
	elif request.method == "GET":
			return render_template("index.html")

@app.route("/<user>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/signup")
def signup():
    return render_template("signup.html")
 
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
 
if __name__ == "__main__":
    app.run()
