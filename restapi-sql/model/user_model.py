print("User Model Loaded")
import mysql.connector
import json
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

    def user_getall_model(self):
        self.cur.execute("select * from users")
        data=self.cur.fetchall()
        print(data)
        #connectuion establishment
       
        return json.dumps(data)
    
    def user_addone_model(self,data):
        self.cur.execute(f"insert into users(name,email,phone,role,password) values('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        print(data['email'])
        return "user created successfully"
        
        
    # put
    def user_update_model(self,data):
        self.cur.execute(
            f"update users set name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' where id={data['id']}")
        if self.cur.rowcount>0:
            return "User updated successfully"
        else:
            return "Nothing to update"
    
    def user_delete_model(self,data):
        self.cur.execute(f"delete from users where id={data['id']}")
        if self.cur.rowcount>0:
            return "User deleted successfully"
        else:
            return "Nothing to delete"
        
        





