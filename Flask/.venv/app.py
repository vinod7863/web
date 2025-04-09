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
# app.secret_key = 'your_secret_key'  # Required for flashing messages

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
#     password_hash = db.Column(db.String(200), nullable=False)

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
#             session['user_id'] = user.id
#             session['username'] = user.username
#             flash('Login successful!', 'success')
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid credentials, please try again.', 'danger')
#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         return f"Welcome, {session['username']}!"
#     return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     session.clear()
#     flash('Logged out successfully.', 'info')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
