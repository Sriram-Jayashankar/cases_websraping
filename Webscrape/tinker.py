import tkinter as tk
from tkinter import simpledialog
from tkcalendar import DateEntry
from datetime import datetime

class ScrollableFormDialog(simpledialog.Dialog):
    def __init__(self, parent, options):
        self.options = options
        super().__init__(parent)

    def body(self, master):
        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        for option in self.options:
            self.listbox.insert(tk.END, option)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(master, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.from_date_label = tk.Label(master, text="From Date:")
        self.from_date_label.pack()
        self.from_date = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.from_date.pack()

        self.to_date_label = tk.Label(master, text="To Date:")
        self.to_date_label.pack()
        self.to_date = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.to_date.pack()

        return self.listbox  # Focus will be set on the listbox initially

    def apply(self):
        selected_option = self.listbox.get(self.listbox.curselection())
        selected_from_date = self.from_date.get()
        selected_to_date = self.to_date.get()
        selected_from_date = datetime.strptime(selected_from_date, "%m/%d/%y").strftime("%d-%m-%Y")
        selected_to_date = datetime.strptime(selected_to_date, "%m/%d/%y").strftime("%d-%m-%Y")
        print("selected_option:", selected_option)
        print("selected_from_date:", selected_from_date)
        print("selected_to_date:", selected_to_date)
        self.result= [selected_option, selected_from_date, selected_to_date]
        return self.result

# Example usage:
# court_names = ["omommom", "alalalalal"]
# dialog = ScrollableFormDialog(None, court_names)
# result = dialog.result
# print("Result:", result)
