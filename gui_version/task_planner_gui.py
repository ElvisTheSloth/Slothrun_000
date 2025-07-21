"PLAIN CODE TO GUI"
import tkinter as tk
from tkinter import messagebox
from tkinter import font
title_font = ("Times New Roman", 16, "bold")
label_font = ("Times New Roman", 18,)
entry_font = ("Times New Roman", 12)
button_font = ("Times New Roman", 12, "bold")
list_font = ("Times New Roman", 16)
root = tk.Tk()
root.title("Task planner")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text = "WELCOME", font=label_font)
title_label.pack(pady=20)
task_list = []

def updatelist():
    task_display.delete(0, tk.END)
    for task in task_list:
        status = "[X]" if task["complete"] else "[--]"
        task_display.insert(tk.END, f"{status} {task['name']}")

def addtask():
    task_name = entry.get().strip()
    if task_name:
        task_list.append({"name": task_name.lower(), "complete": False})
        entry.delete(0, tk.END)
        updatelist()
        messagebox.showinfo(f"Successful", f"{task_name} has been added to list")
    else:
        messagebox.showwarning("ERROR", "Please enter a task name.")

def complete():
    selected = task_display.curselection()
    if selected:
        index = selected[0]
        task_list[index]["complete"] = True
        updatelist()
        messagebox.showinfo("Task updated successfully!", "Your task has been completed!")
    else:
        messagebox.showwarning("ERROR","No task selected")

def delete():
    selected = task_display.curselection()
    if selected:
        index = selected[0]
        task_list.pop(index)
        updatelist()
        messagebox.showinfo("Task deleted!", "Task no longer exists")
    else:
        messagebox.showwarning("ERROR","No task selected")
            

entry = tk.Entry(root, font=entry_font, width = 30)
entry.pack(pady = 10, padx=5)

button_frame = tk.Frame(root, bg="#ffffff")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", bg="#4CAF50", fg="white", font=button_font, width=12, relief="ridge", command=addtask)
add_button.grid(row=0, column=0, padx=5)

mark_button = tk.Button(button_frame, text="Finish", bg="#2196F3", fg="white", font=button_font, width=12, relief="ridge", command=complete)
mark_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete", bg="#F44336", fg="white", font=button_font, width=12, relief="ridge", command=delete)
delete_button.grid(row=0, column=2, padx=5)

task_display = tk.Listbox(root, bg="#fafafa", fg="#333333", font=list_font, width=50, height=12, bd=1, relief="sunken", selectbackground="#cce5ff")
task_display.pack(pady=20)

root.mainloop()