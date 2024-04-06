import sqlite3
import os
from tkinter import *
from my_app import create_app
root = Tk()
font = {"Arial Bold",16}
root.title("main_window")
root.geometry("1000x1000")

#
base_path = "db.db"

def create_base():
    if(os.path.exists(base_path)):
        print("БД есть")
        return
    print("БД нет")
    connect = sqlite3.connect(base_path)
    cur = connect.cursor()

    sql_file = "../sql/sql.sql"
    with open(sql_file,"r") as file:
        print("Читаем sql")
        script = file.read()
        cur.executescript(script)
        connect.commit()
        connect.close()

def insert_data(query,data):
    connect = sqlite3.connect(base_path)
    cur = connect.cursor()
    res = cur.execute(query,data).fetchone() # кортеж
    connect.commit()
    connect.close()
    return res
#
email = StringVar()
password = StringVar()
l_main = Label(root, text="Авторизация",font=font)
create_base()
def auth():
    user = insert_data("SELECT * FROM pacienti WHERE email = ? AND password = ? ",(email.get(),password.get()))
    print(user)
    if user is None:
        l_main.config(text = "Пользователь с таким id: {id} не найден")
        return
    user_id = user[0]
    if(user_id):
        l_main.config(text = "Успешно")
        root.withdraw()
        create_app(root,font,user_props=user)
        return
    l_main.config(text = "Ошибка")

l_email = Label(root, text="Почта",font=font)
l_password = Label(root, text="Пароль",font=font)

e_email = Entry(root, textvariable=email,font=font)
e_password = Entry(root, textvariable=password,font=font)

button = Button(root,text="Авторизоваться",font=font,command=auth)

l_main.grid(row=0,column=1)
l_email.grid(row=1,column=0)
l_password.grid(row=2,column=0)
e_email.grid(row=1,column=2)
e_password.grid(row=2,column=2)
button.grid(row=3,column=1)

if __name__ == " __main__":
    root.mainloop()