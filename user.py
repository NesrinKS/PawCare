from flask import * 
from database import *
import uuid
from datetime import date
import decisiontree as dt
user=Blueprint("user",__name__)
@user.route('/user_home')
def user_home():
	return render_template('user_home.html')
@user.route('/user_manage_pet',methods=['get','post'])
def user_manage_pet():
	data={}
	if 'pet_add' in request.form:
		pet_name=request.form['pet_name']
		age=request.form['age']
		color=request.form['color']
		breed=request.form['breed']
		gender=request.form['gender']
		
		q="insert into pets values(null,'%s','%s','%s','%s','%s','%s','user','0','0')"%(session['login_id'],pet_name,age,color,breed,gender)
		insert(q)
		flash("Added successfully")
		return redirect(url_for('user.user_manage_pet'))
	if 'action' in request.args:
		action=request.args['action']
		pet_id=request.args['pet_id']
	else:
		action=None
	if action=='update':
		d="select * from pets where pet_id='%s'"%(pet_id)
		data['up']=select(d)
	if action=='delete':
		ee="delete from pets where pet_id='%s'"%(pet_id)
		delete(ee)
		flash("deleted successfully")
		return redirect(url_for('user.user_manage_pet'))
	if 'update' in request.form:
		pet_name=request.form['pet_name']
		age=request.form['age']
		color=request.form['color']
		breed=request.form['breed']
		gender=request.form['gender']
		ww="update pets set pet_name='%s',age='%s',color='%s',breed='%s',gender='%s' where pet_id='%s'"%(pet_name,age,color,breed,gender,pet_id)
		update(ww)
		flash("Updated successfully")
		return redirect(url_for('user.user_manage_pet'))
			
	s="select * from pets where pet_for_id='%s'"%(session['login_id'])
	data['view']=select(s)


	return render_template('user_manage_pet.html',data=data)
@user.route('/user_add_image',methods=['get','post'])
def user_add_image():
	data={}
	if 'add' in request.form:
		pid=request.args['pet_id']
		type=request.form['type']
		p_image=request.files['p_image']
		path="static/images/"+str(uuid.uuid4())+p_image.filename
		p_image.save(path)
		u="insert into pet_image values(null,'%s','%s','%s')"%(pid,path,type)
		insert(u)
		return redirect(url_for('user.user_manage_pet'))
	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pet_id']
	else:
		action=None
	if action=='delete':
		r="delete from pet_image where pet_image_id='%s'"%(pid)
		delete(r)
		return redirect(url_for('user.user_manage_pet'))
	pid=request.args['pet_id']
	s="select * from pet_image where pet_id='%s'"%(pid)
	res=select(s)
	data['view']=res
	if res:

		p_type=res[0]['type']
		data['type']=p_type

	return render_template('user_add_image.html',data=data)
@user.route('/user_make_appointment',methods=['get','post'])
def user_make_appointment():
	data={}
	y="select * from category"
	data['cat']=select(y)
	current_date = date.today().strftime('%Y-%m-%d')
	data['current_date'] = current_date
	if 'add' in request.form:
		pet_id=request.args['pet_id']
		cat=request.form['cat']
		book_date=request.form['book_date']
		i="insert into appointment values(null,'%s','%s','%s','pending','%s',curdate(),'0')"%(cat,pet_id,session['user_id'],book_date)
		insert(i)
		flash("Appointment Added successfully")
		return redirect(url_for('user.user_make_appointment'))



	return render_template('user_make_appointment.html',data=data)
@user.route('/user_view_appointment')
def user_view_appointment():
	data={}
	s="select *,staff.login_id as s_lid,appointment.status as astatus from appointment inner join category using(category_id) inner join users using(user_id) inner join staff_assign using(appointment_id) inner join staff using(staff_id) where appointment.user_id='%s'"%(session['user_id'])
	data['view']=select(s)
	return render_template('user_view_appointments.html',data=data)
@user.route('/user_allocated',methods=['get','post'])
def user_allocated():
	data={}
	e="select * from allocation_request where user_id='%s'"%(session['user_id'])
	data['view']=select(e)


	if "action" in request.args:
		action=request.args['action']	
		allocation_request_id=request.args['allocation_request_id']

	else:
		action=None

	if action=='ok':
		q="update allocation_request set status='ok' where allocation_request_id='%s'"%(allocation_request_id)
		update(q)
		return redirect(url_for('user.user_allocated'))


	if "pet_add" in request.form:
		no_days=request.form['no_days']
		day=request.form['day']
		q="insert into allocation_request values(null,'%s','%s','0',curdate(),'pending','%s','0')"%(day,no_days,session['user_id'])
		insert(q)
		return redirect(url_for('user.user_allocated'))
	
	
	return render_template('user_allocated.html',data=data)
