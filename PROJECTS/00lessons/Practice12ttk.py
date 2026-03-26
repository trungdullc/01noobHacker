"""
Main Purpose:
    17 Ttk widgets
    ttk module gives your application a more modern and improved look

    11 “themed” replacements (from tkinter)
        behave like original tkinter widgets but support modern styling/themes
        ttk.Button
        ttk.Checkbutton
        ttk.Entry
        ttk.Frame
        ttk.Label
        ttk.LabelFrame
        ttk.Menubutton
        ttk.PanedWindow
        ttk.Radiobutton
        ttk.Scale
        ttk.Scrollbar

        tkinter.Canvas      Drawing shapes
        tkinter.Message     Displaying text messages to user
        tkinter.Text        Displaying and editing text

    6 new ttk-only widgets
        These do not exist in classic tkinter
        ttk.Combobox →      dropdown + entry
        ttk.Progressbar →   loading/progress indicator
        ttk.Separator →     horizontal/vertical divider line
        ttk.Sizegrip →      resize handle (bottom-right corner)
        ttk.Treeview →      table / hierarchical data view
        ttk.Notebook →      tabbed interface

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    from tkinter import ttk

Created by HackerDu
"""

import sys
import tkinter
from tkinter import ttk

class MyApp(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("TTK Widgets Demo")
        self.root.geometry("600x500")

        # --- Notebook (tabs) ---
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)

        notebook.add(tab1, text="Controls")
        notebook.add(tab2, text="Treeview")

        # --- Combobox ---
        ttk.Label(tab1, text="Choose an option:").pack(pady=5)
        self.combo = ttk.Combobox(tab1, values=["Option 1", "Option 2", "Option 3"])
        self.combo.current(0)
        self.combo.pack(pady=5)

        # --- Progressbar ---
        self.progress = ttk.Progressbar(tab1, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=10)

        ttk.Button(tab1, text="Start Progress", command=self.start_progress).pack(pady=5)

        # --- Separator ---
        ttk.Separator(tab1, orient="horizontal").pack(fill="x", pady=10)

        # --- Sizegrip ---
        sizegrip = ttk.Sizegrip(tab1)
        sizegrip.pack(side="bottom", anchor="se")

        # --- Treeview ---
        columns = ("Name", "Age")
        self.tree = ttk.Treeview(tab2, columns=columns, show="headings")

        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")

        self.tree.insert("", "end", values=("Alice", 25))
        self.tree.insert("", "end", values=("Bob", 30))
        self.tree.insert("", "end", values=("Charlie", 22))

        self.tree.pack(fill="both", expand=True, pady=10)

        self.mainloop()

    def start_progress(self):
        # Simple progress simulation
        self.progress["value"] = 0
        self.update_progress()

    def update_progress(self):
        if self.progress["value"] < 100:
            self.progress["value"] += 10
            self.root.after(300, self.update_progress)

def main():
    root_window = tkinter.Tk()
    app = MyApp(root_window)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()