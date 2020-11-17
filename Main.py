from flask import Flask, redirect, url_for, render_template, request, session
 
class User:
	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password
	
	def __repr__(self):
		return f"<user: {self.username}>"
	
users = []
users.append(User(id=1, username = "ollie", password = "password"))
users.append(User(id=2, username = "ro", password = "secret"))

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")
 
@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.pop("user_id", None)
		username = request.form["username"]
		password = request.form["password"]
		
		user = [x for x in users if x.username == username][0]
		if user and user.password == password:
			session["user_id"] = user.id
			return redirect(url_for("profile"))
		
		return redirect(url_for("login"))
	
	return render_template("login.html")

@app.route("/profile")
def user():
	return render_template("profile.html")
 
if __name__ == "__main__":
    app.run(debug=True)
