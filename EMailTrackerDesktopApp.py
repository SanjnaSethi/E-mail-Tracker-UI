from tkinter import*
import tkinter as tk

#Fuction to open the Send Email window
def open_send_email_window():
    window.destroy()
    import SendEmail

#Function to open the Analysis window
def open_analysis_window():
    window.destroy()
    import Analytics

#Root Window
window = tk.Tk()
window.resizable(False,False)

#Window Title 
window.title("E-mail Tracker Desktop App")

#Window size
window.geometry("1150x900")

#Create a label & place for the company's email ID
company_tracker_label = tk.Label(text = "company@email.com")
company_tracker_label.place(x=1100,y=10,anchor="ne")

#Create a label & place for the "E-mail Tracker" text
email_tracker_label = tk.Label(text = "E-mail Tracker", font=("Arial", 40, "bold"))
email_tracker_label.place(x=575,y=50,anchor="center")

#Load the email logo image
email_logo = tk.PhotoImage(file="email_logo.png")

#Create a label for the email logo image
email_logo_label = tk.Label(image=email_logo)

#Place the email logo label below the "E-mail Tracker" text
email_logo_label.place(x=575, y=100, anchor="center")

#Create Send Email & Analysis buttons
send_email_button = tk.Button(window, text ="Send Email", command=open_send_email_window)
send_email_button.place(x=300, y=600)

analysis_button = tk.Button(window, text ="Analysis", command=open_analysis_window)
analysis_button.place(x=800, y=600)

#Starting the mainloop
window.mainloop()
