"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask
from flask import request
from flask import Blueprint
from flask import render_template

# from views.items import items_app
# from views.products import products_app

app = Flask(__name__)


@app.get("/")
def index_page():
    return render_template("index.html", textos="Its Home page")


@app.get("/about/")
def about_path():
    return render_template("about.html", textos="It's about page")


if __name__ == "__main__":
    app.run(debug=True)