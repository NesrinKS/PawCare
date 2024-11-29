from flask import *
from database import *
import uuid



public=Blueprint("public",__name__)

@public.route('/')
def home():
	data={}
	t="select * from rating inner join users using(user_id)"
	data['view']=select(t)
	for item in data['view']:
		item['rate'] = int(item['rate'])
	return render_template('index.html',data=data,int=int)

@public.route('/login',methods=['get','post'])
def login():
	if 'login' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['user_type']=='admin':
				
				return redirect(url_for('admin.admin_home'))
			if res[0]['user_type']=='shop':
				w="select * from shops where login_id='%s'"%(session['login_id'])
				res2=select(w)
				if res2:
					session['shop_id']=res2[0]['shop_id']
				
				return redirect(url_for('shop.shop_home'))
			if res[0]['user_type']=='veterinary':
				w="select * from hospitals where login_id='%s'"%(session['login_id'])
				res2=select(w)
				if res2:
					session['hospital_id']=res2[0]['hospital_id']
				
				return redirect(url_for('hospitals.hospitals_home'))
			if res[0]['user_type']=='user':
				w="select * from users where login_id='%s'"%(session['login_id'])
				res2=select(w)
				if res2:
					session['user_id']=res2[0]['user_id']
				return redirect(url_for('user.user_home'))

			if res[0]['user_type']=='staff':
				w="select * from staff where login_id='%s'"%(session['login_id'])
				res8=select(w)
				if res8:
					session['staff_id']=res8[0]['staff_id']
				
				return redirect(url_for('staff.staff_home'))
	if 'cha_pass' in request.form:
		uname=request.form['uname']
		pass1=request.form['pass1']
		t="update login set password='%s' where username='%s'"%(pass1,uname)
		update(t)		
		return redirect(url_for('public.login'))
	return render_template('login.html')
@public.route('/shop_reg',methods=['get','post'])
def shop_reg():
	if 'shop_reg' in request.form:
		s_name=request.form['s_name']
		place=request.form['place']
		email=request.form['email']
		phone=request.form['phone']
		o_name=request.form['o_name']
		s_file=request.files['s_file']
		path="static/images/"+str(uuid.uuid4())+s_file.filename
		s_file.save(path)
		uname=request.form['uname']
		passw=request.form['passw']
		r="insert into login value(null,'%s','%s','pending')"%(uname,passw)
		log=insert(r)
		t="insert into shops value(null,'%s','%s','%s','%s','%s','%s','%s')"%(log,s_name,o_name,path,place,email,phone)
		insert(t)
		flash("Added successfully")

	return render_template('shop_reg.html')
@public.route('/reg_hospitals',methods=['get','post'])
def reg_hospitals():
	data={}
	if 'add_hos' in request.form:
		h_name=request.form['h_name']
		h_phone=request.form['phone']
		h_place=request.form['h_place']
		phone=request.form['phone']
		email=request.form['email']
		pincode=request.form['pincode']
		fee=request.form['fee']
		uname=request.form['uname']
		passw=request.form['passw']
		e="insert into login values(null,'%s','%s','pending')"%(uname,passw)
		res=insert(e)
		t="insert into hospitals values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,h_name,h_place,h_phone,email,pincode,fee)
		insert(t)

		flash("Added successfully")
	return render_template('reg_hospitals.html',data=data)
@public.route('/user_reg',methods=['post','get'])
def user_reg():
	if 'add' in request.form:
	   first_name=request.form['fname']
	   last_name=request.form['lname']
	   phone=request.form['phone']
	   place=request.form['place']
	   email=request.form['email']
	   pincode=request.form['pincode']
	   address=request.form['address']
	   username=request.form['uname']
	   password=request.form['passw']
	   q="insert into login values(null,'%s','%s','user')"%(username,password)
	   log=insert(q)
	   r="insert into users values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(log,first_name,last_name,phone,place,email,pincode,address)
	   insert(r)
	return render_template('user_reg.html')

   