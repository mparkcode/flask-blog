from flask import Flask, render_template
import os
app = Flask(__name__)

posts = [
    {
        'author': 'Michael Park',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 20, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 21, 2018'
    },
    {
        'author': 'Jane Blogs',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'June 18, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)
    
@app.route("/about")
def about():
    return render_template("about.html", title="About")
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)