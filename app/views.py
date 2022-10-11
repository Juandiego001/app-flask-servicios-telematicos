from app import app
from flask import render_template
from data import Articles

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/articles")
def articles():
    articles = Articles()
    return render_template("articles.html", articles=articles)

@app.route("/articles/<id>")
def the_article(id):
        articles = Articles()
        the_article = ""
        for article in articles:
                if int(id) == int(article['id']):
                        the_article = article
                        break

        return render_template("the_article.html", article=article)
