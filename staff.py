from flask import *
from database import *
import uuid
from datetime import datetime



staff=Blueprint("staff",__name__)

@staff.route('/staff_home')
def staff_home():
	return render_template('staff_home.html')


@staff.route('/staff_viewapp')
def staff_viewapp():
	data={}
	e="SELECT *,users.login_id as u_lid,appointment.status as ap_status FROM appointment  INNER JOIN pets USING (pet_id)  INNER JOIN category USING(category_id) INNER JOIN users ON users.user_id=`appointment`.user_id  inner join staff_assign using(appointment_id) where staff_assign.staff_id='%s' "%(session['staff_id'])
	data['view']=select(e)
	print(e)


	if 'action' in request.args:
		action=request.args['action']
		s_id=request.args['appointment_id']
	else:
		action=None
	if action=='accept':
		u="update appointment set status='assigned' where appointment_id='%s'"%(s_id)
		update(u)
		return redirect(url_for('staff.staff_viewapp'))
	if action=='reject':
		r="update appointment set status='reject' where appointment_id='%s'"%(s_id)
		update(r)
		return redirect(url_for('staff.staff_viewapp'))
	
	return render_template('staff_viewapp.html',data=data)


@staff.route('/shop_view_booking')
def shop_view_booking():
	data={}
	w="select * from pet_sale inner join pets using(pet_id) INNER JOIN users USING(user_id) where Pet_for_id='%s'"%(session['login_id'])
	data['view']=select(w)
	e="select * from acc_sale inner join users using(user_id) inner join accessories using (accessorie_id) where shop_id='%s'"%(session['shop_id'])
	data['view1']=select(e) 

	return render_template('shop_view_booking.html',data=data)

@staff.route('/shop_view_payment')
def shop_view_payment():
	data={}
	r="SELECT * FROM `payment` WHERE `shop_id`='%s'"%(session['shop_id'])
	data['view1']=select(r)
	return render_template('shop_view_payment.html',data=data)


@staff.route('/staff_viewcustompet',methods=['get','post'])
def staff_viewcustompet():
	data={}
	
	e="select * from allocation_request inner join users using (user_id)  where staff_id=(select staff_id from staff where login_id='%s')"%(session['login_id'])
	data['view']=select(e)

	if 'action' in request.args:
		action=request.args['action']
		s_id=request.args['allocation_request_id']
	else:
		action=None
	if action=='accept':
		u="update allocation_request set status='accept' where allocation_request_id='%s'"%(s_id)
		update(u)
		return redirect(url_for('staff.staff_viewcustompet'))
	if action=='reject':
		r="update allocation_request set status='reject' where allocation_request_id='%s'"%(s_id)
		update(r)
		return redirect(url_for('staff.staff_viewcustompet'))	
	return render_template('staff_viewcustompet.html',data=data)


@staff.route('/staff_viewpets1')
def staff_viewpets1():
	data={}
	uid=request.args['uid']
		
	s="SELECT * FROM pets INNER JOIN users ON pets.pet_for_id=users.login_id INNER JOIN allocation_request ON users.user_id=allocation_request.user_id WHERE allocation_request.user_id='%s'"%(uid)
	data['view']=select(s)

	return render_template('admin_view_petdetails.html',data=data)


@staff.route('/staff_viewpayment')
def staff_viewpayment():
	data={}
	appointment_id=request.args['appointment_id']
	e="select * from payment where appointment_id='%s'"%(appointment_id)
	data['view']=select(e)
	return render_template('staff_viewpayment.html',data=data)


@staff.route('/user_chat',methods=['get','post'])
def user_chat():
	data={}
	slid=request.args['slid']
	timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	data['timestamp']=timestamp

	gg="SELECT * FROM `chat` INNER JOIN login ON `login`.`Login_id`=`chat`.`sender_id` where `sender_id`='%s' AND `receiver_id`='%s'  or (`sender_id`='%s' AND `receiver_id`='%s' )"%(slid,session['login_id'],session['login_id'],slid)
	print(gg)
	data['view']=select(gg)

	if 'submit' in request.form:
		message=request.form['message']
		h="insert into `chat` values(null,'%s','%s','%s',curdate())"%(session['login_id'],slid,message)
		insert(h)
		return redirect(url_for('staff.user_chat',slid=slid))

	
	return render_template('user_chat.html',data=data,slid=slid)



@staff.route('/addamount',methods=['get','post'])
def addamount():
	data={}
	appointment_id=request.args['appointment_id']
	

	if "pet_add" in request.form:
		amount=request.form['amount']

		q="update appointment set amount='%s' , status='addamount' where appointment_id='%s'"%(amount,appointment_id)
		update(q)
		print(q)
		return redirect(url_for('staff.staff_viewapp'))
		
	return render_template('addamount.html',data=data)

@staff.route('/staff_view_petimage')
def staff_view_petimage():
	data={}
	pid=request.args['pid']
	e="select * from pet_image where pet_id='%s'"%(pid)
	data['view']=select(e)
	return render_template('staff_view_petimage.html',data=data)
@staff.route('/staff_view_petdetails')
def staff_view_petdetails():
	data={}
	uid=request.args['uid']
		
	s="SELECT * FROM pets INNER JOIN users ON pets.pet_for_id=users.login_id INNER JOIN allocation_request ON users.user_id=allocation_request.user_id WHERE allocation_request.user_id='%s'"%(uid)
	data['view']=select(s)
	return render_template('staff_view_petdetails.html',data=data)
@staff.route('/addamount1',methods=['get','post'])
def addamount1():
	data={}
	allocation_request_id=request.args['allocation_request_id']
	
	if "pet_add" in request.form:
		amount=request.form['amount']

		q="update allocation_request set amount='%s' , status='addamount' where allocation_request_id='%s'"%(amount,allocation_request_id)
		update(q)
		print(q)
		return redirect(url_for('admin.admin_view_allocation'))
		
	return render_template('admin_add_amount.html',data=data)