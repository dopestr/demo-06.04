from tkinter import *
import sqlite3
import os

def create_app(root,font,user_props):
    app = Toplevel(root)
    app.title("Онлайн")
    app.geometry("1000x1000")
    l_main = Label(app,font=font, text="Онлайн")
    l_main.grid(row=0,column=1)
    l_pacienti = Label(app,font=font, text="пациент")
    l_pacienti.grid(row=1,column=1)
    #
    def insert_data(query,data):
        base_path = "database.db"
        connect = sqlite3.connect(base_path)
        cur = connect.cursor()
        res = cur.execute(query,data).fetchone() # кортеж
        connect.commit()
        connect.close()
        return res
    id = StringVar()
    first_name = StringVar()
    l_name = StringVar()
    middle_name = StringVar()
    passport_number = StringVar()
    date_of_birth = StringVar()
    gender = StringVar()
    address = StringVar()
    phone = StringVar()
    email = StringVar()
    medical_card_number = StringVar()
    date_of_issue_of_medical_card = StringVar()
    data_medic_card = StringVar()
    data_next_visit = StringVar()
    insurance_policy_number = StringVar()
    insurance_policy_end_date = StringVar()


    # def get_users():
    #     l_main.config(text = "Ввести нужно все данные иначе будет ошибка. Сидеть вечно тут и обрабатывать каждую я не могу")
    #     users = insert_data("SELECT * FROM pacienti ",())
    #     if users is None:
    #         l_main.config(text = "Пользователей нет")
    #         return
    #     if(users):
    #         l_main.config(text = "Успешно")
    #         print(users)
    #         return
    #     l_main.config(text = "Ошибка")

    def get_user():
        l_main.config(text = "Введите данные")
        user = insert_data("SELECT * FROM pacienti WHERE id = ? ",(id.get()))
        print(user)
        if user is None:
            l_main.config(text = "Пользователь с таким id: {id} не найден")
            return
        user_id = user[0]
        if(user_id):
            l_main.config(text = "Успешно")
            return
        l_main.config(text = "Ошибка")

    def new_user():
        fields = []
        values = []
        if(first_name is not None):
            fields.append("first_name")
            values.append(f"'{first_name}")
        if(l_name is not None):
            fields.append("l_name")
            values.append(f"'{l_name}")
        if(middle_name is not None):
            fields.append("middle_name")
            values.append(f"'{middle_name}")
        if(passport_number is not None):
            fields.append("passport_number")
            values.append(f"'{passport_number}")
        if(date_of_birth is not None):
            fields.append("date_of_birth")
            values.append(f"'{date_of_birth}")
        if(gender is not None):
            fields.append("gender")
            values.append(f"'{gender}")
        if(address is not None):
            fields.append("address")
            values.append(f"'{address}")
        if(phone is not None):
            fields.append("phone")
            values.append(f"'{phone}")
        if(email is not None):
            fields.append("email")
            values.append(f"'{email}")
        if(medical_card_number is not None):
            fields.append("medical_card_number")
            values.append(f"'{medical_card_number}")
        if(number_medic_card is not None):
            fields.append("number_medic_card")
            values.append(f"'{number_medic_card}")
        if( date_of_issue_of_medical_car is not None):
            fields.append(" date_of_issue_of_medical_car")
            values.append(f"'{ date_of_issue_of_medical_car}")
        if(data_medic_card is not None):
            fields.append("data_medic_card")
            values.append(f"'{data_medic_card}")
        if(data_next_visit is not None):
            fields.append("data_next_visit")
            values.append(f"'{data_next_visit}")
        if(insurance_policy_number is not None):
            fields.append("insurance_policy_number")
            values.append(f"'{insurance_policy_number}")
        if(insurance_policy_end_date is not None):
            fields.append("insurance_policy_end_date")
            values.append(f"'{insurance_policy_end_date}")
        fields = ", ".join(fields)
        values = ", ".join(values)
        user = insert_data(f"""INSERT INTO pacienti ({fields}) VALUES ({values}) RETURNING id""",())
        print(user)
        if user is None:
            l_main.config(text = "Ошибка")
            return
        user_id = user[0]
        if(user_id):
            l_main.config(text = "Успешно")
            create_app(app,font,user_props=user)
            return
        l_main.config(text = "Ошибка")

    def upd_user():
        l_main.config(text = "")

    def del_user():
        l_main.config(text = "Введи необходимые данные")
        user = insert_data("DELETE FROM pacienti WHERE id = ? RETURNING id",(id.get()))
        print(user)
        if user is None:
            l_main.config(text = "Пользователь с таким id: {id} не найден")
            return
        user_id = user[0]
        if(user_id):
            l_main.config(text = "Успешно")
            create_app(app,font,user_props=user)
            return
        l_main.config(text = "Ошибка")

    b_pacienti_get = Button(app,font=font, text="Получить пациента",command=get_user)
    # b_pacienti_gets = Button(app,font=font, text="Получить пациентов",command=get_users)
    b_pacienti_new = Button(app,font=font, text="Создать пациента",command=new_user)
    b_pacienti_upd = Button(app,font=font, text="Обновить пациента",command=upd_user)
    b_pacienti_del = Button(app,font=font, text="Удалить пациента",command=del_user)
    b_pacienti_get.grid(row=2,column=0)
    b_pacienti_gets.grid(row=2,column=4)
    b_pacienti_new.grid(row=2,column=1)
    b_pacienti_upd.grid(row=2,column=2)
    b_pacienti_del.grid(row=2,column=3)

    idl = Label(app,font=font, text="id")
    ide = Entry(app, textvariable=id,font=font)
    idl.grid(row=3,column=0)
    ide.grid(row=3,column=1)
    first_name1 = Label(app,font=font, text="first_name")
    first_name = Entry(app, textvariable=name,font=font)
    first_name1.grid(row=4,column=0)
    first_name.grid(row=4,column=1)
    l_name1 = Label(app,font=font, text="l_name")
    l_name2 = Entry(app, textvariable=familiya,font=font)
    l_name1.grid(row=5,column=0)
    l_name.grid(row=5,column=1)
    middle_name = Label(app,font=font, text="middle_name")
    middle_name1 = Entry(app, textvariable=otchestvo,font=font)
    middle_name1.grid(row=6,column=0)
    middle_name2.grid(row=6,column=1)
    passport_number1 = Label(app,font=font, text="passport_number")
    passport_number2 = Entry(app, textvariable=number_seria_pasport,font=font)
    passport_number2.grid(row=7,column=0)
    passport_number2.grid(row=7,column=1)
    date_of_birth1 = Label(app,font=font, text="date_of_birth")
    date_of_birth2 = Entry(app, textvariable=data_rojdeniya,font=font)
    date_of_birth1.grid(row=8,column=0)
    date_of_birth2.grid(row=8,column=1)
    gender1 = Label(app,font=font, text="gender")
    gender2 = Entry(app, textvariable=pol,font=font)
    gender1.grid(row=9,column=0)
    gender2.grid(row=9,column=1)
    address1 = Entry(app, textvariable=address,font=font)
    address2 = Label(app,font=font, text="address")
    address1.grid(row=10,column=1)
    address2.grid(row=10,column=0)
    phone1 = Entry(app, textvariable=number,font=font)
    phone2 = Label(app,font=font, text="phone")
    phone1.grid(row=11,column=1)
    numberl.grid(row=11,column=0)
    emaill = Label(app,font=font, text="email")
    emaile = Entry(app, textvariable=email,font=font)
    emaill.grid(row=12,column=0)
    emaile.grid(row=12,column=1)
    passwordl = Label(app,font=font, text="password")
    passworde = Entry(app, textvariable=password,font=font)
    passwordl.grid(row=13,column=0)
    passworde.grid(row=13,column=1)
    medical_card_number1 = Label(app,font=font, text="medical_card_number")
    medical_card_number2 = Entry(app, textvariable=number_medic_card,font=font)
    medical_card_number1.grid(row=14,column=0)
    medical_card_number2.grid(row=14,column=1)
    number_medic_card1 = Label(app,font=font, text="number_medic_card")
    number_medic_card2 = Entry(app, textvariable=data_medic_card,font=font)
    1umber_medic_card1.grid(row=15,column=0)
    number_medic_card2.grid(row=15,column=1)
    data_last_obrascheniyal = Label(app,font=font, text="data_last_obrascheniya")
    data_last_obrascheniyae = Entry(app, textvariable=data_last_obrascheniya,font=font)
    data_last_obrascheniyal.grid(row=16,column=0)
    data_last_obrascheniyae.grid(row=16,column=1)
    data_next_visitl = Label(app,font=font, text="data_next_visit")
    data_next_visite = Entry(app, textvariable=data_next_visit,font=font)
    data_next_visitl.grid(row=17,column=0)
    data_next_visite.grid(row=17,column=1)
    insurance_policy_number1 = Label(app,font=font, text="insurance_policy_number")
    insurance_policy_number2 = Entry(app, textvariable=number_polis,font=font)
    insurance_policy_number.grid(row=18,column=0)
    number_polise.grid(row=18,column=1)
    insurance_policy_end1 = Label(app,font=font, text="insurance_policy_end_date")
    insurance_policy_end2 = Entry(app, textvariable=data_okonchaniya_polis,font=font)
    insurance_policy_end1.grid(row=19,column=0)
    insurance_policy_end2.grid(row=19,column=1)
