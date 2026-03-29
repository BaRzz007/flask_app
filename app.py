from flask import Flask, flash, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = "simple_secret_key"
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))


mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Invalid Username and Password")
            return redirect(url_for("signup"))

        hashed_password = generate_password_hash(password)

        cursor = mysql.connection.cursor()

        query = """
        INSERT INTO tbl_user (username, password)
        VALUES (%s, %s)
        """ #in a real app, this can be better using ORM

        cursor.execute(query, (username, hashed_password))
        mysql.connection.commit()
        cursor.close()

        flash("Account created successfuly")
        return redirect(url_for("home"))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
