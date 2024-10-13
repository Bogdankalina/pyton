import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

#=========Create=============
#cur.execute("CREATE TABLE LOGINS (name TEXT, password TEXT);")
connection.commit()

#===========Register=============
enter = input("Напишіть 1 якщо хочете війти Напищіть 2 якщо хочете зарегеструватись   ")
print(enter)

if enter == 1:
    user = input("Введіть нікнейм: ")
    cur.execute(f"SELECT rowid,name FROM USERS name='{user}'")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        print("Не існує цюго ніку")
    else:
        passw = input("Введіть пароль: ")
        cur.execute(f"SELECT rowid,name FROM USERS name='{passw}'")

if enter == 2:
    print("Ви регеструете аккаунт в Хамстер комбат напешіть свій нік та пароль")
    user = input("Введіть Нікнейм: ")
    cur.execute(f"SELECT rowid,name FROM USERS name='{user}'")
    res = cur.fetchall()
    if len(res) == 1:
        print("Вибачне виберіть другий нік такий вже є")
    else:
        passw = input("Введіть пароль: ")
        cur.execute(f"INSERT INTO LOGINS (name, password) VALUES ('{user}', '{passw}');")
        connection.commit()

2
























#===== INSERT =========

#user = input("Username : ")
#passw = input("Password : ")
#cur.execute(f"INSERT INTO LOGINS (name, password) VALUES ('{user}', '{passw}');")
#connection.commit()

#========Select======

#user = input("Username  :")
#cur.execute(f"SELECT rowid,name FROM USERS")
#connection.commit()

#res = cur.fetchall()
#if len(res) == 0:
    #print("User not found!")
#else:
   # print(res[0][1])


#cur.execute(f"UPDATE USERS SET name='Katerina' WHERE rowid=3")






#cur.execute(f"DELETE FROM USERS WHERE rowid=3")


connection.close()
