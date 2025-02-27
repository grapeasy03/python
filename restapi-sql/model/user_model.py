print("User Model Loaded")
import mysql.connector
import json
from flask import make_response
class user_model:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="kushagra",
                database="flask"
            )
            self.conn.autocommit=True
            self.cur = self.conn.cursor()
            print("Connection established")  # Now should print when class is instantiated
        except mysql.connector.Error as e:
            print(f"Database Connection Error: {e}")

  
    def user_getall_model(self):  # Remove the 'data' parameter since it's not needed
        self.cur.execute("SELECT * FROM users")
        data = self.cur.fetchall()
        return make_response({"message":data},200)
    
    def user_addone_model(self, data):
        sql = "INSERT INTO users(name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)"
        values = (data['name'], data['email'], data['phone'], data['role'], data['password'])
        self.cur.execute(sql, values)
        self.conn.commit()  # Explicitly commit the transaction
        
        
        new_user_id = self.cur.lastrowid
        
        return make_response({
            "message": "user created successfully",
            "user_details": {
                "id": new_user_id,
                "name": data['name'],
                "email": data['email'],
                "phone": data['phone'],
                "role": data['role']
                # Not returning password for security reasons
            }
        },200)
        
        
    # put
    def user_update_model(self,data):
        self.cur.execute(
            f"update users set name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' where id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfully"},200)
        else:
            return make_response({"message":"Nothing to update"},202)
    
    def user_delete_model(self,data):
        self.cur.execute(f"delete from users where id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"User deleted successfully"},200)
        else:
            return make_response({"message":"Nothing to delete"},202)
    
    def user_patch_model(self,data,id):
        
        qry="UPDATE users SET "
        for key in data:
            qry += f"{key}='{data[key]}', "
        qry = qry[:-2]
        qry += f" where id={id}"
        print(qry)
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"User with id "+id+" updated successfully"},200)
        else:
            return make_response({"message":"Nothing to update"},202)
        
        # update users set col=val,col=val where id={id}
        # return qry[:-2]





