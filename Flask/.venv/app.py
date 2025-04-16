# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"


# # routing
# from flask import Flask, render_template


# # Initialize Flask app
# app = Flask(__name__)

# @app.route('/')
# def home():
#     # return "Flask is working!"
#     return render_template('home.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')
    

# @app.route('/testpage')
# def testpage():
#     return render_template('testpage.html')

# @app.route('/result')
# def result():
#     return render_template('result.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# #varible routing
# from flask import Flask
# app = Flask(__name__)

# @app.route('/user/<name>')
# def user(name):
#     return f"Hello, {name}!"
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f"Post ID: {post_id}"

# #multiple routes
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# @app.route('/home')
# def home():
#     return "Welcome to the Home Page!"

# #redirect
# from flask import Flask, redirect, url_for
# app = Flask(__name__)
# @app.route('/')
# def home():
#      return redirect(url_for('login'))
# @app.route('/login')
# def login():
#     return "Login page"



# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/test')
# def test():
#     return render_template('test.html')

# @app.route('/result')
# def result():
#     return render_template('result.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Define the User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False, unique=True)
#     email = db.Column(db.String(120), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'

# # Route to display users and form
# @app.route('/')
# def index():
#     users = User.query.all()
#     return render_template('index.html', users=users)

# # Route to add a user
# @app.route('/add', methods=['POST'])
# def add_user():
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']

#     new_user = User(username=username, email=email, password=password)
#     db.session.add(new_user)
#     db.session.commit()

#     return redirect(url_for('index'))

# if __name__ == '__main__':
#         db.create_all()  # Create database tables
#         app.run(debug=True)



# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configure SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Define User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

#     def __repr__(self):
#         return f"<User {self.username}>"

# # Create database tables
# with app.app_context():
#     db.create_all()

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configure SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Define User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

#     def __repr__(self):
#         return f"<User {self.username}>"

# # Create database tables

# @app.route('/')
# def index():
#     return render_template('register.html')

# @app.route('/register', methods=['POST'])
# def register():
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']
    
#     new_user = User(username=username, email=email, password=password)
#     db.session.add(new_user)
#     db.session.commit()
    
#     flash('Registration successful!', 'success')  # Flash success message
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, flash, session
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configure SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Define User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

#     def __repr__(self):
#         return f"<User {self.username}>"

# # Create database tables
# @app.route('/')
# def index():
#     return render_template('register.html')

# @app.route('/register', methods=['POST'])
# def register():
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']
    
    
#     new_user = User(username=username, email=email, password=password)
#     db.session.add(new_user)
#     db.session.commit()
    
#     flash('Registration successful!', 'success')  # Flash success message
#     return redirect(url_for('index'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
        
#         if user and password(user.password, password):
#             flash('Login successful!', 'success')
#         else:
#             flash('Invalid credentials, please try again.', 'danger')
#     return render_template('login.html')


# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Ensure the database and tables are created
#     app.run(debug=True)


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import sqlite3

# app = Flask(__name__)

# # Database connection
# def get_db_connection():
#     conn = sqlite3.connect('users.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# # ------------------- Student Login -------------------
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         student = conn.execute('SELECT * FROM User WHERE username = ? AND password = ?', 
#                                (username, password)).fetchone()
#         conn.close()
#         if student:
#             session['student'] = username
#             return f"Welcome Student {username}!"
#         else:
#             flash("Invalid Student Credentials!")
#             return redirect(url_for('login'))
#     return render_template('login.html')


# # ------------------- Main Route -------------------
# @app.route('/')
# def index():
#     return "Welcome to the Login App!"

# if __name__ == '__main__':
#     app.run(debug=True)



# #session management
# from flask import Flask, session, redirect, url_for, request

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# @app.route('/')
# def home():
#     if 'username' in session:
#         return f"Hello {session['username']}!"
#     return "You are not logged in."

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('home'))
#     return '''
#         <form method="post">
#             <input type="text" name="username">
#             <input type="submit" value="Login">
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Define Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(500), nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    option4 = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "SQLite Database Connected!"

#insert data
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return "User registered successfully!"
    return render_template('register.html')
 
#login page for user
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return f"Welcome {user.username}!"
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

#retrieve the data from Question table
@app.route('/testpage', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return render_template('testpage.html', questions=questions)




if __name__ == '__main__':
    app.run(debug=True)


