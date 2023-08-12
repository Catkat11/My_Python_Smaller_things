from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/0d12765d7a5f66bfc61f").json()

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    chosen_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            chosen_post = blog_post
    return render_template("post.html", post=chosen_post)


if __name__ == "__main__":
    app.run(debug=True)
