import tkinter as tk
from tkinter import ttk, filedialog
import pickle
import os.path
from tkinter import messagebox
import pool_driver as pd



class PoolGUI:
    n_lines = 4  # initial line count
    pools = ["Pool A", "Pool B", "Pool C", "Rinse"]  # pool selection options

    # lists to keep track of the table
    cbox_list =[]  # comboboxes for pool selection
    ent_list = []  # entries for timing options
    lab_list = []  # number of entries


    def add_line(self):

        self.n_lines += 1  # increase lines count by 1

        # create new label
        lab = ttk.Label(self.frm_table, text=self.n_lines)
        lab.grid(row=self.n_lines+1, column=0)
        self.lab_list.append(lab)

        # create new combobox
        cbox = ttk.Combobox(self.frm_table, values=self.pools, state="readonly")
        cbox.current(0)
        cbox.grid(row=self.n_lines+1, column=1)
        self.cbox_list.append(cbox)

        # create new entry
        ent = ttk.Entry(self.frm_table)
        ent.grid(row=self.n_lines+1, column=2)
        self.ent_list.append(ent)

    def remove_line(self):

        if self.n_lines > 1:  # more than one element in lines count? if yes:

            self.n_lines -= 1  # decrease lines count by 1

            # destroy all widgets of the line from the table
            self.lab_list[self.n_lines].destroy()
            self.cbox_list[self.n_lines].destroy()
            self.ent_list[self.n_lines].destroy()

            # remove the destroyed objects from the lists
            self.lab_list.pop()
            self.cbox_list.pop()
            self.ent_list.pop()

    def validate(self):

        # create red background style
        s = ttk.Style()
        s.configure("Red.TEntry", fieldbackground="red")

        # list for control
        tt=[]

        for i in range(self.n_lines):
            try:  # can in convert to int? yes:
                tt.append(int(self.ent_list[i].get()))  # append int value to tt!
                self.ent_list[i].configure(style="TEntry")

            except:  # no:
                self.ent_list[i].configure(style="Red.TEntry")

        if len(tt) == self.n_lines:  # all lines are int??
            self.btn_start.configure(state="active")
            return True
        else:
            self.btn_start.configure(state="disabled")
            return False

    def start(self):
        if not self.validate():
            print("still errors")
        else:
            print("yeah, lets go")
            pool = pd.make_pool_driver(self.n_lines, self.cbox_list, self.ent_list, self.pools)
            pool.run_experiment()

    def load(self):
        home = os.path.expanduser('~')
        filename = filedialog.askopenfilename(initialdir=home, title="Select file",
                                              filetypes=[("Olympic Pool Files", "*.opl")])
        file = open(filename, "rb")
        obj = pickle.load(file)
        print(obj)
        file.close()
        for i in range(self.n_lines):
            self.cbox_list[i].destroy()
            self.ent_list[i].destroy()
            self.lab_list[i].destroy()

        self.cbox_list = []
        self.ent_list  = []
        self.lab_list  = []

        # create and place the table(comboboxes and entries)
        cb = obj[0]
        et = obj[1]
        self.n_lines = obj[2]
        for i in range(self.n_lines):

            # label for numbering
            lab = ttk.Label(self.frm_table, text=i+1)
            lab.grid(row=i+1, column=0)
            self.lab_list.append(lab)  # <-- store the labels in the list!

            # combobox for selection of pool
            cbox = ttk.Combobox(self.frm_table, values=self.pools, state="readonly")
            cbox.set(cb[i])
            cbox.grid(row=i+1, column=1)
            self.cbox_list.append(cbox)  # <-- store the comboboxes in list!

            # entry for selection of timing
            ent = ttk.Entry(self.frm_table)
            ent.insert(0, et[i])
            ent.grid(row=i+1, column=2)
            self.ent_list.append(ent)  # <-- store the entries in list!

    def save(self):
        cbox = []
        ent  = []
        n    = self.n_lines

        for i in range(n):
            cbox.append(self.cbox_list[i].get())
            ent.append(self.ent_list[i].get())

        home = os.path.expanduser('~')
        filename = filedialog.asksaveasfilename(initialdir=home, title="Select file",
                                                filetypes=[("Olympic Pool Files", "*.opl")])
        file = open(filename, "wb")
        pickle.dump([cbox, ent, n], file)
        file.close()

    def __init__(self, f):
        
        f.title("Pool 2018")

        # create and place main frame-widgets: menu and table
        self.frm_menu = ttk.Frame(f)
        self.frm_menu.grid(row=0, column=0, pady=(0, 10))
        self.frm_table = ttk.Frame(f)
        self.frm_table.grid(row=1, column=0)

        # create menu widgets
        self.btn_add = ttk.Button(self.frm_menu, text="+", command=self.add_line)
        self.btn_delete = ttk.Button(self.frm_menu, text="-", command=self.remove_line)
        self.btn_validate = ttk.Button(self.frm_menu, text="validate", command=self.validate)
        self.btn_start = ttk.Button(self.frm_menu, text="start", state="disabled", command=self.start)
        self.btn_load = ttk.Button(self.frm_menu, text="load", command=self.load)
        self.btn_save = ttk.Button(self.frm_menu, text="save", command=self.save)

        # place menu widgets
        self.btn_add.grid(row=0, column=0)
        self.btn_delete.grid(row=0, column=1)
        self.btn_validate.grid(row=0, column=2, padx=(20, 0))
        self.btn_start.grid(row=0, column=3)
        self.btn_load.grid(row=0, column=4, padx=(20, 0))
        self.btn_save.grid(row=0, column=5)

        # create table widgets
        self.lab_pool = ttk.Label(self.frm_table, text="Pool")
        self.lab_time = ttk.Label(self.frm_table, text="Time [min]")

        # place table widgets
        self.lab_pool.grid(row=0, column=1)
        self.lab_time.grid(row=0, column=2)

        # generate the grid
        for i in range(self.n_lines):

            # label for numbering
            lab = ttk.Label(self.frm_table, text=i+1)
            lab.grid(row=i+1, column=0)
            self.lab_list.append(lab)  # <-- store the labels in the list!

            # combobox for selection of pool
            cbox = ttk.Combobox(self.frm_table, values=self.pools, state="readonly")
            cbox.current(0)
            cbox.grid(row=i+1, column=1)
            self.cbox_list.append(cbox)  # <-- store the comboboxes in list!

            # entry for selection of timing
            ent = ttk.Entry(self.frm_table)
            ent.grid(row=i+1, column=2)
            self.ent_list.append(ent)  # <-- store the entries in list!




root = tk.Tk()
GUI = PoolGUI(root)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
