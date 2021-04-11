from flask import Flask, render_template, request, flash, url_for, redirect, session
from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange
from wtforms.fields.html5 import EmailField
from wtforms import validators, ValidationError
import datetime
import pymysql


app = Flask(__name__)
app.secret_key = 'development'
db = pymysql.connect(host='localhost', user='localhost', password='root', database='205cde')

class RegisterForm0(Form):
	"""docstring for RegisterFormtest  (testing version)"""
	username = TextField("", [validators.DataRequired("Please enter your name."), validators.Length(min=4, max=20)])
	email = TextField("", [validators.DataRequired("Please enter your email."), validators.Email("Please enter your email."), validators.Length(min=8, max=50)])
	password = PasswordField("", [validators.DataRequired("Please enter your password."), validators.Length(min=3, max=20), validators.EqualTo('confirm', message="Password must match")])
	confirm = PasswordField("")

class RegisterForm(Form):
	"""docstring for RegisterForm"""
	username = TextField("", [validators.DataRequired("Please enter your name."), validators.Length(min=4, max=20)],
						render_kw={"placeholder": "Please enter your username..."})
	email = TextField("", [validators.DataRequired("Please enter your email."), validators.Email("Please enter your email."), validators.Length(min=8, max=50)],
						render_kw={"placeholder": "Please enter your email..."})
	password = PasswordField("", [validators.DataRequired("Please enter your password."), validators.Length(min=3, max=20), validators.EqualTo('confirm', message="Password must match")],
						render_kw={"placeholder": "Please enter your password..."})
	confirm = PasswordField("", render_kw={"placeholder": "Please enter your password again..."})
	address = TextField("", [validators.DataRequired("Please enter your address."), validators.Length(min=1, max=255)],
						render_kw={"placeholder": "Please enter your address..."})
	region = SelectField("", choices=[('Kowloon', 'Kowloon'), ('Hong Kong Island', 'Hong Kong Island'), ('New Territories', 'New Territories')])
	phoneNo = TextField("", [validators.DataRequired("Please enter your phone number."), validators.Length(min=8, max=8)],
						render_kw={"placeholder": "Please enter your phone number..."})

class LoginForm(Form):
	"""docstring for RegisterForm"""
	username = TextField("", [validators.Length(min=4, max=20)], render_kw={"placeholder": "Please enter your username..."})
	password = PasswordField("", [validators.DataRequired("Please enter your password."), validators.Length(min=3, max=20)], render_kw={"placeholder": "Please enter your password..."})

class UpdateUserInfoForm(Form):
	"""docstring for UpdateForm"""
	username = TextField("", [validators.DataRequired("Please enter your name."), validators.Length(min=4, max=20)],
						render_kw={"placeholder": "Please enter your username..."})
	email = TextField("", [validators.DataRequired("Please enter your email."), validators.Email("Please enter your email."), validators.Length(min=8, max=50)],
						render_kw={"placeholder": "Please enter your email..."})
	password = PasswordField("", [validators.DataRequired("Please enter your password."), validators.Length(min=3, max=20), validators.EqualTo('confirm', message="Password must match")],
						render_kw={"placeholder": "Please enter your password..."})
	confirm = PasswordField("", render_kw={"placeholder": "Please enter your password again..."})
	address = TextField("", [validators.DataRequired("Please enter your address."), validators.Length(min=1, max=255)],
						render_kw={"placeholder": "Please enter your address..."})
	region = SelectField("", choices=[('Kowloon', 'Kowloon'), ('Hong Kong Island', 'Hong Kong Island'), ('New Territories', 'New Territories')])
	phoneNo = TextField("", [validators.DataRequired("Please enter your phone number."), validators.Length(min=8, max=8)],
						render_kw={"placeholder": "Please enter your phone number..."})

