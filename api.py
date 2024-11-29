from flask import * 
from database import *
import uuid


api=Blueprint("api",__name__)

@api.route('/login_here',methods=['post'])
def login():
      
   username=request.form['username']
   password=request.form['password']
   Q="select * from login where username='%s' and password='%s'"%(username,password)
   res=select (Q)
   if res:
         login_id=res[0]['login_id']
         if res[0]['user_type']=="user":
            s="select * from users where login_id='%s'"%(login_id)
            rs1=select(s)
            if rs1:
               session['user_id']=rs1[0]['user_id']
            return jsonify(status="ok",login_id=res[0]['login_id'])
         
         else:
            return jsonify(status="failed")
   else:
      return jsonify(status="failed")
@api.route('/signup',methods=['post'])
def signup():
   first_name=request.form['first_name']
   last_name=request.form['last_name']
   phone=request.form['phone']
   place=request.form['place']
   email=request.form['email']
   username=request.form['username']
   password=request.form['password']
   q="insert into login values(null,'%s','%s','user')"%(username,password)
   log=insert(q)
   r="insert into users values(null,'%s','%s','%s','%s','%s','%s')"%(log,first_name,last_name,phone,place,email)
   res=insert(r)
   if res:
      return jsonify(status="ok")
   else:
      return jsonify(status="failed")

@api.route('/update_profile',methods=['post'])
def update_profile():
   lid=request.form['login_id']
   first_name=request.form['fname']
   last_name=request.form['lname']
   phone=request.form['phone']
   place=request.form['place']
   email=request.form['email']
  

   r="update users set first_name='%s',last_name='%s',phone='%s',place='%s',email='%s' where login_id='%s'"%(first_name,last_name,phone,place,email,lid)
   res=update(r)
   if res:
      return jsonify(status="ok")
   else:
      return jsonify(status="failed")
@api.route('/manage_pet',methods=['post'])
def manage_pet():
   login_id=request.form['login_id']
   pet_name=request.form['pet_name']
   age=request.form['age']
   color=request.form['color']
   breed=request.form['breed']
   image=request.files['pic']
   path="static/images/"+str(uuid.uuid4())+image.filename
   image.save(path) 
   price=request.form['price']
   
   r="insert into pets values(null,'%s','%s','%s','%s','%s','%s','user','%s')"%(login_id,pet_name,age,color,breed,path,price)
   res=insert(r)
   if res:
      return jsonify(status="ok")
   else:
      return jsonify(status="failed")

@api.route('/view_profile',methods=['post'])
def view_profile():
   data={}
   login_id=request.form['login_id']
   e="select * from users where login_id='%s'"%(login_id)
   res1=select(e)
   print(login_id)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/view_hospital',methods=['post'])
def view_hospital():
   data={}
   e="select * from hospitals"
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/view_vaccine',methods=['post'])
def view_vaccine():
   data={}
   e="select * from vaccine"
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")

@api.route('/view_accessories',methods=['post'])
def view_accessories():
   data={}
   e="select * from accessories"
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/shop_view_accessories',methods=['post'])
def shop_view_accessories():
   data={}
   shop_id=request.form['sid']
   e="select * from accessories where shop_id='%s'"%(shop_id)
   res1=select(e)
   print("KKKKKKKKKKKKK",shop_id)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/view_pet',methods=['post'])
def view_pet():
   data={}
   e="select * from pets"
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/shop_view_pet',methods=['post'])
def shop_view_pet():
   data={}
   shop_id=request.form['sid']

   e="select * from pets where Pet_for_id=(select login_id from shops where shop_id='%s')"%(shop_id)
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/view_pet2',methods=['post'])
def view_pet2():
   data={}
   login_id=request.form['login_id']
   e="select * from pets where Pet_for_id='%s'"%(login_id)
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/view_shop',methods=['post'])
def view_shop():
   data={}
   e="select * from shops"
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")

@api.route('/petcart',methods=['post'])
def petcart():
   data={}
   pets_id = request.form.get('petsid')
   
   e="select * from pets where pet_id='%s'"%(pets_id)
   
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/addcart',methods=['post'])
def addcart():
   price = request.form.get('price')
   pets_id = request.form.get('petsid')
   login_id = request.form.get('login_id')
   
   e="select * from users where login_id='%s'"%(login_id)
   re=select(e)
   if re:
      user_id=re[0]['user_id']
     
   r="insert into pet_sale values(null,'%s','%s','%s',curdate(),'cart')"%(user_id,pets_id,price)
   insert(r)
   e="select * from pets where pet_id='%s'"%(pets_id)
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")

