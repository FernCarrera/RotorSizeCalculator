import tkinter as tk

class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label="Search",width=5, **kwargs):
        tk.Entry.__init__(self, master,fg = "grey",width=width,**kwargs)
        self.label = label
        self.width = width
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self,event=None):
        if self.get() == self.label:
            self.delete(0, tk.END)

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)