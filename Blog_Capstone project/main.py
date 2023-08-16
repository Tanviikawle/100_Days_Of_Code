from flask import Flask,render_template,request
import requests
import smtplib
# from post import Post

url="https://api.npoint.io/f9f32f8b9c58c2870aa3"
posts=requests.get(url).json()
# print(response)

# OWN_EMAIL = YOUR OWN EMAIL ADDRESS
# OWN_PASSWORD = YOUR EMAIL ADDRESS PASSWORD


app = Flask(__name__)

@app.route('/index.html')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# @app.route('/form-entry',methods=["POST"])
# def receive_data():
#     data = request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phone"])
#     print(data["message"])
#     return "<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True)