class UploadProductInfoForm(Form):
	"""docstring for UploadProductInfoForm"""
	productname = TextField("", [validators.DataRequired("Please enter the name of the product..."), validators.Length(min=5, max=255)],
						render_kw={"placeholder": "Please enter the name of the product..."})
	price = IntegerField("", [validators.DataRequired("Please enter the price of the product...")],
						render_kw={"placeholder": "Please enter the price of the product..."})
	brand = TextField("", [validators.DataRequired("Please enter the brand of the product..."), validators.Length(min=5, max=50)],
						render_kw={"placeholder": "Please enter the brand of the product..."})
	detail = TextField("", [validators.DataRequired("Please enter the brand of the product..."), validators.Length(min=5, max=255)],
						render_kw={"placeholder": "Please enter the brand of the product..."})
	image = TextField("", [validators.DataRequired("Please enter the image of the product..."), validators.Length(min=5, max=50)],
						render_kw={"placeholder": "Please enter the image of the product..."})

class EditProductInfoForm(Form):
	"""docstring for UploadProductInfoForm"""
	productname = TextField("", [validators.DataRequired("Please enter the name of the product..."), validators.Length(min=5, max=255)],
						render_kw={"placeholder": "Please enter the name of the product..."})
	price = IntegerField("", [validators.DataRequired("Please enter the price of the product...")],
						render_kw={"placeholder": "Please enter the price of the product..."})
	brand = TextField("", [validators.DataRequired("Please enter the brand of the product..."), validators.Length(min=5, max=50)],
						render_kw={"placeholder": "Please enter the brand of the product..."})
	detail = TextField("", [validators.DataRequired("Please enter the brand of the product..."), validators.Length(min=5, max=255)],
						render_kw={"placeholder": "Please enter the brand of the product..."})
	image = TextField("", [validators.DataRequired("Please enter the image of the product..."), validators.Length(min=5, max=50)],
						render_kw={"placeholder": "Please enter the image of the product..."})

class QuestionForm(Form):
	question = TextField("", [validators.DataRequired("Please enter the question here..."), validators.Length(min=10, max=10000)],
						render_kw={"placeholder": "Please enter the question..."})

class ReplyForm(Form):
	reply = TextField("", [validators.DataRequired("Please enter the reply here..."), validators.Length(min=10, max=10000)],
						render_kw={"placeholder": "Please enter the reply..."})

