import tkinter as tk
from tkinter import ttk
from threading import Thread
import time


class PoolDriver:
    n_lines = 0
    cbox_list = []
    ent_list = []
    tt = 60

    def __init__(self,lines,cb,et,pls):
        self.n_lines = lines
        self.cbox_list = cb
        self.ent_list = et
        self.pools = pls

    def printer(self):
        print(self.n_lines)
        for i in range(self.n_lines):
            print(self.ent_list[i].get(), " ", self.cbox_list[i].get())

    def run_experiment(self):

        def run_pb(i):
            timer = int(self.ent_list[i].get())*self.tt
            pb[i]["maximum"] = timer
            print(timer)
            for t in range(timer):
                time.sleep(1)
                pb[i]["value"] = t+1
                pb[i].update()
                print(self.tt, t)
                # place your code here
                print("------------         HERE COMES THE CODE!!, every second")
                if self.cbox_list[i].get() == self.pools[0]:
                    print("p1")


                elif self.cbox_list[i].get() == self.pools[1]:
                    print("p2")


                elif self.cbox_list[i].get() == self.pools[2]:
                    print("p3")


                elif self.cbox_list[i].get() == self.pools[3]:
                    print("rns")


                else:
                    print("ERROR!!")

                #print(self.cbox_list[i].get())



                print("------------         End of Loop..")
            print("------------\n")

        for i in range(self.n_lines):
            print(i+1, ":\t ", self.ent_list[i].get(), "\t ", self.cbox_list[i].get())
        print("------------\n")

        slave = tk.Tk()
        slave.title("Pool 2018 - Experiment")
        pb = []
        for i in range(self.n_lines):
            labStr = str(i + 1) + "/" + str(self.n_lines) + "\t"
            ttk.Label(slave, text=labStr).grid(row=i, column=0)

            labStr = self.cbox_list[i].get() + "\t"
            ttk.Label(slave, text=labStr).grid(row=i, column=1)

            labStr = self.ent_list[i].get() + "\t"
            ttk.Label(slave, text=labStr).grid(row=i, column=2)

            self.bar = ttk.Progressbar(slave, length=200, mode="determinate", value=0)
            self.bar.grid(row=i, column=3)
            pb.append(self.bar)

        start_time = time.time()
        for i in range(self.n_lines):
            run_pb(i)
        elapsed_time = time.time()-start_time
        print(elapsed_time)


def make_pool_driver(lines, cb, et, pls):
    pool = PoolDriver(lines, cb, et, pls)
    return pool



