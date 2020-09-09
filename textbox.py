import tkinter as tk
from tkinter import ttk
import webbrowser

def callback(url):
    webbrowser.open_new(url)

def text(news_list,company_name,news_link_list):
    window = tk.Tk()

    pw = tk.PanedWindow()
    pw.pack(fill="both", expand=True)

    window.title("Stock News")
    window.minsize(600,600)

    text = tk.Text(window,height=50,width=150)
    text.config(state = "normal")

    #pw.add(text) what is this used for

    for i in range(len(news_list)): #goes through each news source, for example cnbc and then to wsj
        if i != 0:
            text.insert(tk.INSERT,"\n")
        text.insert(tk.INSERT,company_name[i])
        text.insert(tk.INSERT,"\n")
        link_num = 1 #used to initialize hyperlink label
        for k in range(len(news_list[i])): #news_list consist of different lists of headlines that is within the news_list
            curr_link = "link" + str(link_num)
            curr_link = tk.Label(window,text = news_list[i][k], fg = "blue", cursor = "hand2")
            curr_link.pack()
            curr_link.bind("<Button-1>", lambda event: callback(news_link_list[i][k]))
            #text.insert(tk.INSERT,news_list[i][k])
            #text.insert(tk.INSERT,"\n")

    text.pack()
    window.mainloop()
