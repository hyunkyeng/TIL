import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Movie


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/movies/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
    
@app.route('/movies/new/')
def new():
    return render_template('new.html')
    
@app.route('/movies/create/')
def create():
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('index'))
    
# 영화정보조회(show)
@app.route('/movies/<int:id>/')
def show(id):
    movie = Movie.query.get(id)
    return render_template('show.html', movie=movie)
    
# 영화정보수정Form(edit)
@app.route('/movies/<int:id>/edit/')
def edit(id):
    movie = Movie.query.get(id)
    return render_template('edit.html', movie=movie)
    
# 영화정보수정(update)
@app.route('/movies/<int:id>/update/')
def update(id):
    movie = Movie.query.get(id)
    
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie.title = title
    movie.title_en = title_en
    movie.audience = audience
    movie.open_date = open_date
    movie.genre = genre
    movie.watch_grade = watch_grade
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    
    db.session.commit()
    
    return redirect(f'/movies/{id}/')
    
# 영화정보삭제(delete)
@app.route('/movies/<int:id>/delete/')
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    
    return redirect(url_for('index'))
        

    









if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port=os.getenv('PORT'), debug=True)
