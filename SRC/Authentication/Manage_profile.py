import json
import datetime

from SRC.Authentication.Sign_in import signin
from SRC.Authentication.Sign_up import signup
from SRC.Authentication.Writelogs import writelogs

class AuthenticationManager:
    def __init__(self):
      pass

    def display_menu(self):
            while True:
                print("\n------Wellcome to Rajasthani Thali -----")
                print("1. Sign in")
                print("2. Sign up")
                print("3. Exit")
                
                try:
                    userchoice = int(input("Choose an option: "))
                    if userchoice == 1:
                       object = signin()
                       object.get_signin("admin")
                    elif userchoice == 2:
                        object = signup()
                        object.get_signup("staff")
                    elif userchoice == 3:
                        print("Goodbye!")
                        break
                    else:
                        print("Invalid input. Please enter 1, 2, or 3.")
                except Exception as e:
                    print("\nInvalid input! please enter a number.")
                    data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    logs=json.dumps(data,indent=4)
                    writelogs(logs)