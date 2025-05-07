import json
import datetime

from SRC.Authentication.Sign_in import get_signin
from SRC.Authentication.Sign_up import get_signup

log=fr"C:\Indixpert_dec_batch24_restaurant_management_system\SRC\logs\logs.txt"

class AuthenticationManager:
    def __init__(self):
      pass

    def writelogs(self,logs):
        with open(log, "a") as file:
            file.write(logs + "\n")

    def display_menu(self):
            while True:
                print("\n------ Authentication Menu -----")
                print("1. Sign in")
                print("2. Sign up")
                print("3. Exit")
                
                try:
                    userchoice = int(input("Choose an option: "))
                    if userchoice == 1:
                       object = get_signin()
                       object.signin()
                    elif userchoice == 2:
                        object = get_signup()
                        object.signup()
                    elif userchoice == 3:
                        print("Goodbye!")
                        break
                    else:
                        print("Invalid input. Please enter 1, 2, or 3.")
                except Exception as e:
                    print("\nInvalid input! please enter a number.")
                    data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    logs=json.dumps(data,indent=4)
                    self.writelogs(logs)