@app.route("/")
def home():
	return render_template("home.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		username = form.username.data
		password = form.password.data
		custUname = None

		cursor = db.cursor()
		sql = ("SELECT username, userpassword, userid FROM user WHERE username = '"+username+"' ")
		cursor.execute(sql)

		db.commit()
		results = cursor.fetchall()

		for row in results:
			custUname = row[0]

		if custUname is None:
			flash('You have not registered!')
			return render_template("login.html")

		else:
			if username == row[0] and password == row[1]:
				if username == "admin":
					for row in results:
						custUname = row[0]
						custPassword = row[1]
						custuserid = row[2]
						session['admin'] = custUname
						session['adminid'] = custuserid

						flash('Logged in successfully!', 'success')
						return redirect(url_for('adminlogin'))

				else:
					for row in results:
						custUname = row[0]
						custPassword = row[1]
						custuserid = row[2]
						session['uname'] = custUname
						session['userid'] = custuserid

						flash('Logged in successfully!', 'success')
						return redirect(url_for('userlogin'))

			else:
				flash('Incorrect username/password!', 'danger')
				return redirect(url_for('login'))

	return render_template("login.html", form=form)

@app.route('/register_sample', methods=['POST', 'GET'])
def register_sample():
	form = RegisterForm0()
	if request.method == 'POST' and form.validate():
		username = form.username.data
		email = form.email.data
		password = form.password.data

		cursor = db.cursor()
		sql = '''
		INSERT INTO testuser (username,email,password) VALUES ( '%s', '%s', '%s')
		'''
		cursor.execute(sql%(username,email,password))

		db.commit()

		db.close()

		flash('User registered successfully! You can now login!', 'success')
		return redirect(url_for('login'))

	return render_template("register_sample.html", form=form)

@app.route('/register', methods=['POST', 'GET'])
def register():
	form = RegisterForm()
	if request.method == 'POST' and form.validate():
		username = form.username.data
		email = form.email.data
		password = form.password.data
		address = form.address.data
		region = form.region.data
		phoneNo = form.phoneNo.data

		cursor = db.cursor()
		sql = '''
		INSERT INTO user(username,useremail,userpassword,address,region,phoneNo) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')
		'''
		cursor.execute(sql%(username,email,password,address,region,phoneNo))

		db.commit()

		flash('User registered successfully! You can now login!', 'success')
		return redirect(url_for('login'))

	return render_template("register.html", form=form)

"""User Page Design"""
@app.route('/userlogin')
def userlogin():
	return render_template("userlogin.html")

@app.route('/logout', methods=['POST', 'GET'])
def logout():
	session.clear()

	cursor = db.cursor()
	sql = ("DELETE FROM cart")
	cursor.execute(sql)
	db.commit()

	return render_template("logout.html")

@app.route('/userinfo', methods=['POST', 'GET'])
def userinfo():
	if 'uname' in session:
		username = session['uname']
		cursor = db.cursor()
		sql = ("SELECT * FROM user WHERE username = '"+username+"' ")
		cursor.execute(sql)
		db.commit()
		row = cursor.fetchall()
		return render_template("userinfo.html", row=row)

@app.route('/updateuserinfo', methods=['POST', 'GET'])
def updateuserinfo():
	form = UpdateUserInfoForm()
	if 'uname' in session:
		username = session['uname']
		userid = session['userid']

		cur = db.cursor()
		sql = ("SELECT * FROM user WHERE userid=%s ")
		cur.execute(sql%(userid))
		result = cur.fetchall()

		if request.method == 'POST' and form.validate():
			username = form.username.data
			email = form.email.data
			password = form.password.data
			address = form.address.data
			region = form.region.data
			phoneNo = form.phoneNo.data

			cursor = db.cursor()
			
			check = cursor.execute("UPDATE user SET username=%s,useremail=%s,userpassword=%s,address=%s,region=%s,phoneNo=%s WHERE userid=%s ",
						(username,email,password,address,region,phoneNo,userid))
			db.commit()
			if check:
				return redirect(url_for('afterupdateuserinfo'))
			else:
				flash('User information	fail to update!', 'danger')
				return render_template("updateuserinfo.html", form=form)

	return render_template("updateuserinfo.html", form=form)

@app.route('/afterupdateuserinfo')
def afterupdateuserinfo():
	session.clear()
	return render_template("afterupdateuserinfo.html")

@app.route('/productdemo')
def productdemo():
	return render_template("productdemo.html")

@app.route('/product', methods=['POST', 'GET'])
def product():
	brand1 = db.cursor()
	brand1.execute("SELECT * FROM products WHERE pdtbrand='logitech' ")
	db.commit()
	logitech = brand1.fetchall()

	brand2 = db.cursor()
	brand2.execute("SELECT * FROM products WHERE pdtbrand='razer' ")
	db.commit()
	razer = brand2.fetchall()

	brand3 = db.cursor()
	brand3.execute("SELECT * FROM products WHERE pdtbrand='hyperx' ")
	db.commit()
	hyperx = brand3.fetchall()

	brand4 = db.cursor()
	brand4.execute("SELECT * FROM products WHERE pdtbrand='steelseries' ")
	db.commit()
	steelseries = brand4.fetchall()

	return render_template("product.html", logitech=logitech, razer=razer, hyperx=hyperx, steelseries=steelseries)


@app.route('/productdetail', methods=['POST', 'GET'])
def productdetail():
	if 'pdtid' in request.args:
		pdtid = request.args['pdtid']
		cursor = db.cursor()
		sql = ("SELECT * FROM products WHERE pdtid=%s")
		cursor.execute(sql%(pdtid))
		db.commit()
		detail = cursor.fetchall()

		return render_template("productdetail.html", detail=detail)

@app.route('/shoppingcart', methods=['POST', 'GET'])
def shoppingcart():
	if 'uname' in session:
		totalPrice = 0
		totalProduct = []
		cursor = db.cursor()
		sql = ("SELECT * FROM cart")
		cursor.execute(sql)
		db.commit()
		detail = cursor.fetchall()

		for row in detail:
			totalPrice += row[2]
			totalProduct.append(row[1])
			session['totalPrice'] = totalPrice
			session['totalProduct'] = totalProduct

		return render_template("shoppingcart.html", detail=detail, totalPrice=totalPrice, totalProduct=totalProduct)

@app.route('/cartadd', methods=['POST', 'GET'])
def cartadd():
	if 'cart' in request.args:
		pdtid = request.args['cart']
		cur = db.cursor()
		sql = ("SELECT pdtid,pdtname,pdtprice,pdtimage FROM products WHERE pdtid=%s")
		cur.execute(sql%(pdtid))
		result = cur.fetchall()
		for row in result:
			pdtid = row[0]
			pdtname = row[1]
			pdtprice = row[2]
			pdtimage = row[3]

		cursor = db.cursor()
		sql = ("INSERT INTO cart(pdtid,pdtname,pdtprice,pdtimage) VALUES ('%s','%s','%s','%s')")
		cursor.execute(sql%(pdtid,pdtname,pdtprice,pdtimage))
		db.commit()

		flash('Product added success!', 'success')
		return redirect(url_for('product'))

@app.route('/cartdelete', methods=['POST', 'GET'])
def cartdelete():
	if 'cart' in request.args:
		pdtname = request.args['cart']
		cursor = db.cursor()
		sql = ("DELETE FROM cart WHERE pdtname = '"+pdtname+"' ")
		cursor.execute(sql)
		db.commit()

		flash('Delete product from cart successfully!', 'success')
		return redirect(url_for('shoppingcart'))

'''
@app.route('/cartorder', methods=['POST', 'GET'])
def cartorder():
	if 'cart' in request.args:
		totalProduct = request.args['cart']
		for data in total
		totalPrice = session['totalPrice']

		username = session['uname']
		cur = db.cursor()
		sql1 = ("SELECT username, phoneNo, address FROM user WHERE username='"+username+"' ")
		cur.execute(sql1)
		db.commit()
		result = cur.fetchall()
		for row in result:
			for data in row:
				username = row[0]
				phoneNo = row[1]
				address = row[2]


		now = datetime.datetime.today()
		duedate = datetime.timedelta(days=14)
		delivery_time = now + duedate
		delivery_date = delivery_time.strftime("%Y/%m/%d %H:%M:%S")

		cursor = db.cursor()
		sql = ("INSERT INTO orders2(pdtsname,pdtsprice,username,phoneNo,address,date) VALUES ('%s','%s','%s','%s','%s','%s')")
		cursor.execute(sql%(str(totalProduct),totalPrice,username,phoneNo,address,delivery_date))
		db.commit()

		flash('Order success!', 'success')
		return redirect(url_for('userlogin'))
'''

@app.route('/uservieworders', methods=['POST', 'GET'])
def uservieworders():
	if 'uname' in session:
		username = session['uname']
		cursor = db.cursor()
		sql = ("SELECT * FROM orders WHERE username='"+username+"' ")
		cursor.execute(sql)
		db.commit()
		order = cursor.fetchall()

	return render_template("uservieworders.html", order=order)

@app.route('/order', methods=['POST', 'GET'])
def order():
	if 'pdtid' in request.args:
		if 'uname' in session:
			pdtid = request.args['pdtid']
			username = session['uname']

			cursor1 = db.cursor()
			sql1 = ("SELECT pdtid, pdtname, pdtprice FROM products WHERE pdtid=%s")
			cursor1.execute(sql1%(pdtid))
			db.commit()
			result1 = cursor1.fetchall()
			for rows in result1:
				pdtid = rows[0]
				pdtname = rows[1]
				pdtprice = rows[2]

			cursor2 = db.cursor()
			sql2 = ("SELECT username, phoneNo, address FROM user WHERE username = '"+username+"' ")
			cursor2.execute(sql2)
			db.commit()
			result2 = cursor2.fetchall()
			for row in result2:
				username = row[0]
				phoneNo = row[1]
				address = row[2]

			return render_template("order.html", result1=result1, result2=result2)

		else:
			flash('Please login your user account!', 'danger')
			return redirect(url_for('login'))

	return render_template("order.html")

@app.route('/ordernow', methods=['POST', 'GET'])
def ordernow():
	if 'pdtid' in request.args:
		pdtid = request.args['pdtid']

		cursor1 = db.cursor()
		sql1 = ("SELECT pdtid, pdtname, pdtprice FROM products WHERE pdtid=%s")
		cursor1.execute(sql1%(pdtid))
		db.commit()
		result1 = cursor1.fetchall()
		for rows in result1:
			pdtid = rows[0]
			pdtname = rows[1]
			pdtprice = rows[2]

		username = session['uname']
		cursor2 = db.cursor()
		sql2 = ("SELECT username, phoneNo, address FROM user WHERE username='"+username+"' ")
		cursor2.execute(sql2)
		db.commit()
		result2 = cursor2.fetchall()
		for row in result2:
			username = row[0]
			phoneNo = row[1]
			address = row[2]

		now = datetime.datetime.today()
		duedate = datetime.timedelta(days=14)
		delivery_time = now + duedate
		delivery_date = delivery_time.strftime("%Y/%m/%d %H:%M:%S")

		cur = db.cursor()
		sql = ("INSERT INTO orders(pdtid,pdtname,pdtprice,username,phoneNo,address,date) VALUES ('%s','%s','%s','%s','%s','%s','%s')")
		cur.execute(sql%(pdtid,pdtname,pdtprice,username,phoneNo,address,delivery_date))
		db.commit()

		flash('Order success!', 'success')
		return redirect(url_for('userlogin'))

	return render_template("order.html")

@app.route('/question', methods=['POST', 'GET'])
def question():
	form = QuestionForm()
	if 'uname' in session:
		username = session['uname']
		userid = session['userid']

		if request.method == 'POST' and form.validate():
			question = form.question.data

			cursor = db.cursor()
			sql = ("INSERT INTO question(userid,username,question) VALUES ('%s','%s','%s')")
			cursor.execute(sql%(userid,username,question))
			db.commit()

			flash('Question successfully sent!', 'success')
			return redirect(url_for('userlogin'))

	return render_template("question.html", form=form)

@app.route('/viewreply', methods=['POST','GET'])
def viewreply():
	if 'userid' in session:
		userid = session['userid']

		cursor = db.cursor()
		sql = ("SELECT * FROM reply WHERE userid=%s")
		cursor.execute(sql%(userid))
		db.commit()
		reply = cursor.fetchall()

		return render_template("viewreply.html", reply=reply)

"""Admin Page Design"""
@app.route('/adminlogin')
def adminlogin():
	return render_template("adminlogin.html")

@app.route('/viewuserinfo', methods=['POST','GET'])
def viewuserinfo():
	cursor = db.cursor()
	sql = ("SELECT * FROM user")
	cursor.execute(sql)
	db.commit()
	result = cursor.fetchall()

	return render_template("viewuserinfo.html", result=result)

@app.route('/uploadproduct', methods=['POST', 'GET'])
def uploadproduct():
	form = UploadProductInfoForm()
	if request.method == 'POST' and form.validate():
		productname = form.productname.data
		price = form.price.data
		brand = form.brand.data
		detail = form.detail.data
		image = form.image.data

		cursor = db.cursor()
		sql = '''
		INSERT INTO products(pdtname,pdtprice,pdtbrand,pdtdetail,pdtimage) VALUES ('%s', '%s', '%s', '%s', '%s')
		'''
		cursor.execute(sql%(productname,price,brand,detail,image))
		db.commit()

		flash('New product upload successfully!', 'success')
		return redirect(url_for('adminlogin'))

	return render_template("uploadproduct.html", form=form)

@app.route('/viewproducts', methods=['POST', 'GET'])
def viewproducts():
	cursor = db.cursor()
	sql = ("SELECT * FROM products")
	cursor.execute(sql)
	db.commit()
	allpdt = cursor.fetchall()

	return render_template("viewproducts.html", allpdt=allpdt)

@app.route('/editproduct', methods=['POST', 'GET'])
def editproduct():
	if 'pdtid' in request.args:
		pdtid = request.args['pdtid']
		form = EditProductInfoForm()
		cur = db.cursor()
		sql = ("SELECT * FROM products WHERE pdtid=%s")
		cur.execute(sql%(pdtid))
		result = cur.fetchall()

		if request.method == 'POST' and form.validate():
			productname = form.productname.data
			price = form.price.data
			brand = form.brand.data
			detail = form.detail.data
			image = form.image.data

			cursor = db.cursor()
			check = cursor.execute("UPDATE products SET pdtname=%s,pdtprice=%s,pdtbrand=%s,pdtdetail=%s,pdtimage=%s WHERE pdtid=%s ",
						(productname,price,brand,detail,image,pdtid))
			db.commit()
			if check:
				flash('Product information update successfully!', 'success')
				return render_template("editproduct.html", form=form)
			else:
				flash('Product information fail to update!', 'danger')
				return render_template("editproduct.html", form=form)

		return render_template("editproduct.html", form=form)

@app.route('/deleteproduct', methods=['POST', 'GET'])
def deleteproduct():
	if 'pdtid' in request.args:
		pdtid = request.args['pdtid']
		cursor = db.cursor()
		sql = ("DELETE FROM products WHERE pdtid=%s")
		cursor.execute(sql%(pdtid))
		db.commit()

	return redirect(url_for('viewproducts'))

@app.route('/adminvieworders', methods=['POST', 'GET'])
def adminvieworders():
	cursor = db.cursor()
	sql = ("SELECT * FROM orders")
	cursor.execute(sql)
	db.commit()
	order = cursor.fetchall()

	return render_template("adminvieworders.html", order=order)

@app.route('/deleteorder', methods=['POST','GET'])
def deleteorder():
	if 'orderid' in request.args:
		orderid = request.args['orderid']
		cursor = db.cursor()
		sql = ("DELETE FROM orders WHERE orderid=%s")
		cursor.execute(sql%(orderid))
		db.commit()

	return redirect(url_for('adminvieworders'))

@app.route('/viewquestion', methods=['POST','GET'])
def viewquestion():
	cursor = db.cursor()
	sql = ("SELECT * FROM question")
	cursor.execute(sql)
	db.commit()
	question = cursor.fetchall()

	return render_template("viewquestion.html", question=question)

@app.route('/delquestion', methods=['POST','GET'])
def delquestion():
	if 'qid' in request.args:
		qid = request.args['qid']
		cursor = db.cursor()
		sql = ("DELETE FROM question WHERE qid=%s")
		cursor.execute(sql%(qid))
		db.commit()

		flash('Question deleted!', 'success')
		return redirect(url_for('viewquestion'))

@app.route('/reply', methods=['POST','GET'])
def reply():
	form = ReplyForm()
	if 'qid' in request.args:
		qid = request.args['qid']

		cur = db.cursor()
		sql1 = ("SELECT qid,userid,question FROM question WHERE qid=%s")
		cur.execute(sql1%(qid))
		db.commit()
		result = cur.fetchall()
		for row in result:
			qid = row[0]
			userid = row[1]
			question = row[2]

		if request.method == 'POST' and form.validate():
			reply = form.reply.data

			cursor = db.cursor()
			sql = ("INSERT INTO reply(qid,userid,question,reply) VALUES ('%s','%s','%s','%s')")
			cursor.execute(sql%(qid,userid,question,reply))
			db.commit()

			flash('Reply success!', 'success')
			return redirect(url_for('adminlogin'))

	return render_template("reply.html", form=form, result=result)


if __name__ == '__main__':
	app.run(debug = True)