@user.route('/user_make_pet_allo_payment',methods=['get','post'])
def user_make_pet_allo_payment():
	data={}
	allo_id=request.args['allo_id']
	amount=request.args['amo']
	
	data['amount']=amount
	

	if "payment" in request.form:
		
		q="insert into payment values(null,'%s','%s','Allocation','%s',curdate())"%(allo_id,session['user_id'],amount)
		insert(q)
		q="update allocation_request set status='paid' where allocation_request_id='%s'"%(allo_id)
		update(q)
		flash("Payemnt successfully Completed")
		return redirect(url_for('user.user_home'))
	return render_template('user_make_pet_allo_payment.html')
@user.route('/staff_chat',methods=['get','post'])
def staff_chat():
	data={}
	slid=request.args['slid']
	if 'submit' in request.form:
		message=request.form['message']
		h="insert into `chat` values(null,'%s','%s','%s',curdate())"%(session['login_id'],slid,message)
		insert(h)
		return redirect(url_for('user.staff_chat',slid=slid))
	gg="SELECT * FROM `chat` INNER JOIN login ON `login`.`Login_id`=`chat`.`sender_id` where `sender_id`='%s' AND `receiver_id`='%s'  or (`sender_id`='%s' AND `receiver_id`='%s' )"%(slid,session['login_id'],session['login_id'],slid)
	print(gg)
	data['view']=select(gg)
	return render_template('staff_chat.html',data=data,slid=slid)
@user.route('/user_make_payment',methods=['get','post'])
def user_make_payment():
	data={}
	appointment_id=request.args['aid']
	amount=request.args['amount']
	cat=request.args['cat']
	data['amount']=amount
	

	if "payment" in request.form:
		
		q="insert into payment values(null,'%s','%s','%s','%s',curdate())"%(appointment_id,session['user_id'],cat,amount)
		insert(q)
		q="update appointment set status='paid' where appointment_id='%s'"%(appointment_id)
		update(q)
		flash("Payemnt successfully Completed")
		return redirect(url_for('user.user_home'))
	return render_template('user_make_payment.html')
@user.route('/user_view_accessories',methods=['get','post'])
def user_view_accessories():
	data={}
	d="select * from accessories where quantity>0"
	data['view']=select(d)
	return render_template('user_view_accessories.html',data=data)
@user.route('/user_addtocart',methods=['post','get'])	
def user_addtocart():
	data={}
	p=request.args['price']
	data['amo']=p

	pro=request.args['pro']
	data['prod']=pro


	q="select * from purchase_child inner join purchase_master using (purchase_master_id) inner join accessories using (accessorie_id) inner join users using (user_id) where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['order']=res
	qty=request.args['qty']
	data['qty']=qty


	if "add" in request.form:
		uid=session['user_id']
		pid=request.args['pid']
		a=request.args['price']
		sid=request.args['sid']
		t=request.form['total']
		qu=request.form['qua']

		q="select * from purchase_master where user_id='%s' and status='pending'"%(uid)
		res=select(q)
		if res:
			omid=res[0]['purchase_master_id']
		else:


			q="insert into purchase_master values(null,'%s','0',curdate(),'pending')"%(uid)
			omid=insert(q)

		q="select * from purchase_child where accessorie_id='%s' and purchase_master_id='%s'"%(pid,omid)
		res=select(q)
		print(q)

		if res:
				odid=res[0]['purchase_child_id']	

				q="update purchase_child set qty=qty+'%s' , amount=amount+'%s' where purchase_child_id='%s'"%(qu,t,odid)
				update(q)
				print(q)

		else:
			w="insert into purchase_child values(null,'%s','%s','%s','%s')"%(omid,pid,t,qu)
			insert(w)


		q="update purchase_master set total=total+'%s' where purchase_master_id='%s'"%(t,omid)
		update(q)	



		return redirect(url_for('user.user_view_accessories'))

	return render_template('user_addtocart.html',data=data)
