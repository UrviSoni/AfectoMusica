from flask import Flask, render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login_data'

mysql = MySQL(app)

@app.route('/')
def index():
	return render_template('./index.html')

@app.route('/mood')
def mood():
	return render_template('./mood.html')

@app.route('/music')
def music():
	return render_template('./music.html')

@app.route('/contact')
def contact():
	return render_template('./contact.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('pwd')

		import hashlib
		h = hashlib.md5(password.encode())
		pwd = h.hexdigest()
		cur = mysql.connection.cursor()
		
		cur.execute("SELECT password from user where email like '"+email+"'")
		
		results = cur.fetchone()
		cur.close()
		if results[0] == pwd :
			return "sucess" 
		
		return "failed"

	return render_template('login.html')


@app.route('/signup',methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':

		name = request.form.get('author')
		email = request.form.get('email')
		password = request.form.get('pwd')
		import hashlib
		h = hashlib.md5(password.encode())
		
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO user(name, email, password) VALUES(%s, %s, %s)",(name, email, h.hexdigest()))
		mysql.connection.commit()
		cur.close()
		

		return 'sucess'

	return render_template('signup.html')

if __name__ == '__main__':
	app.run(debug = True)





