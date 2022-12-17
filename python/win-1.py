from tkinter import *
def clicked():  
    label.configure(text="Я же просил...")  
 
Window = Tk()     # создаем корневой объект - окно
Window.title("Приложение на Tkinter")     # устанавливаем заголовок окна
Window.geometry("700x700")    # устанавливаем размеры окна
  
label = Label(Window, text="Привет", font=("Arial Bold", 50), fg="red") # создаем текстовую
# метку и устанавливаем шрифт и цвет
label.grid(column=0, row=0) # c начала в верху
# label.pack()    # размещаем метку в окне по центру в верху
btn = Button(Window, text="Не нажимать!", bg="yellow", fg="red", command=clicked)  # Начнем с добавления кнопки
# в окно. Кнопка создается и добавляется в окно так же, как и метка:
btn.grid(column=1, row=0)  
Window.mainloop()