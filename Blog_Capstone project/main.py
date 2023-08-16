from flask import Flask,render_template
import requests
# from post import Post

url="https://api.npoint.io/f9f32f8b9c58c2870aa3"
posts=requests.get(url).json()
# print(response)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# def get_post(id):
#     return render_template('post.html', current_year=c_year, today=today, all_blogs=blog_posts, num=id)

if __name__ == "__main__":
    app.run(debug=True)