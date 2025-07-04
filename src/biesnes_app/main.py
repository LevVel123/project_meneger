### Импортируем модули и библиотеки ###
import tkinter as tk
import sqlite3 as sql

### Подключаемя к базе данных и создаем таблицу ###
conn = sql.connect('./src/biesnes_app/database/database.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS project (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,  
            delivery_date TEXT NOT NULL
)''')

### Создаем главное окно приложения ###
root = tk.Tk()
root.geometry('1000x600')
root.title('Biesnes App')
root.configure(bg='#dadba9')

### Добавляем виджеты ###
txt = tk.Text(root)
txt.grid(column=0, row=2, padx=20, pady=20)

lb = tk.Label(text="Cписок проектов: ", font=20, bg='#dadba9')
lb.grid(column=0, row=1)

bt = tk.Button(root, text="Добавить проект", font=20)
bt.grid(column=2, row=1, pady=10)

### Завершаем главный цикл приложения ###
root.mainloop()