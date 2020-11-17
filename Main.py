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

print(users)

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")
 
@app.route("/login", methods=["POST", "GET"])
def login():
	return render_template("login.html")

@app.route("/profile")
def user():
	return render_template("profile.html")
 
if __name__ == "__main__":
    app.run(debug=True)
