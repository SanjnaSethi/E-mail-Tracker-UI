from tkinter import*
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
data=requests.get("https://email-tracking-five.vercel.app/get").json()
x=data['data']
x=x.replace("null","None")
x=eval(x)

def generate_email_data(size = 50):
    
    data = np.random.choice([0,1], size=size)
    return data

def generate_email_open_times(size = 50):
    
    peak_time = np.random.randint(8 * 60, 18 * 60)
    times = np.random.normal(loc=peak_time, scale=60, size=size).astype(int)
    times = np.clip(times, 0, 24*60-1)
    times.sort()
    return times

def generate_pie_data(size = 50):
    
    data = np.random.choice([0,1], size=size)
    return data

def plot_email_data(ax):
    newData={"opened":0,"NotOpened":0}
    for i in x:
	    if int(i['fields']['status'])>0:
	        newData['opened']+=1
	    else:
		    newData['NotOpened']+=1
                    
    EmailOpened = list(newData.keys())
    EmailNotOpened = list(newData.values())
 
    # creating the bar plot
    ax.bar(EmailOpened, EmailNotOpened, color ='maroon',width = 0.5)
    
    ax.set_xlabel("Current Scenario")
    ax.set_ylabel("Count")
    ax.set_title("Bar Graph of Open and Not Open Count")


def plot_email_pie(ax):
    email_pie_data = generate_pie_data()
    opened_count = np.sum(email_pie_data)
    not_opened_count = len(email_pie_data) - opened_count
    newData={"opened":0,"NotOpened":0}
    for i in x:
	    if int(i['fields']['status'])>0:
	        newData['opened']+=1
	    else:
		    newData['NotOpened']+=1
                    
    y = np.array([newData['opened'],newData['NotOpened']])
    mylabels = ["Opened", "Not Opened"]

    ax.pie(y, labels = mylabels)
    # labels = ['Opened','Not Opened']
    # colors = ['skyblue', 'lightcoral']
    # explode = (0.1,0) 
    # ax.pie([opened_count, not_opened_count], labels=labels, autopct="%1.1f%%", startangle=90, colors=colors, explode=explode)
    ax.set_title('Pie Chart')

def plot_email_timeline(ax):
    email_timeline_data = generate_email_open_times()
    time_labels = [f"{hour % 12 or 12}:{minute:02d} {'AM' if hour < 12 else 'PM'}" for hour, minute in zip(email_timeline_data // 60, email_timeline_data % 60)]
    ax.hist(email_timeline_data, bins=range(0, 24*60+1, 120), color=['skyblue'], edgecolor='black')
    ax.set_xticks(np.arange(0, 24*60+1, 120))  
    ax.set_xticklabels(time_labels[::4], rotation=45, ha='right') 
    ax.set_xlabel("Time of Day")
    ax.set_ylabel("Frequency")
    ax.set_title("Timeline")
    ax.grid(True, linestyle='--', alpha=0.6, which='both', axis='y', color='black')

#Root window
window = tk.Tk()
window.resizable(False,False)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 6))

# Plot data on each subplot
plot_email_data(ax1)
plot_email_timeline(ax2)
plot_email_pie(ax3)

# Add titles
ax1.set_title("Bar Graph")
ax2.set_title("Timeline")
ax3.set_title("Pie Chart")

# Add canvas to Tkinter window
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

#Window Title 
window.title("E-mail Tracker Desktop App")

#Window size
window.geometry("1150x900")

#Create a label & place for the company's email ID
company_tracker_label = tk.Label(text = "company@email.com")
company_tracker_label.place(x=1100,y=10,anchor="ne")

#Create a label & place for the "Analytics" text
email_tracker_label = tk.Label(text = "Analytics", font=("Arial", 30, "bold"))
email_tracker_label.place(x=575,y=35,anchor="center")

canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=60)

#Create a get raw data button
get_raw_data_button = tk.Button(window, text ="Get Raw Data")
get_raw_data_button.place(x=575, y=800,anchor="center")

#Starting the mainloop
window.mainloop()