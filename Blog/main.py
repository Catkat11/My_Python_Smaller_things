from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    for post in posts:
        if post["id"] == index:
            return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
