import json
import os
import uuid
import datetime

from SRC.Authentication.Writelogs import writelogs

data=uuid.uuid1()
id=str(data)[:6]

class signup:
    def __init__(self):
        self.path = fr"C:\Indixpert_dec_batch24_restaurant_management_system\SRC\Database\Staff.json"
        self.id=id
        self.name=input("Enter your Name:- ")
        self.email=input("Enter your Email Id:- ")
        self.password=input("Enter your password:- ")
        self.role = "staff"
    
    def get_signup(self):
        signupdict={}
        signupdict["Id"]=self.id
        signupdict["Name"]=self.name
        signupdict["Email"]=self.email
        signupdict["Password"]=self.password
        signupdict["Role"] = self.role
        
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                try:
                    SignUp1 = json.load(file)
                except Exception as e:
                    SignUp1 = []
                    data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    logs=json.dumps(data,indent=4)
                    writelogs(logs)
                    
        else:
            SignUp1 = []
        
        SignUp1.append(signupdict)
        print("signup successfully..")
        
        with open(self.path, "w") as file:
            json.dump(SignUp1,file,indent = 4)   