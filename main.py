
# main.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_post', methods=['POST'])
def generate_post():
    brand_characteristics = request.form.to_dict()
    generated_post = generate_social_media_post(brand_characteristics)
    return render_template('posts.html', post=generated_post)

@app.route('/posts')
def show_posts():
    posts = get_social_media_posts()
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.run()