@user.route('/user_cart',methods=['post','get'])
def user_cart():
	data={} 
	uid=session['user_id']
	# q="SELECT * FROM order_details INNER JOIN order_master  USING (order_master_id) INNER JOIN products USING (product_id) INNER JOIN users USING(user_id) where user_id='%s'"%(uid)
	# q="SELECT *,`order_master`.status AS st FROM order_details INNER JOIN order_master  USING (order_master_id) INNER JOIN products USING (product_id) INNER JOIN users USING(user_id) WHERE user_id='%s'"%(uid)
	# res=select(q)
	# data['order']=res
	if 'actionn1' in request.args:
		action = request.args['actionn1']
		
		oid=request.args['oid']
		amo=request.args['amo']
	else:
		action = None
	

	if action == 'remove':
		odid=request.args['odid']
		l = "delete from purchase_child where purchase_child_id='%s'" % (odid)
		delete(l)
		ll="select * from purchase_master where purchase_master_id='%s'"%(oid)
		sdd=select(ll)
		if sdd[0]['total']==amo:
			l = "delete from purchase_master where purchase_master_id='%s'" % (oid)
			delete(l)
			flash("Removed..........!")
			return redirect(url_for('user.user_view_accessories'))
		else:
			j="update purchase_master set total=total-'%s' where purchase_master_id='%s' "%(amo,oid)
			update(j)
			flash("Removed..........!")
			return redirect(url_for('user.user_view_accessories'))
	gf="SELECT *, `purchase_child`.`amount` AS c_t, purchase_child.qty AS rr, `purchase_master`.status AS st FROM purchase_child INNER JOIN purchase_master USING (purchase_master_id) INNER JOIN accessories USING (accessorie_id) INNER JOIN users USING (user_id) WHERE user_id='%s' AND `purchase_master`.`status`='pending'"%(session['user_id'])
	data['view_book_cart']=select(gf)	
	return render_template('user_cart.html',data=data)
@user.route('/user_make_acc_payment',methods=['get','post'])
def user_make_acc_payment():
	data={}
	purchase_master_id=request.args['pid']
	amount=request.args['amo']
	acc_id=request.args['acc_id']
	qty=request.args['qty']
	
	data['amount']=amount
	

	if "payment" in request.form:
		
		q="insert into payment values(null,'%s','%s','accessories','%s',curdate())"%(purchase_master_id,session['user_id'],amount)
		insert(q)
		q="update purchase_master set status='paid' where purchase_master_id='%s'"%(purchase_master_id)
		update(q)
		u="update accessories set quantity=quantity-'%s' where accessorie_id='%s'"%(qty,acc_id)
		update(u)
		flash("Payemnt successfully Completed")
		return redirect(url_for('user.user_home'))
	return render_template('user_make_payment.html')



@user.route('/user_view_pet',methods=['get','post'])
def user_view_pet():
	data={}
	d="select * from pets inner join shops on pets.pet_for_id=shops.login_id where type='shop'"
	data['view']=select(d)
	return render_template('user_view_pet.html',data=data)
@user.route('/user_view_petimage')
def user_view_petimage():
	data={}
	pid=request.args['pid']
	e="select * from pet_image where pet_id='%s'"%(pid)
	data['view']=select(e)
	return render_template('user_view_petimage.html',data=data)
@user.route('/user_pet_addtocart',methods=['post','get'])	
def user_pet_addtocart():
	data={}
	p=request.args['price']
	data['amo']=p

	pro=request.args['pro']
	data['prod']=pro


	q="select * from sales_child inner join sales_master using (sales_master_id) inner join pets using (pet_id) inner join users using (user_id) where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['order']=res
	qty=request.args['qty']
	data['qty']=qty


	if "add" in request.form:
		uid=session['user_id']
		pid=request.args['pid']
		a=request.args['price']
		sid=request.args['sid']
		t=request.form['total']
		qu=request.form['qua']

		q="select * from sales_master where user_id='%s' and status='pending'"%(uid)
		res=select(q)
		if res:
			omid=res[0]['sales_master_id']
		else:


			q="insert into sales_master values(null,'%s','0',curdate(),'pending')"%(uid)
			omid=insert(q)

		q="select * from sales_child where pet_id='%s' and sales_master_id='%s'"%(pid,omid)
		res=select(q)
		print(q)

		if res:
				odid=res[0]['sales_child_id']	

				q="update sales_child set s_qty=s_qty+'%s' , s_amount=s_amount+'%s' where sales_child_id='%s'"%(qu,t,odid)
				update(q)
				print(q)

		else:
			w="insert into sales_child values(null,'%s','%s','%s','%s')"%(omid,pid,t,qu)
			insert(w)


		q="update sales_master set total=total+'%s' where sales_master_id='%s'"%(t,omid)
		update(q)	



		return redirect(url_for('user.user_view_pet'))

	return render_template('user_pet_addtocart.html',data=data)
