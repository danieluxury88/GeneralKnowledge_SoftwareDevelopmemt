import os
import tkinter as tk
from tkinter import filedialog, ttk

results_table = None
folder_path = None
search_text = None
path = None


class SearchResults(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        # Create search results table
        self.table = ttk.Treeview(self, columns=("line", "filename", "path", "no_line"))
        self.table.heading("line", text="Line")
        self.table.heading("filename", text="Filename")
        self.table.heading("path", text="Path")
        self.table.heading("no_line", text="Line Number")
        self.table.column("line", width=400)
        self.table.column("filename", width=200)
        self.table.column("path", width=400)
        self.table.column("no_line", width=100)
        self.table.pack(padx=10, pady=10, fill="both", expand=True)

        # Add scrollbars to table
        self.xscrollbar = tk.Scrollbar(
            self, orient="horizontal", command=self.table.xview
        )
        self.xscrollbar.pack(side="bottom", fill="x")
        self.yscrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.table.yview
        )
        self.yscrollbar.pack(side="right", fill="y")
        self.table.configure(
            xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set
        )

    def add_result(self, line, filename, path, no_line):
        self.table.insert("", tk.END, values=(line, filename, path, no_line))


def search_files():
    global search_text
    search_text = search_box.get()
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r") as f:
                    for i, line in enumerate(f):
                        if search_text in line:
                            results_table.add_result(line, file, file_path, i + 1)
            except:
                pass


def search_folder():
    global path
    global search_text
    path = filedialog.askdirectory()
    search_text = search_box.get()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root

    # Create search window
    search_window = tk.Tk()
    search_window.title("Search Files")
    search_window.geometry("800x1000")

    # Folder selection button
    folder_button = tk.Button(
        search_window, text="Select Folder", command=search_folder
    )
    folder_button.pack(pady=10)

    search_label = tk.Label(search_window, text="Enter text to search:")
    search_label.pack(pady=5)
    search_box = tk.Entry(search_window)
    search_box.pack()

    # Search button
    search_button = tk.Button(search_window, text="Search", command=search_files)
    search_button.pack(pady=10)

    # Add search results table
    results_table = SearchResults(search_window)

    search_window.mainloop()
