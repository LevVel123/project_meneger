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
txt = tk.Text()
txt.grid(column=0, row=2, padx=20, pady=20)

### Завершаем главный цикл приложения ###
root.mainloop()