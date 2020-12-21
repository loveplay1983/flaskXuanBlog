from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta


# Create Flask object
app = Flask(__name__)

# Configure Flask object and generate the SQLAlchemy object

# set up timer for cache clean
# https://www.cnblogs.com/zhenggaoxiong/p/9465440.html
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# app.send_file_max_age_default = timedelta(seconds=1)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# Database Model
class BlogPost(db.Model):
    """
    BlogPost is the Model part of MVC(model, view and control) structure
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # nullable - Same as 'NOT NULL' in SQL
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """
        %r is the Python “representation” for the object, a string which, 
        if presented to a Python in terpreter should be parsed as a literal 
        or as an instantiation of a new object of that time and with the same value. 
        The %r and %s for many objects is identical.
        """
        return 'Blog Post  %r' % str(self.id)


# # dummy data
# all_posts = [
#     {
#         'title': 'The Venus Project',
#         'content': 
#         """
#         I was asked once, 'you're a smart man,why aren't you rich?' 
#         I replied, 'you're a rich man, why aren't you smart?
#         """,
#         'author': 'Jacque Fresco'
#     },

#     {
#         'title': 'The Venus Project',
#         'content': 
#         """ 
#         There are no bad people, there are people with insufficient information 
#         **To** make appropriate decisions.
#         """,
#         'author': 'Jacque Fresco'
        
#     }
# ]



# index page
@app.route('/')
def index():
    return render_template('index.html')

# home page
# @app.route('/home')
@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return 'Hey Dear ' + name + ', your id is : ' + str(id) + '.' 

# error page
# @app.route('/onlyget', methods=['GET'])
@app.route('/onlyget', methods=['POST'])    
def get_req():
    return 'You can only get this webpage.'

# posts page
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    """
    Posts page with GET and POST
    you can view the posts and upload the new posts
    """
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['auth']

        # add now post
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
        
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

# delete posts
@app.route('/delete/<int:id>')
def delete(id):
    post_to_delete = BlogPost.query.get_or_404(id)

    

if __name__ == "__main__":
    app.run(debug=True)