from flask import *
from database import *
import uuid



hospitals=Blueprint("hospitals",__name__)

@hospitals.route('/hospitals_home')
def hospitals_home():
	return render_template('hospitals_home.html')
@hospitals.route('/hospital_profile')
def hospital_profile():
	data={}
	r="select * from hospitals where login_id='%s'"%(session['login_id'])
	data['view']=select(r)
	return render_template('hospital_profile.html',data=data)
@hospitals.route('/hospital_manage_slot',methods=['post','get'])
def hospital_manage_slot():
	data={}
	d="select * from hospitals"
	data['hosp']=select(d)
	e="select * from vaccine"
	data['vacc']=select(e)
	if 'addslot' in request.form:
		
		v_name=request.form['v_name']
		slot=request.form['slot']
		qty=request.form['qty']
		w="insert into slots values(null,'%s','%s','%s','%s')"%(session['hospital_id'],v_name,slot,qty)
		insert(w)
		return redirect(url_for('hospitals.hospital_manage_slot'))
	if 'action' in request.args:
		action=request.args['action']
		slot_id=request.args['slot_id']
	else:
		action=None
	if action=='delete':
		e="delete from slots where slot_id='%s'"%(slot_id)
		delete(e)
		return redirect(url_for('hospitals.hospital_manage_slot'))
	if action=='update':
		r1="select * from slots where slot_id='%s'"%(slot_id)
		data['up']=select(r1)
	if 'update' in request.form:
		v_name=request.form['v_name']
		slot=request.form['slot']
		qty=request.form['qty']
		ee="update slots set vaccine_id='%s',slot='%s',quantity='%s' where slot_id='%s'"%(v_name,slot,qty,slot_id)
		update(ee)
		return redirect(url_for('hospitals.hospital_manage_slot'))
	g="select * from slots inner join vaccine using(vaccine_id) where hospital_id='%s'"%(session['hospital_id'])
	data['view']=select(g)
	return render_template('hospital_manage_slot.html',data=data)
@hospitals.route('/hospital_View_appo')
def hospital_View_appo():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		s_id=request.args['vid']
	else:
		action=None
	if action=='accept':
		u="update vet_appointment set status='accept' where vet_appointment_id='%s'"%(s_id)
		update(u)
		return redirect(url_for('hospitals.hospital_View_appo'))
	if action=='reject':
		r="update vet_appointment set status='reject' where vet_appointment_id='%s'"%(s_id)
		update(r)
		return redirect(url_for('hospitals.hospital_View_appo'))
	e="select * from vet_appointment inner join pets on vet_appointment.pet_id=pets.pet_id inner join users on pets.Pet_for_id=users.login_id where vet_appointment.hospital_id='%s'"%(session['hospital_id'])
	data['view']=select(e)
	return render_template('hospital_View_appo.html',data=data)
@hospitals.route('/hos_addamount',methods=['get','post'])
def hos_addamount():
	data={}
	vid=request.args['vid']
	

	if "pet_add" in request.form:
		amount=request.form['amount']

		q="update vet_appointment set amount='%s' , status='addamount' where vet_appointment_id='%s'"%(amount,vid)
		update(q)
		print(q)
		return redirect(url_for('hospitals.hospitals_home'))
		
	return render_template('hos_addamount.html',data=data)
