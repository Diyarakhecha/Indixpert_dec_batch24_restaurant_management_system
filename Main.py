import sys
import os
sys.path.append(os.getcwd())

from SRC.Authentication.Manage_profile import AuthenticationManager

app = AuthenticationManager()
app.display_menu()