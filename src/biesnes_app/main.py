### Импортируем модули и библиотеки ###
import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox


### Подключаемя к базе данных и создаем таблицу ###
conn = sql.connect('./src/biesnes_app/database/database.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS project (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,  
            delivery_date TEXT NOT NULL
)''')


def validate_fields():
    """Проверяет, что все поля заполнены"""
    if not pole_name.get().strip():
        messagebox.showerror("Ошибка", "Поле 'Имя проекта' не может быть пустым!")
        pole_name.focus_set()  # Устанавливаем фокус на поле
        return False
    
    if not pole_des.get().strip():
        messagebox.showerror("Ошибка", "Поле 'Описание' не может быть пустым!")
        pole_des.focus_set()
        return False
    
    if not pole_dd.get().strip():
        messagebox.showerror("Ошибка", "Поле 'Дата сдачи' не может быть пустым!")
        pole_dd.focus_set()
        return False
    
    return True


### Функция для загрузки и отображения проектов из БД ###
def load_projects():
    # Очищаем текстовое поле перед загрузкой новых данных
    txt.delete(1.0, tk.END)
    
    # Получаем все проекты из БД
    cur.execute("SELECT * FROM project")
    projects = cur.fetchall()
    
    # Если проектов нет - выводим сообщение
    if not projects:
        txt.insert(tk.END, "Список проектов пуст\n")
        return
    
    # Форматируем и выводим каждый проект
    for project in projects:
        project_id, name, description, delivery_date = project
        txt.insert(tk.END, 
                  f"ID: {project_id}\n"
                  f"Название: {name}\n"
                  f"Описание: {description}\n"
                  f"Дата сдачи: {delivery_date}\n"
                  "----------------------------\n")


### Создаем функцию добавления нового проекта ###
def init_new_project_win():
    bt.grid_forget() # Убираем главные виджеты
    txt.grid_forget()
    lb.grid_forget()
    bt2.grid_forget()
    bt_del.grid_forget()

    lb_name.grid(column=0, row=0) # Добавляем новые виджеты
    pole_name.grid(column=0, row=1, padx=300, pady=10)
    lb_des.grid(column=0, row=2)
    pole_des.grid(column=0, row=3, pady=10)
    lb_dd.grid(column=0, row=4, pady=10)
    pole_dd.grid(column=0, row=5)
    bt_new.grid(column=0, row=6, pady=50)
    bt_back.grid(column=0, row=7)


### Добавляем новый проект ###
def init_project():
    if not validate_fields():  # Проверяем перед добавлением
        return
    get_pole_name = pole_name.get()
    get_pole_des = pole_des.get()
    get_pole_dd = pole_dd.get()
    all_p = (get_pole_name, get_pole_des, get_pole_dd)

    cur.execute(f'INSERT INTO project (name, description, delivery_date) VALUES (?, ?, ?)', all_p)
    conn.commit()

    pole_name.delete(0, tk.END)
    pole_des.delete(0, tk.END)
    pole_dd.delete(0, tk.END)
        
    messagebox.showinfo("Успех", "Проект успешно добавлен!")
    load_projects()


### Создаем функцию чтобы вернуться на главную в случае отмены ###
def back():
    lb_name.grid_forget()
    pole_name.grid_forget()
    lb_des.grid_forget()
    pole_des.grid_forget()
    lb_dd.grid_forget()
    pole_dd.grid_forget()
    bt_new.grid_forget()
    bt_back.grid_forget()
    lb_del.grid_forget()
    pole_del.grid_forget()
    bt_del_win.grid_forget()

    txt.grid(column=0, row=2, padx=20, pady=20)
    lb.grid(column=0, row=1)
    bt.grid(column=2, row=1, pady=10)
    bt2.grid(column=2, row=2)
    bt_del.grid(column=2, row=3)


def del_projects_win():
    bt.grid_forget() # Убираем главные виджеты
    txt.grid_forget()
    lb.grid_forget()
    bt2.grid_forget()
    bt_del.grid_forget()

    lb_del.grid(column=0, row=1, padx=300, pady=10)
    pole_del.grid(column=0, row=2, pady=10)
    bt_del_win.grid(column=0, row=3, pady=10)
    bt_back.grid(column=0, row=4, pady=10)


def project_del():
    pole_del_get = pole_del.get()

    cur.execute('DELETE FROM project WHERE id=?', (pole_del_get,))
    conn.commit()

    pole_del.delete(0, tk.END)

    messagebox.showinfo('Успех', 'Проект успешно удален!')

    load_projects()


### Создаем главное окно приложения ###
root = tk.Tk()
root.geometry('1000x600')
root.title('Biesnes App')
root.configure(bg='#dadba9')


### Добавляем главные виджеты ###
txt = tk.Text(root)
txt.grid(column=0, row=2, padx=20, pady=20)
txt.config(state='normal')
lb = tk.Label(text="Cписок проектов: ", font=20, bg='#dadba9')
lb.grid(column=0, row=1)
bt = tk.Button(root, text="Добавить проект", font=20, command=init_new_project_win)
bt.grid(column=2, row=1, pady=10)
bt2 = tk.Button(root, text="Обновить список", font=20, command=load_projects)
bt2.grid(column=2, row=2)
bt_del = tk.Button(root, text="Удалить проект", font=20, command=del_projects_win)
bt_del.grid(column=2, row=3)


### Добавляем виджеты для окна добавления проекта ###
lb_name = tk.Label(root, text="Введите имя проекта:", font=20, bg='#dadba9')
pole_name = tk.Entry(root, width=50, font=20)
lb_des = tk.Label(root, text="Введите краткое описание: ", font=20, bg='#dadba9')
pole_des = tk.Entry(root, width="50", font=20)
lb_dd = tk.Label(root, text="Введите дату сдачи проекта: ", font=20, bg='#dadba9')
pole_dd = tk.Entry(root, width="50", font=20)
bt_new = tk.Button(root, text="Добавить проект", font=20, command=init_project)
bt_back = tk.Button(root, text="Назад", font=20, command=back)


### Добавляем виджеты для окна удаления проекта ###
lb_del = tk.Label(root, text="Введите ID проекта", font=20, bg='#dadba9')
pole_del = tk.Entry(root, width="50", font=20)
bt_del_win = tk.Button(root, text="Удалить проект", font=20, command=project_del)


load_projects()

### Завершаем главный цикл приложения ###
root.mainloop()