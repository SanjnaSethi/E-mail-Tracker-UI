from tkinter import*
import tkinter as tk
import requests 
from tkinter import messagebox

def send_email():
    params={
    "recipient_list":[""],
    "subject":"hello"
    }
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

#Create a label & place for the "Send E-mail" text
email_tracker_label = tk.Label(text = "Send E-mail", font=("Arial", 30, "bold"))
email_tracker_label.place(x=450,y=50,anchor="center")

#Create a label for the text area title
recipient_email_list_label = tk.Label(text="Recipient E-mail List", font=("Arial", 10, "bold"))
recipient_email_list_label.place(x=20, y=110)

#Create a text area for the user to write in
text_area = tk.Entry(window, width=106, height=2)
text_area.place(x=20, y=140)

#Create a label for the subject area title
subject_of_email_label = tk.Label(text="Subject of E-mail", font=("Arial", 10, "bold"))
subject_of_email_label.place(x=20, y=210)

#Create a subject area for the user to write in
subject_area = tk.Entry(window, width=106, height=2)
subject_area.place(x=20, y=240)

#Create a label for the body area title
body_of_email_label = tk.Label(text="Body of E-mail", font=("Arial", 10, "bold"))
body_of_email_label.place(x=20, y=310)

#Create a body area for the user to write in
body_area = tk.Entry(window, width=106, height=7)
body_area.place(x=20, y=340)

#Create a Send button
send_email_button = tk.Button(window, text ="Send E-mail", command=lambda:send_email)
send_email_button.place(x=450, y=550,anchor="center")

#Starting the mainloop
window.mainloop()