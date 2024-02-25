from flask import Flask, flash, redirect, render_template, request, url_for
from db import EngineDB
from facade import PostFacade


app = Flask(__name__)
app.config['SECRET_KEY'] = '****'
engine_db = EngineDB()
posts_facade = PostFacade(engine_db=engine_db)


@app.route('/')
def index():
    post_data = posts_facade.get_all_posts()
    return render_template('index.html', posts=post_data)


@app.route('/create-post', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title or not content:
            flash('Title and Content are both required!')
        else:
            posts_facade.create_post(title=title, content=content)
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    post_data = posts_facade.get_post(post_id)
    return render_template('post.html', post=post_data)


@app.route('/<int:post_id>/edit', methods=['POST', 'GET'])
def edit(post_id):
    post_data = posts_facade.get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and Content are both required!')
        else:
            posts_facade.update_post(title=title, content=content)
            return redirect(url_for('index'))
    return render_template('edit.html', post=post_data)


@app.route('/<int:post_id>/delete', methods=['POST'])
def delete(post_id):
    posts_facade.delete_post(post_id)
    return redirect(url_for('index'))

app.run(debug=True)

