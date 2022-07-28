# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:33:04 2022

@author: PC_RC
"""

from tkinter import * 
import random

root=Tk()

root.title("Random Word Generator")
root.geometry("500x500")
root.configure(background="gold")


random_text = Label(root)



def random_word():
    alpha_list = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    random_no1 = random.randint(0,25)
    random_no2 = random.randint(0, 25)
    random_no3 = random.randint(0, 25)
    random_no4 = random.randint(0, 25)
    random_no5 = random.randint(0, 25)

    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    
    random_text["text"] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    
    
btn1 = Button(root)
btn1 = Button(root, text=" Generate Random Word ", fg="blue", command = random_word)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
random_text.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()