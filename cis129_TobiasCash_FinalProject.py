# Tobias Cash
# cis_129
# Final Project: Vineyard Manager
# This code is a first draft for the Vineyard Manager program.
# This program can map a vineyard, assign health status to plants,
# manage and schedule tasks and will be further developed with possibility
# of more functions.


import tkinter as tk
from tkinter import simpledialog, messagebox, ttk, Listbox, Scrollbar
from datetime import datetime, timedelta

def get_task_status_color(due_date):
    """Return color based on task status compared to the current date"""
    today = datetime.now().date()
    if due_date < today:
        return "red"  # Overdue
    elif (due_date - today).days <= 2:
        return "yellow"  # Due soon
    else:
        return "green"  # On schedule

class TaskManager(tk.Toplevel):
    """Manage tasks within a block"""
    def __init__(self, master, block_name, block_tasks):
        super().__init__(master)
        self.title(f"Tasks for {block_name}")
        self.geometry("400x300")
        self.block_tasks = block_tasks
        self.create_ui()

    def create_ui(self):
        """set up user interface for managing tasks"""
        self.task_entry = ttk.Entry(self)
        self.task_entry.pack(pady=10)
        self.add_task_button = ttk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)
        self.tasks_frame = ttk.Frame(self)
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)
        self.update_task_display()

    def add_task(self):
        """Add a new task to the block"""
        task_name = self.task_entry.get()
        task_type = simpledialog.askstring("Task Type", "Enter task type (one-time or recurring):", parent=self)
        if task_type and task_type.lower() == "one-time":
            due_date_str = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):", parent=self)
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                self.block_tasks.append({'name': task_name, 'due_date': due_date, 'type': 'one-time'})
                self.update_task_display()
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.", parent=self)
        elif task_type and task_type.lower() == "recurring":
            period_days = simpledialog.askinteger("Period Days", "Enter the recurrence period in days:", parent=self)
            if period_days:
                due_date = datetime.now().date() + timedelta(days=period_days)
                self.block_tasks.append({'name': task_name, 'due_date': due_date, 'type': 'recurring', 'period_days': period_days})
                self.update_task_display()
        else:
            messagebox.showerror("Error", "Task type must be 'one-time' or 'recurring'.", parent=self)

    def update_task_display(self):
        """update display of tasks in the task manager"""
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        for task in self.block_tasks:
            task_color = get_task_status_color(task['due_date'])
            ttk.Label(self.tasks_frame, text=f"{task['name']} - Due: {task['due_date']}", background=task_color).pack()

class VineyardApp(tk.Tk):
    """main application"""
    def __init__(self):
        super().__init__()
        self.title("Vineyard Manager by Tobias Cash")
        self.geometry("1024x768")
        self.blocks = {}
        self.selected_block = None
        self.plant_status_colors = {1: "green", 2: "yellow", 3: "red"}
        self.create_ui()
    def create_ui(self):
        """setup main ui components"""
        self.left_panel = ttk.Frame(self, width=200)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.add_block_button = ttk.Button(self.left_panel, text="Add Block", command=self.add_block)
        self.add_block_button.pack(pady=10)
        self.block_listbox = Listbox(self.left_panel, exportselection=False)
        self.block_listbox.pack(fill=tk.BOTH, expand=True)
        self.block_listbox.bind("<<ListboxSelect>>", self.on_block_selected)
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=10, pady=10)

    def add_block(self):
        """add new block"""
        block_name = simpledialog.askstring("Block Name", "Enter the name of the new block:", parent=self)
        if block_name:
            self.blocks[block_name] = {'rows': [], 'tasks': []}
            self.block_listbox.insert(tk.END, block_name)

    def on_block_selected(self, event):
        """handle changes"""
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.selected_block = event.widget.get(index)
            self.update_ui()

    def update_ui(self):
        """update main frame ui to reflect the selected block's details"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        if self.selected_block:
            ttk.Button(self.main_frame, text="Manage Tasks", command=lambda: self.manage_tasks(self.selected_block)).pack(pady=20)
            ttk.Button(self.main_frame, text="Add Row", command=self.add_row).pack()
            self.display_urgent_tasks()
            self.display_rows()

    def add_row(self):
        """add new row of plants to block"""
        if not self.selected_block:
            messagebox.showerror("Error", "No block selected.", parent=self)
            return
        num_plants = simpledialog.askinteger("Number of Plants", "How many plants in this row?", minvalue=1, parent=self)
        if num_plants:
            new_row = {'plants': [{'status': 1} for _ in range(num_plants)]}
            self.blocks[self.selected_block]['rows'].append(new_row)
            self.update_ui()

    def manage_tasks(self, selected_block):
        """open task manager for selected block"""
        if selected_block:
            TaskManager(self, selected_block, self.blocks[selected_block]['tasks'])

    def display_urgent_tasks(self):
        """display urgent tasks for quick overview of main frame"""
        urgent_tasks = [task for task in self.blocks[self.selected_block]['tasks'] if get_task_status_color(task['due_date']) != 'green']
        if urgent_tasks:
            urgent_tasks_frame = ttk.Frame(self.main_frame)
            urgent_tasks_frame.pack(fill=tk.X)
            ttk.Label(urgent_tasks_frame, text="Urgent Tasks:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
            for task in urgent_tasks:
                task_color = get_task_status_color(task['due_date'])
                ttk.Label(urgent_tasks_frame, text=f"{task['name']}", background=task_color).pack(side=tk.LEFT, padx=5)

    def display_rows(self):
        """display rows of plants in selected blocks"""
        block_info = self.blocks[self.selected_block]
        for row in block_info['rows']:
            row_frame = tk.Frame(self.main_frame)
            row_frame.pack(fill=tk.X, pady=5)
            for i, plant in enumerate(row['plants'], start=1):
                plant_status = self.plant_status_colors[plant['status']]
                plant_btn = tk.Button(row_frame, text=f"{i}", bg=plant_status, width=2)
                plant_btn.pack(side=tk.LEFT, padx=2)
                # Bind the button click event
                plant_btn.bind('<Button-1>', lambda event, p=plant, b=plant_btn: self.change_plant_status(p, b))
                if i % 4 == 0 and i != len(row['plants']):
                    separator = tk.Label(row_frame, text='|', foreground='black')
                    separator.pack(side=tk.LEFT, padx=2)

    def change_plant_status(self, plant, button):
        """change status of a plant and update its visual representation"""
        # Cycle through the statuses
        new_status = plant['status'] % len(self.plant_status_colors) + 1
        plant['status'] = new_status
        # Update the button's background color
        button.config(bg=self.plant_status_colors[new_status])


if __name__ == "__main__":
    app = VineyardApp()
    app.mainloop()