@api.route('/payment',methods=['post'])
def payment():
   price=request.form['price']
   pet_id=request.form['petsid']
   petforid=request.form['petforid']
   
   t="insert into payment values(null,'%s','%s','pet','%s',curdate())"%(petforid,pet_id,price)
   res=insert(t)
   u="update pets set Status='sold Out' where pet_id='%s'"%(pet_id)
   res=update(u)
   if res:
      return jsonify(status="ok",data=res)
   else:
      return jsonify(status="failed")

@api.route('/acc_cart',methods=['post'])
def acc_cart():
   data={}
   price = request.form.get('price')
   acc_id = request.form.get('accids')
   print("rrrrrrrrrrrrrrr",acc_id)
   login_id = request.form.get('login_id')
   e1="select * from users where login_id='%s'"%(login_id)
   re=select(e1)
   if re:
      user_id=re[0]['user_id']
      r="insert into acc_sale values(null,'%s','%s','%s',curdate(),'cart')"%(user_id,acc_id,price)
      insert(r)
   e="select * from accessories where accessorie_id='%s'"%(acc_id)
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/acc_payment',methods=['post'])
def acc_payment():
   price=request.form['price']
   acc_id=request.form['accids']
   shop_id=request.form['shop_id']
   t="insert into payment values(null,'%s','%s','accessories','%s',curdate())"%(shop_id,acc_id,price)
   res=insert(t)
   if res:
      return jsonify(status="ok",data=res)
   else:
      return jsonify(status="failed")

@api.route('/delete_pet',methods=['post'])
def delete_pet():
   data={}
   pet_id=request.form['petsid']
   e="delete from pets where pet_id='%s'"%(pet_id)
   res4=delete(e)
   if res4:
      return jsonify(status="ok",data=res4)
   else:
      return jsonify(status="failed")
@api.route('/book_slot',methods=['post'])
def book_slot():
   data={}
   vacc_id = request.form.get('vacc_id')
   login_id = request.form.get('login_id')
   date=request.form['date']
   time=request.form['time']
   
   y="select * from users where login_id='%s'"%(login_id)
   r=select(y)
   if r:
      user_id=r[0]['user_id']

   u="insert into slot_booking values(null,'%s','%s','%s','%s','added')"%(user_id,vacc_id,date,time)
   re=insert(u)
   if re:
      return jsonify(status="ok",data=re)
   else:
      return jsonify(status="failed")
@api.route('/complaints',methods=['post'])
def complaints():
   comp=request.form['complaints']
   login_id = request.form.get('login_id')
  
   e="insert into complaints values(null,'%s','%s','pending',curdate())"%(login_id,comp)
   res=insert(e)
   if res:
      return jsonify(status="ok",data=res)
   else:
      return jsonify(status="failed")
@api.route('/view_comp',methods=['post'])
def view_comp():
   data={}
   login_id = request.form.get('login_id')
   e="select * from complaints where login_id='%s'"%(login_id)
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/send_feedback',methods=['post'])
def send_feedback():
   feedback=request.form['feedback']
   login_id = request.form.get('login_id')
  
   e="insert into feedback values(null,(select user_id from users where login_id='%s'),'%s',curdate())"%(login_id,feedback)
   res=insert(e)
   if res:
      return jsonify(status="ok",data=res)
   else:
      return jsonify(status="failed")
@api.route('/view_feedback',methods=['post'])
def view_feedback():
   data={}
   login_id = request.form.get('login_id')
   e="select * from feedback where user_id=(select user_id from users where login_id='%s')"%(login_id)
   res1=select(e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/search_shop',methods=['post'])
def search_shop():
   data={}
   s_place = request.form.get('s_place')
   e="SELECT * FROM `shops` WHERE`s_place` LIKE '%s'"%(s_place)
   res1=select(e)
   print("kkkkkkkkkkkkkkkkkkkkkkkk",e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")
@api.route('/search_hospital',methods=['post'])
def search_hospital():
   data={}
   h_place = request.form.get('h_place')
   e="SELECT * FROM `hospitals` WHERE`h_place` LIKE '%s'"%(h_place)
   res1=select(e)
   print("kkkkkkkkkkkkkkkkkkkkkkkk",e)
   if res1:
      return jsonify(status="ok",data=res1)
   else:
      return jsonify(status="failed")

    
