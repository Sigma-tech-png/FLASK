from flask import Flask,request,render_template,redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_url = os.environ.get("MONGO_URL")
client = MongoClient(mongo_url)
db = client["Data"]
users = db["users"]
print("MongoDB Connected...")

#---------------------------------------------

@app.route("/", methods=["GET","POST"])
def Home():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        users.insert_one(
            {
                "name":name,
                "age":age,
            }
        )
        return redirect('/save')

    return render_template("home.html")

@app.route("/save")
def Save():
    return "Saved"

if __name__ == "__main__":
    app.run(debug=True)