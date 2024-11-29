from flask import *
from database import *
import uuid



admin=Blueprint("admin",__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_manage_category',methods=['get','post'])
def admin_manage_category():
	data={}
	if 'add' in request.form:
		cat_name=request.form['cat_name']
		
		t="insert into category values(null,'%s')"%(cat_name)
		insert(t)
		flash("Added successfully")
	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
		
	else:
		action=None
	if action=='update':
		rr="select * from category where category_id='%s'"%(cid)
		data['up']=select(rr)
	if 'update' in request.form:
		cat_name=request.form['cat_name']
		
	
		ee="update category set category_name='%s' where category_id='%s'"%(cat_name,cid)
		update(ee)
		flash("updated successfully")
	if action=='delete':
		g="delete from category where category_id='%s'"%(cid)
		delete(g)
		flash("deleted successfully")	

	ee="select * from category"
	data['view']=select(ee)
	return render_template('admin_manage_category.html',data=data)

@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():
	data={}
	if 'add_hos' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phone']
		place=request.form['place']
		email=request.form['email']
		specialization=request.form['specialization']
		uname=request.form['uname']
		passw=request.form['passw']
		e="insert into login values(null,'%s','%s','staff')"%(uname,passw)
		res=insert(e)
		t="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,place,phone,email,specialization)
		insert(t)
		flash("Added successfully")
	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
		log_id=request.args['log_id']
	else:
		action=None
	if action=='update':
		rr="select * from staff where staff_id='%s'"%(sid)
		data['up']=select(rr)
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phone']
		place=request.form['place']
		email=request.form['email']
		specialization=request.form['specialization']
		
		ee="update staff set fname='%s',lname='%s',phone='%s',place='%s',email='%s',specialization='%s' where staff_id='%s'"%(fname,lname,phone,place,email,specialization,sid)
		update(ee)
		flash("updated successfully")
	if action=='delete':
		g="delete from staff where staff_id='%s'"%(sid)
		delete(g)
		r="delete from login where login_id='%s'"%(log_id)
		delete(r)
		flash("deleted successfully")	

	ee="select * from staff"
	data['view']=select(ee)
	return render_template('admin_manage_staff.html',data=data)
@admin.route('/admin_view_shop')
def admin_view_shop():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		h_id=request.args['s_id']
		log_id=request.args['log_id']
	else:
		action=None
	if action=='update':
		rr="update login set user_type='shop' where login_id='%s'"%(log_id)
		update(rr)
		return redirect(url_for('admin.admin_view_shop'))
	if action=='delete':
		r="delete from shops where shop_id='%s'"%(h_id)
		delete(r)
		r="delete from login where login_id='%s'"%(log_id)
		delete(r)
		return redirect(url_for('admin.admin_view_shop'))
		flash("deleted successfully")	
	s="select * from shops inner join login using(login_id)"
	data['view']=select(s)

	return render_template('admin_view_shop.html',data=data)
@admin.route('/admin_view_veterinary_officials')
def admin_view_veterinary_officials():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		h_id=request.args['h_id']
		log_id=request.args['log_id']
	else:
		action=None
	if action=='update':
		rr="update login set user_type='veterinary' where login_id='%s'"%(log_id)
		update(rr)
		return redirect(url_for('admin.admin_view_veterinary_officials'))
	if action=='delete':
		r="delete from hospitals where hospital_id='%s'"%(h_id)
		delete(r)
		r="delete from login where login_id='%s'"%(log_id)
		delete(r)
		return redirect(url_for('admin.admin_view_veterinary_officials'))
		flash("deleted successfully")	
	s="select * from hospitals inner join login using(login_id)"
	data['view']=select(s)

	return render_template('admin_view_veterinary_officials.html',data=data)
@admin.route('/admin_view_appointment')
def admin_view_appointment():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
		
	else:
		action=None
	if action=='accept':
		u="update appointment set status='accept' where appointment_id='%s'"%(aid)
		update(u)
		return redirect(url_for('admin.admin_view_appointment'))
	if action=='reject':
		u="update appointment set status='reject' where appointment_id='%s'"%(aid)
		update(u)
		return redirect(url_for('admin.admin_view_appointment'))
	s="select * from appointment inner join category using(category_id) inner join users using(user_id)"
	data['view']=select(s)
	return render_template('admin_view_appointment.html',data=data)
@admin.route('/admin_view_petdetails')
def admin_view_petdetails():
	data={}
	pid=request.args['pid']
	e="select * from pets where pet_id='%s'"%(pid)
	data['view']=select(e)
	return render_template('admin_view_petdetails.html',data=data)
@admin.route('/admin_view_allo_petdetails')
def admin_view_allo_petdetails():
	data={}
	uid=request.args['uid']
	e="SELECT * FROM pets INNER JOIN users ON pets.pet_for_id=users.login_id INNER JOIN allocation_request ON users.user_id=allocation_request.user_id WHERE allocation_request.user_id='%s'"%(uid)
	data['view']=select(e)
	return render_template('admin_view_petdetails.html',data=data)

@admin.route('/admin_assign_allo_staff',methods=['get','post'])
def admin_assign_allo_staff():
	data={}
	allocation_request_id=request.args['allocation_request_id']
	
	e="select * from staff"
	data['view']=select(e)


	if "pet_add" in request.form:
		cid=request.form['cid']

		q="update allocation_request set staff_id='%s' , status='assigned' where allocation_request_id='%s'"%(cid,allocation_request_id)
		update(q)
		print(q)
		return redirect(url_for('admin.admin_view_allocation'))
		
	return render_template('admin_assign_allo_staff.html',data=data)
# @admin.route('/addamount1',methods=['get','post'])
# def addamount1():
# 	data={}
# 	allocation_request_id=request.args['allocation_request_id']
	
# 	if "pet_add" in request.form:
# 		amount=request.form['amount']

# 		q="update allocation_request set amount='%s' , status='addamount' where allocation_request_id='%s'"%(amount,allocation_request_id)
# 		update(q)
# 		print(q)
# 		return redirect(url_for('admin.admin_view_allocation'))
		
# 	return render_template('admin_add_amount.html',data=data)
@admin.route('/admin_assign_staff')
def admin_assign_staff():
	data={}
	aid=request.args['aid']
	data['aid']=aid
	e="select * from staff"
	data['view']=select(e)
	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None
	if action=='assign':
		appointment_id=request.args['aid']
		staff_id=request.args['sid']
		up="insert into staff_assign values(null,'%s','%s',curdate(),'pending')"%(appointment_id,staff_id)
		insert(up)
		up="update appointment set status='assigned' where appointment_id='%s'"%(appointment_id)
		update(up)
		flash("Assigned successfully")
		return redirect(url_for('admin.admin_view_appointment'))


	return render_template('admin_assign_staff.html',data=data)
@admin.route('/admin_view_petimage')
def admin_view_petimage():
	data={}
	pid=request.args['pid']
	e="select * from pet_image where pet_id='%s'"%(pid)
	data['view']=select(e)
	return render_template('admin_view_petimage.html',data=data)
@admin.route('/admin_view_allocation',methods=['get','post'])
def admin_view_allocation():
	data={}
	
	e="select * from allocation_request"
	data['view']=select(e)	
	return render_template('admin_view_allocation.html',data=data)
@admin.route('/admin_view_complaints')
def admin_view_complaints():
	data={}
	e="select * from complaints inner join users using(login_id)"
	data['view']=select(e)
	return render_template('admin_view_complaints.html',data=data)
@admin.route('/admin_send_reply',methods=['get','post'])
def admin_send_reply():
	c_id=request.args['c_id']
	if 'reply' in request.form:
		reply=request.form['reply']
		y="update complaints set reply='%s' where complaint_id='%s'"%(reply,c_id)
		update(y)
		return redirect(url_for('admin.admin_view_complaints'))
	return render_template('admin_send_reply.html')
@admin.route('/admin_report')
def admin_report():
	data={}
	e="SELECT * FROM appointment  INNER JOIN pets USING (pet_id)  INNER JOIN category USING(category_id) INNER JOIN users ON users.user_id=`appointment`.user_id"
	data['r']=select(e)
	
	return render_template('admin_report.html',data=data)
@admin.route('/admin_allocation_report',methods=['get','post'])
def admin_allocation_report():
	data={}
	s="select * from allocation_request inner join users using(user_id)"
	data['view']=select(s)
	return render_template('admin_allocation_report.html',data=data)
@admin.route('/admin_veterinary_appo_report')
def admin_veterinary_appo_report():
	data={}
	e="SELECT * FROM vet_appointment  INNER JOIN pets USING (pet_id)  INNER JOIN hospitals USING(hospital_id) INNER JOIN users ON users.login_id=`pets`.pet_for_id"
	data['view']=select(e)
	
	return render_template('admin_veterinary_appo_report.html',data=data)
@admin.route('/admin_accessories_report')
def admin_accessories_report():
	data={}
	e="SELECT * FROM purchase_master  INNER JOIN purchase_child USING (purchase_master_id)  INNER JOIN accessories USING(accessorie_id) INNER JOIN users using(user_id) inner join shops ON shops.shop_id=`accessories`.shop_id"
	data['view']=select(e)
	
	return render_template('admin_accessories_report.html',data=data)
@admin.route('/admin_pet_report')
def admin_pet_report():
	data={}
	e="SELECT * FROM sales_master  INNER JOIN sales_child USING (sales_master_id)  INNER JOIN pets USING(pet_id) INNER JOIN users using(user_id) inner join shops ON shops.login_id=`pets`.Pet_for_id"
	data['view']=select(e)
	
	return render_template('admin_pet_report.html',data=data)
@admin.route('/admin_payment_report')
def admin_payment_report():
	data={}
	e="SELECT payment.*, accessories.*, pets.*, hospitals.*, vet_appointment.*, allocation_request.*, staff.*,appointment.*, shops.*,users.*,payment.amount as pay FROM payment LEFT JOIN accessories ON accessories.accessorie_id = payment.shop_id LEFT JOIN pets ON pets.pet_id = payment.shop_id LEFT JOIN vet_appointment ON vet_appointment.vet_appointment_id = payment.shop_id LEFT JOIN hospitals ON hospitals.hospital_id = vet_appointment.hospital_id LEFT JOIN allocation_request ON allocation_request.allocation_request_id = payment.shop_id LEFT JOIN appointment ON appointment.appointment_id = payment.shop_id LEFT JOIN shops ON shops.shop_id = accessories.shop_id OR shops.login_id = pets.pet_for_id LEFT join users on users.user_id=payment.payment_for_id LEFT join staff on staff.staff_id=allocation_request.staff_id WHERE payment.shop_id IS NOT NULL;"
	data['view']=select(e)
	
	return render_template('admin_payment_report.html',data=data)

@admin.route('/admin_add_petevents',methods=['get','post'])
def admin_add_petevents():
	data={}
	if 'add_event' in  request.form:
		
		image=request.files['image']
		path="static/images/"+str(uuid.uuid4())+image.filename
		image.save(path)
		rr="insert into events values(null,'%s')"%(path)
		insert(rr)
		flash("Added successfully")
		return redirect(url_for('admin.admin_add_petevents'))
	if 'action' in request.args:
		action=request.args['action']
		event_id=request.args['event_id']
	else:
		action=None
	if action=='update':
		d="select * from events where event_id='%s'"%(event_id)
		data['up']=select(d)
	if action=='delete':
		ee="delete from events where event_id='%s'"%(event_id)
		delete(ee)
		flash("deleted successfully")
		return redirect(url_for('admin.admin_add_petevents'))
	if 'update' in request.form:
		
		image=request.files['image']
		path="static/images/"+str(uuid.uuid4())+image.filename
		image.save(path)
		ww="update events set image='%s' where event_id='%s'"%(path,event_id)
		update(ww)
		flash("Updated successfully")
		return redirect(url_for('admin.admin_add_petevents'))




	e="select * from events"
	data['view']=select(e)	
	return render_template('admin_add_petevents.html',data=data)
