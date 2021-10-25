from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return 'Hello World: ECS Standard'

# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     # print(url_for('static', filename='bank_icon.ico'))
#     return render_template('index.html', name=username, post_id=post_id)

@app.route("/about.html")
def about():
    return render_template('About.html')

@app.route("/blog")
def blog():
    return "<p>This is my first blog</p>"

@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my Dog</p>"