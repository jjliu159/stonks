import tkinter as tk
from tkinter import ttk


def text(news_list,company_name):
    window = tk.Tk()

    pw = tk.PanedWindow()
    pw.pack(fill="both", expand=True)

    window.title("Stock News")
    window.minsize(600,600)

    text = tk.Text(window,height=50,width=150)
    text.config(state = "normal")

    pw.add(text)
    
    for i in range(len(news_list)):
        if i != 0:
            text.insert(tk.INSERT,"\n")
        text.insert(tk.INSERT,company_name[i])
        text.insert(tk.INSERT,"\n")
        for k in range(len(news_list[i])):
            text.insert(tk.INSERT,news_list[i][k])
            text.insert(tk.INSERT,"\n")

    text.pack()
    window.mainloop()
