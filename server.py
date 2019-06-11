from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('restfulusers')
    myUsers = mysql.query_db('SELECT * FROM users;')
    print(myUsers)
    return render_template("index.html", users = myUsers)

@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
    data = {
        "fname" : request.form['first_name'],
        "lname" : request.form['last_name'],
        "email" : request.form['email_name']
    }
    db = connectToMySQL('restfulusers')
    db.query_db(query, data)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)