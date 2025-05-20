import json
import os
import datetime

from SRC.Authentication.Writelogs import writelogs

class signin:
    def __init__(self):
        pass

    def get_signin(self, role):

        role = role.lower()
        
        if role == "admin":
            path = fr"C:\Indixpert_dec_batch24_restaurant_management_system\Src\Database\Admin.json"
        
        elif role == "staff":
            path = fr"C:\Indixpert_dec_batch24_restaurant_management_system\Src\Database\Staff.json"
        
        else:
            print("Invalid!!.")
            return

        if not os.path.exists(path):
            print(f"No {role.capitalize()} data found.")
            return

        with open(path, "r") as file:
            try:
                users = json.load(file)
            except Exception as e:
                print("Data corrupted or empty.",e)
                data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs=json.dumps(data,indent=4)
                writelogs(logs)
                return
            
        self.email = input("Enter the email Id: ")
        self.password = input("Enter the password: ")
    

        for user in users:
            if user["Email"] == self.email and user["Password"] == self.password:
                print(f"\nSign in successful! Welcome {user['Name']}")
                if role == "admin":
                    print("You have full access.")
                else:
                    print("processing.....")
                   
                return
        print("Sign in failed!!")