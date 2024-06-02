import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Todo App")
root.geometry('400x500')
root.resizable(False,False)
root.iconbitmap('image1.ico')

task_list = []

def add_task(event):
    task = task_entry.get()
    task_entry.delete(0,tk.END)
    if task:
        with open('tasklist.txt', 'a') as file:
            file.write(task)
        
        listbox.insert(tk.END,task)
        task_list.append(task)
        
def delete_task():
    task = listbox.get()
    task = listbox.get(tk.ANCHOR)
    listbox.delete(tk.ANCHOR)
    task_list.remove(task)
        

heading = ttk.Label(root, text='ALL TASKS',font='arial 20 bold')
heading.pack()
frame = ttk.Frame(root,width=400, height=50)
frame.pack(pady=25)
task_entry = ttk.Entry(frame, font='arial 18' , width=25)
task_entry.pack()

task_entry.bind("<Return>",add_task)

frame1= ttk.Frame(root, width=300, height=250)
frame1.pack()

listbox = tk.Listbox(frame1, font='arial 12', width=40 ,height=16)
listbox.pack()

s = ttk.Style()
s.configure('TButton', font=('arial',12))

deletebutton = ttk.Button(root, text='Delete',style='TButton', command=delete_task)

deletebutton.pack(side='bottom',pady='12', ipadx=10,ipady=15 )


root.mainloop()
