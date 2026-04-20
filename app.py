import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение за задачи")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        self.title_label = tk.Label(
            root,
            text="Списък със задачи",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=15)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = tk.Entry(self.input_frame, font=("Arial", 12))
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.add_button = tk.Button(
            self.input_frame,
            text="Добави",
            command=self.add_task,
            font=("Arial", 11),
            width=10
        )
        self.add_button.pack(side="right")

        self.listbox = tk.Listbox(root, font=("Arial", 12), height=12)
        self.listbox.pack(padx=20, pady=15, fill="both", expand=True)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.delete_button = tk.Button(
            self.buttons_frame,
            text="Изтрий избрана",
            command=self.delete_task,
            font=("Arial", 11),
            width=15
        )
        self.delete_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(
            self.buttons_frame,
            text="Изчисти всички",
            command=self.clear_tasks,
            font=("Arial", 11),
            width=15
        )
        self.clear_button.grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()

        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Грешка", "Моля, въведете задача.")

    def delete_task(self):
        selected_task = self.listbox.curselection()

        if selected_task:
            self.listbox.delete(selected_task[0])
        else:
            messagebox.showwarning("Грешка", "Моля, изберете задача за изтриване.")

    def clear_tasks(self):
        if self.listbox.size() == 0:
            messagebox.showinfo("Информация", "Няма задачи за изтриване.")
            return

        confirm = messagebox.askyesno(
            "Потвърждение",
            "Сигурни ли сте, че искате да изтриете всички задачи?"
        )

        if confirm:
            self.listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()