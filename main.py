from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from tkinter import filedialog
from tkinter import scrolledtext
import io


# Функция калькулятора

def clicked():
    a = int(txt.get())
    b = int(txt1.get())
    if combo.get() == '+':
        res = a + b
    elif combo.get() == '-':        
        res = a - b
    elif combo.get() == '*':
        res = a * b
    elif combo.get() == '/':
        res = a / b
    lbl.configure(text=res)
    
# Функция Чек_баттон

def check_bu():
    if chk1.get() == 1 and chk2.get() == 0 and chk3.get() == 0: messagebox.showinfo('Опа','Вы выбрали первый вариант')
    elif chk1.get() == 0 and chk2.get() == 1 and chk3.get() == 0: messagebox.showinfo('Опа','Вы выбрали второй вариант')
    elif chk1.get() == 0 and chk2.get() == 0 and chk3.get() == 1: messagebox.showinfo('Опа','Вы выбрали третий вариант')
    elif chk1.get() == 1 and chk2.get() == 1 and chk3.get() == 0: messagebox.showinfo('Опа','Вы выбрали первый и второй варианты')
    elif chk1.get() == 1 and chk2.get() == 0 and chk3.get() == 1: messagebox.showinfo('Опа','Вы выбрали первый и третий варианты')
    elif chk1.get() == 0 and chk2.get() == 1 and chk3.get() == 1: messagebox.showinfo('Опа','Вы выбрали второй и третий варианты')
    elif chk1.get() == 1 and chk2.get() == 1 and chk3.get() == 1: messagebox.showinfo('Опа','Вы выбрали все варианты')
    
# Функция загрузки и чтения файла

def load_file():
    
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with io.open(filepath, encoding='utf-8') as file:
            stxt = file.read()
            scr_txt.insert("1.0", stxt)
        
    
# Форматирование окна

window = Tk()
window.title('Жуков Владислав Вячеславович')
window.geometry('600x300')

# Настройка вкладок

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Файл')
tab_control.pack(expand=1, fill='both')

# Настройка первой вкладки

txt = Entry(tab1, width=5, font='Arial 14')
txt1 = Entry(tab1, width=5, font='Arial 14')
combo = Combobox(tab1, width = 2, font='Arial 14')
combo['values'] = ('+', '-', '*', '/')
combo.grid(column=1, row = 0)
combo.get()

lbl = Label(tab1, text="", font='Arial 14')
lbl.grid(column=4, row=0)

txt.grid(column=0, row = 0)
txt1.grid(column=2, row = 0)

btn = Button(tab1, text="=", command=clicked)
btn.grid(column=3, row=0)


# Настройка второй вкладки

chk1 = IntVar()
chk1.set(0)
chk1_button = Checkbutton(tab2, text='Первый', var=chk1)

chk2 = IntVar()
chk2.set(0)
chk2_button = Checkbutton(tab2, text='Второй', var=chk2)

chk3 = IntVar()
chk3.set(0)
chk3_button = Checkbutton(tab2, text='Третий', var=chk3)

chk1_button.grid(column=0,row=0)
chk2_button.grid(column=0,row=1)
chk3_button.grid(column=0,row=2)

btn = Button(tab2, text='Какая кнопка?', command=check_bu)
btn.grid(column=1, row=1)

# Настройка третьей вкладки

btn = Button(tab3, text='Загрузить файл', command=load_file)
btn.grid(column=0, row=0)

scr_txt = Text(tab3)
scr_txt.grid(column=0, row=1)

# Вызов окна
window.mainloop()
