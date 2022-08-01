import tkinter as tk 
from tkinter import ttk,messagebox


window=tk.Tk()
window.title('To Do List'),window.geometry('500x600')
window.resizable(False,False)

def add_tasks(*args):
    task=add_task_entry.get()
    if task !='':
        list_tasks.insert(tk.END,task)
        add_task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning(title="Warning!",message="You must enter a Task.")

def del_tasks():
    try:
        task_index=list_tasks.curselection()[0]
        list_tasks.delete(task_index)
    except:
        messagebox.showwarning(title="Warning!",message="You must select a Task.")

banner_lbl=ttk.Label(text='My To Do')
font=('Supermercado',35,'bold')
banner_lbl.config(font=font)
banner_lbl.grid(row=0,column=1,sticky='ew',padx=40)

add_task_lbl=ttk.Label(text='Add New Task')
add_task_lbl.config(font=('Supermercado',15))
add_task_lbl.grid(row=2,column=1,padx=75,pady=10,sticky='ew')

add_task_entry=ttk.Entry()
add_task_entry.config(width=55,justify='right')
add_task_entry.grid(row=3,column=1,pady=5,padx=20,sticky='ew')

add_task_btn=ttk.Button(text='Add',command=add_tasks)
add_task_btn.grid(row=3,column=0,sticky='w',padx=(10,2))
window.bind('<Return>',add_tasks)

del_task_btn=ttk.Button(text='Delete',command=del_tasks)
del_task_btn.grid(row=3,column=1,sticky='w',padx=(0,5))

list_tasks=tk.Listbox(height=26,width=80)
list_tasks.config(justify='right')
list_tasks.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

window.mainloop()