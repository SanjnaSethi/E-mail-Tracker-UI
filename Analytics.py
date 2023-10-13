from tkinter import*
import tkinter as tk

#Root window
window = tk.Tk()
window.resizable(False,False)

#Window Title 
window.title("E-mail Tracker Desktop App")

#Window size
window.geometry("900x600")

#Create a label & place for the company's email ID
company_tracker_label = tk.Label(text = "company@email.com")
company_tracker_label.place(x=880,y=10,anchor="ne")

#Create a label & place for the "Analytics" text
email_tracker_label = tk.Label(text = "Analytics", font=("Arial", 30, "bold"))
email_tracker_label.place(x=450,y=50,anchor="center")

#Create a get raw data button
get_raw_data_button = tk.Button(window, text ="Get Raw Data")
get_raw_data_button.place(x=450, y=550,anchor="center")

#Starting the mainloop
window.mainloop()