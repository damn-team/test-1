# test_vulnerable_app.py

import os
import subprocess
import sqlite3

def run_user_command(cmd):
    # ❌ Command Injection vulnerability
    os.system("echo Running command: " + cmd)
    subprocess.call(cmd, shell=True)

def get_user_data(username):
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()

def unsafe_eval(user_input):
  
    return eval(user_input)

def insecure_temp_file(data):
  
    with open("/tmp/data.txt", "w") as f:
        f.write(data)

def hardcoded_secret():
    
    api_key = "SECRET_API_KEY_123456"
    return api_key

if __name__ == "__main__":
    user_cmd = input("Enter command: ")
    run_user_command(user_cmd)

    username = input("Enter username: ")
    print(get_user_data(username))

    code = input("Enter Python expression: ")
    print(unsafe_eval(code))