@user.route('/user_pet_cart',methods=['post','get'])
def user_pet_cart():
	data={} 
	uid=session['user_id']
	# q="SELECT * FROM order_details INNER JOIN order_master  USING (order_master_id) INNER JOIN products USING (product_id) INNER JOIN users USING(user_id) where user_id='%s'"%(uid)
	# q="SELECT *,`order_master`.status AS st FROM order_details INNER JOIN order_master  USING (order_master_id) INNER JOIN products USING (product_id) INNER JOIN users USING(user_id) WHERE user_id='%s'"%(uid)
	# res=select(q)
	# data['order']=res
	if 'actionn1' in request.args:
		action = request.args['actionn1']
		
		oid=request.args['oid']
		amo=request.args['amo']
	else:
		action = None
	

	if action == 'remove':
		odid=request.args['odid']
		l = "delete from sales_child where sales_child_id='%s'" % (odid)
		delete(l)
		ll="select * from sales_master where sales_master_id='%s'"%(oid)
		sdd=select(ll)
		if sdd[0]['total']==amo:
			l = "delete from sales_master where sales_master_id='%s'" % (oid)
			delete(l)
			flash("Removed..........!")
			return redirect(url_for('user.user_view_pet'))
		else:
			j="update sales_master set total=total-'%s' where sales_master_id='%s' "%(amo,oid)
			update(j)
			flash("Removed..........!")
			return redirect(url_for('user.user_view_pet'))
	gf="SELECT *, `sales_child`.`s_amount` AS c_t, sales_child.s_qty AS rr, `sales_master`.status AS st FROM sales_child INNER JOIN sales_master USING (sales_master_id) INNER JOIN pets USING (pet_id) INNER JOIN users USING (user_id) WHERE user_id='%s' AND `sales_master`.`status`='pending'"%(session['user_id'])
	data['view_book_cart']=select(gf)	
	return render_template('user_pet_cart.html',data=data)
@user.route('/user_make_pet_payment',methods=['get','post'])
def user_make_pet_payment():
	data={}
	purchase_master_id=request.args['pid']
	amount=request.args['amo']
	
	data['amount']=amount
	

	if "payment" in request.form:
		
		q="insert into payment values(null,'%s','%s','pets','%s',curdate())"%(purchase_master_id,session['user_id'],amount)
		insert(q)
		q="update sales_master set status='paid' where sales_master_id='%s'"%(purchase_master_id)
		update(q)
		flash("Payemnt successfully Completed")
		return redirect(url_for('user.user_home'))
	return render_template('user_make_payment.html')

@user.route('/user_view_Veterinary_officials',methods=['get','post'])
def user_view_Veterinary_officials():
	data={}

	r="select * from hospitals"
	data['view']=select(r)
	pid=request.args['pet_id']
	data['pid']=pid
	return render_template('user_view_Veterinary_officials.html',data=data)
@user.route('/user_book_vet_hos', methods=['GET', 'POST'])
def user_book_vet_hos():
    data = {}

    current_date = date.today().strftime('%Y-%m-%d')
    data['current_date'] = current_date

    if 'book' in request.form:
        hid = request.args.get('hid')
        book_date = request.form['book_date']
        pet_id = request.args.get('pid')
        u = "INSERT INTO vet_appointment VALUES (NULL, '%s', '%s', '%s', CURDATE(), '0', 'pending')" % (pet_id, hid, book_date)
        insert(u)
        flash("Appointment Added successfully")
        return redirect(url_for('user_make_hos_payment', pid=pet_id, hid=hid))

    return render_template('user_book_vet_hos.html', data=data)

@user.route('/user_hos_view_appointment')
def user_hos_view_appointment():
	data={}
	s="SELECT * FROM `vet_appointment` INNER JOIN `hospitals` USING(`hospital_id`) INNER JOIN pets ON vet_appointment.pet_id=pets.pet_id WHERE pets.pet_for_id='%s'"%(session['login_id'])
	data['view']=select(s)
	return render_template('user_hos_view_appointment.html',data=data)
@user.route('/user_acc_history')
def user_acc_history():
	data={}
	s="SELECT *,purchase_child.qty as pqty,purchase_master.status as pstatus FROM `purchase_child` inner join purchase_master using(purchase_master_id) INNER JOIN `accessories` USING(`accessorie_id`) where purchase_master.user_id='%s'"%(session['user_id'])
	data['view']=select(s)
	return render_template('user_acc_history.html',data=data)
