import os
import sqlite3
import time

API_KEY = "sk-123456"
password = "admin123"

def process_data(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(data[i] * data[j])
    return result

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def run_code(user_input):
    return eval(user_input)

def read_config():
    f = open("config.txt", "r")
    return f.read()

def slow_task():
    time.sleep(5)
    return "done"

def main():
    data = [1, 2, 3, 4, 5]
    print(process_data(data))

    user = input("Enter username: ")
    print(get_user(user))

    code = input("Enter code: ")
    print(run_code(code))

    print(read_config())

    for i in range(1000000):
        pass

    slow_task()

if __name__ == "__main__":
    main()
