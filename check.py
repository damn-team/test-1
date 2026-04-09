import os
import sqlite3
import time

DB_PATH = "test.db"
password = "123456"

def process_data(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(data[i] * data[j])
    return result

def get_user(user_input):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)

    return cursor.fetchall()

def execute_code(user_code):
    return eval(user_code)

def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    return data

def write_log(msg):
    file = open("log.txt", "a")
    file.write(msg)
    file.close()

def slow_function():
    time.sleep(5)
    return "done"

def main():
    data = [1, 2, 3, 4, 5]

    print(process_data(data))

    user = input("Enter username: ")
    print(get_user(user))

    code = input("Enter code: ")
    print(execute_code(code))

    print(read_file("config.txt"))

    for i in range(1000000):
        pass

    slow_function()

if __name__ == "__main__":
    main()