@user.route('/user_pet_history')
def user_pet_history():
	data={}
	s="SELECT *,sales_child.s_qty as pqty,sales_master.status as pstatus FROM `sales_child` inner join sales_master using(sales_master_id) INNER JOIN `pets` USING(`pet_id`)   where sales_master.user_id='%s'"%(session['user_id'])
	data['view']=select(s)
	return render_template('user_pet_history.html',data=data)
@user.route('/user_make_hos_payment',methods=['get','post'])
def user_make_hos_payment():
	data={}
	purchase_master_id=request.args['pid']
	amount=request.args['amo']
	
	data['amount']=amount
	

	if "payment" in request.form:
		
		q="insert into payment values(null,'%s','%s','vet','%s',curdate())"%(purchase_master_id,session['user_id'],amount)
		insert(q)
		q="update vet_appointment set status='paid' where vet_appointment_id='%s'"%(purchase_master_id)
		update(q)
		flash("Payemnt successfully Completed")
		return redirect(url_for('user.user_home'))
	return render_template('user_make_hos_payment.html')



# @user.route('/user_allocated',methods=['get','post'])
# def user_allocated():
# 	data={}
# 	e="select * from allocation_request where user_id='%s'"%(session['user_id'])
# 	data['view']=select(e)


# 	if "action" in request.args:
# 		action=request.args['action']	
# 		allocation_request_id=request.args['allocation_request_id']

# 	else:
# 		action=None

# 	if action=='ok':
# 		q="update allocation_request set status='ok' where allocation_request_id='%s'"%(allocation_request_id)
# 		update(q)
# 		return redirect(url_for('user.user_allocated'))


# 	if "pet_add" in request.form:
# 		no_days=request.form['no_days']
# 		day=request.form['day']
# 		q="insert into allocation_request values(null,'%s','%s','0',curdate(),'pending','%s','0')"%(day,no_days,session['user_id'])
# 		insert(q)
# 		return redirect(url_for('user.user_allocated'))
	
	
# 	return render_template('user_allocated.html',data=data)
@user.route('/user_add_complaints',methods=['post','get'])
def user_add_complaints():
	data={}
	if 'add' in request.form:	
	   comp=request.form['complaints']
	  
	   e="insert into complaints values(null,'%s','%s','pending',curdate())"%(session['login_id'],comp)
	   res=insert(e)
	e="select * from complaints where login_id='%s'"%(session['login_id'])
	data['view']=select(e)
	return render_template('user_add_complaints.html',data=data)
@user.route('/pet_dt',methods=['get','post'])
def pet_dt():
	data={}
	if "add" in request.form:
		pet=request.form['pet']
		pc=request.form['pc']
		pcc=request.form['pcc']
		ba=request.form['ba']
		bgr=request.form['bgr']
		bu=request.form['bu']
		sc=request.form['sc']
		sod=request.form['sod']
		result=dt.predictsss(pet,pc,pcc,ba,bgr,bu,sc,sod)
		print("resulttttttttttttttttttttttttt is",result)
		print("result",result[0])
		res=result[0]
		u="insert into predict values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(session['user_id'],pet,pc,pcc,ba,bgr,bu,sc,sod,res)
		insert(u)
		data['result']=result
	u="select * from predict where user_id='%s'"%(session['user_id'])
	data['view']=select(u)

		


	return render_template("pet_dt.html",data=data)
@user.route('/user_rate',methods=['get','post'])
def user_rate():
	data={}
	if 'rateing' in request.form:
		rate=request.form['rates']
		review=request.form['review']
		p_image=request.files['p_image']
		path="static/images/"+str(uuid.uuid4())+p_image.filename
		p_image.save(path)

		iss="insert into rating values(null,'%s','%s','%s','%s',curdate())"%(session['user_id'],rate,review,path)
		insert(iss)
	return render_template('user_make_review.html',data=data)
@user.route('/user_payment_report')
def user_payment_report():
	data={}
	t="select * from payment where payment_for_id='%s'"%(session['user_id'])
	data['view']=select(t)
	return render_template('user_payment_report.html',data=data)
	
@user.route('/user_view_petevents',methods=['post','get'])
def user_view_petevents():
	data={}
	d="select * from events"
	data['view']=select(d)
	return render_template('user_view_petevents.html',data=data)