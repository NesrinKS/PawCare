from flask import *
from database import *
import uuid



shop=Blueprint("shop",__name__)

@shop.route('/shop_home')
def shop_home():
	return render_template('shop_home.html')
@shop.route('/shop_manage_pet',methods=['get','post'])
def shop_manage_pet():
	data={}
	if 'pet_add' in request.form:
		pet_name=request.form['pet_name']
		age=request.form['age']
		color=request.form['color']
		breed=request.form['breed']
		price=request.form['price']
		qty=request.form['quantity']
		gender=request.form['gender']
		q="insert into pets values(null,'%s','%s','%s','%s','%s','%s','shop','%s','%s')"%(session['login_id'],pet_name,age,color,breed,gender,qty,price)
		insert(q)
		flash("Added successfully")
		return redirect(url_for('shop.shop_manage_pet'))
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
		return redirect(url_for('shop.shop_manage_pet'))
	if 'update' in request.form:
		pet_name=request.form['pet_name']
		age=request.form['age']
		color=request.form['color']
		breed=request.form['breed']
		price=request.form['price']
		quantity=request.form['quantity']
		gender=request.form['gender']
		
		ww="update pets set pet_name='%s',age='%s',color='%s',breed='%s',gender='%s',qty='%s',price='%s' where pet_id='%s'"%(pet_name,age,color,breed,gender,quantity,price,pet_id)
		update(ww)
		flash("Updated successfully")
		return redirect(url_for('shop.shop_manage_pet'))
			
	s="select * from pets where pet_for_id='%s'"%(session['login_id'])
	data['view']=select(s)


	return render_template('shop_manage_pet.html',data=data)
@shop.route('/shop_add_image',methods=['get','post'])
def shop_add_image():
	data={}
	if 'add' in request.form:
		pid=request.args['pet_id']
		type=request.form['type']
		p_image=request.files['p_image']
		path="static/images/"+str(uuid.uuid4())+p_image.filename
		p_image.save(path)
		u="insert into pet_image values(null,'%s','%s','%s')"%(pid,path,type)
		insert(u)
		return redirect(url_for('shop.shop_manage_pet'))
	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pet_id']
	else:
		action=None
	if action=='delete':
		r="delete from pet_image where pet_image_id='%s'"%(pid)
		delete(r)
		return redirect(url_for('shop.shop_manage_pet'))
	pid=request.args['pet_id']
	s="select * from pet_image where pet_id='%s'"%(pid)
	res=select(s)
	data['view']=res
	if res:

		p_type=res[0]['type']
		data['type']=p_type

	return render_template('user_add_image.html',data=data)
@shop.route('/shop_manage_accessories',methods=['get','post'])
def shop_manage_accessories():
	data={}
	if 'add_acce' in  request.form:
		acces=request.form['acces']
		price=request.form['price']
		qty=request.form['qty']
		image=request.files['image']
		path="static/images/"+str(uuid.uuid4())+image.filename
		image.save(path)
		rr="insert into accessories values(null,'%s','%s','%s','%s','%s')"%(session['shop_id'],acces,price,qty,path)
		insert(rr)
		flash("Added successfully")
		return redirect(url_for('shop.shop_manage_accessories'))
	if 'action' in request.args:
		action=request.args['action']
		acc_id=request.args['acc_id']
	else:
		action=None
	if action=='update':
		d="select * from accessories where accessorie_id='%s'"%(acc_id)
		data['up']=select(d)
	if action=='delete':
		ee="delete from accessories where accessorie_id='%s'"%(acc_id)
		delete(ee)
		flash("deleted successfully")
		return redirect(url_for('shop.shop_manage_accessories'))
	if 'update' in request.form:
		acces=request.form['acces']
		price=request.form['price']
		qty=request.form['qty']
		image=request.files['image']
		path="static/images/"+str(uuid.uuid4())+image.filename
		image.save(path)
		ww="update accessories set accessories='%s',price='%s',quantity='%s',image='%s' where accessorie_id='%s'"%(acces,price,qty,path,acc_id)
		update(ww)
		flash("Updated successfully")
		return redirect(url_for('shop.shop_manage_accessories'))




	e="select * from accessories where shop_id='%s'"%(session['shop_id'])
	data['view']=select(e)	
	return render_template('shop_manage_accessories.html',data=data)

@shop.route('/shop_view_vaccination')
def shop_view_vaccination():
	data={}
	e="select * from vaccine"
	data['view']=select(e)
	return render_template('shop_view_vaccination.html',data=data)

# @shop.route('/shop_send_complaint',methods=['get','post'])
# def shop_send_complaint():
# 	data={}
# 	if 'comp' in request.form:
# 		comp=request.form['comp']
# 		e="insert into complaints values(null,'%s','%s','pending',curdate())"%(session['shop_id'],comp)
# 		insert(e)
# 		flash("Added successfully")
# 		return redirect(url_for('shop.shop_send_complaint'))
# 	e="select * from complaints where shop_id='%s'"%(session['shop_id'])
# 	data['view']=select(e)
# 	return render_template('shop_send_complaint.html',data=data)
@shop.route('/shop_view_booking')
def shop_view_booking():
	data={}
	w="select * from sales_child inner join pets using(pet_id) inner join sales_master using(sales_master_id) INNER JOIN users USING(user_id) where Pet_for_id='%s'"%(session['login_id'])
	data['view']=select(w)
	e="select * from purchase_child inner join purchase_master using(purchase_master_id) inner join users using(user_id) inner join accessories using (accessorie_id) where shop_id='%s'"%(session['shop_id'])
	data['view1']=select(e) 

	return render_template('shop_view_booking.html',data=data)

# @shop.route('/shop_view_payment')
# def shop_view_payment():
# 	data={}
# 	r="SELECT * FROM `payment` WHERE `shop_id`='%s'"%(session['shop_id'])
# 	data['view1']=select(r)
# 	return render_template('shop_view_payment.html',data=data)