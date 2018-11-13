# # -*- coding: utf-8 -*-
# import tkinter.ttk as ttk
# import tkinter as tk
# from threading import Thread
# import time
#
# class Main(object):
#     def __init__(self, master):
#         self.master = master
#
#         self.frame = tk.Frame(self.master, width=400, height=400)
#         self.frame.pack(expand=True)
#
#         self.button = tk.Button(self.frame, text="Add Bar", command=self.start_thread)
#         self.button.pack(fill="y")
#
#     def start_thread(self):
#         self.t = Thread(target=self.add_bar)
#         self.t.start()
#
#     def add_bar(self):
#         var = tk.IntVar()
#         var.set(0)
#
#         progessbar = ttk.Progressbar(self.frame, variable=var, orient=tk.HORIZONTAL, length=200)
#         progessbar.pack()
#
#         self.add_values(var)
#
#     def add_values(self, var):
#         variable = var
#         for x in range(100):
#             time.sleep(1)
#             print(x)
#             variable.set(x)
#
#
# root = tk.Tk()
# app = Main(root)
# root.mainloop()





# -------------------------------------------

import time
import threading
try:
    import Tkinter as tkinter
    import ttk
except ImportError:
    import tkinter
    from tkinter import ttk


class GUI(object):

    def __init__(self):
        self.root = tkinter.Tk()

        self.progbar = ttk.Progressbar(self.root)
        self.progbar.config(maximum=100, mode='determinate')
        self.progbar.pack()
        self.i = 0
        self.b_start = ttk.Button(self.root, text='Start')
        self.b_start['command'] = self.start_thread
        self.b_start.pack()

    def start_thread(self):
        self.b_start['state'] = 'disable'
        self.work_thread = threading.Thread(target=work)
        self.work_thread.start()
        self.root.after(50, self.check_thread)
        self.root.after(50, self.update)

    def check_thread(self):
        if self.work_thread.is_alive():
            self.root.after(50, self.check_thread)
        else:
            self.root.destroy()


    def update(self):
        #Updates the progressbar
        self.progbar["value"] = self.i
        if self.work_thread.is_alive():
            self.root.after(50, self.update)#method is called all 50ms

gui = GUI()

def work():
    #Do your work :D
    for i in range(150):
        gui.i = i
        time.sleep(0.1)
        print(i)


gui.root.mainloop()