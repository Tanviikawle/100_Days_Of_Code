from flask import Flask,render_template
import requests

# response_1=requests.get("")
# response_2=requests.get("")

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello !"

@app.route("/guess/<name>")
def guess(name):
    gender_url=f"https://api.genderize.io?name={name}"
    age_url=f"https://api.agify.io?name={name}"
    res_1=requests.get(gender_url)
    res1_data=res_1.json()
    gender=res1_data["gender"]
    res_2=requests.get(age_url)
    res2_data=res_2.json()
    age=res2_data["age"]
    return render_template("index.html",name=name.title(),age=age,gender=gender)

@app.route("/blog")
def blog():
    return "This is blog page."

if(__name__)=="__main__":
    app.run(debug=True)