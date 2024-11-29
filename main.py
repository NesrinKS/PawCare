from flask import *
from public import public
from admin import admin
from shop import shop
from user import user
from staff import staff
from hospital import hospitals
app=Flask(__name__) 
app.secret_key='abcd'
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(shop)
app.register_blueprint(hospitals)
app.register_blueprint(user)
app.register_blueprint(staff)


app.run(debug=True,port=5002,host="0.0.0.0")