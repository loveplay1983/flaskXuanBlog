from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta



# Create Flask object
app = Flask(__name__)

# Configure the Flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pgjdcwn040506@localhost/flask_study'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

db = SQLAlchemy(app)  # Create sqlalchemy object


# Create database object
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def init_tbl(obj):
        db.create_all()
        db.session.add(obj)
        db.session.commit()

    def __repr__(self):
        return '<Task   %r>' % self.id

person = Person('Admin')
Person.init_tbl(person)

# person = Person('admin')
# """
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
# To create the initial database, just import the db object from an interactive 
# Python shell and run the SQLAlcprimary_keyhemy.create_all() method to create the tables and database
# """
# db.create_all()      
# db.session.add(person)
# db.session.commit()  # write the change to database

## dummy data
all_posts = [
    {
        'title': 'The Venus Project',
        'content': 
        """
        I was asked once, 'you're a smart man,why aren't you rich?' 
        I replied, 'you're a rich man, why aren't you smart?
        """,
        'author': 'Jacque Fresco'
    },

    {
        'title': 'The Venus Project',
        'content': 
        """
        There are no bad people, there are people with insufficient information to make appropriate decisions.
        """
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

# @app.route('/home')
@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return 'Hey Dear ' + name + ', your id is : ' + str(id) + '.' 

# @app.route('/onlyget', methods=['GET'])
@app.route('/onlyget', methods=['POST'])    
def get_req():
    return 'You can only get this webpage.'

@app.route('/mysql_test')
def mysql_test():
    persons = Person.query.order_by(Person.id).all()
    return render_template('mysql.html', persons=persons)


if __name__ == "__main__":
    app.run(debug=True)