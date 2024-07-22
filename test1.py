import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

def weeks_between(start_date,end_date):
    delta = end_date - start_date
    return delta.days//7

def calculate_attendance():
    monday = int(monday_var.get())
    tuesday = int(tuesday_var.get())
    wednesday = int(wednesday_var.get())
    thursday = int(thursday_var.get())
    friday = int(friday_var.get())
    saturday = int(saturday_var.get())

    if saturday == 0:
        total = monday + tuesday + wednesday + thursday + friday
        avg = total/5
    else:
        total = monday + tuesday + wednesday + thursday + friday + saturday
        avg = total/6
    
    joining_date = datetime.strptime(joining_date_var.get(),"%Y-%m-%d")
    end_date = datetime.strptime(end_date_var.get(),"%Y-%m-%d")
    current_date = datetime.now()

    weeks_done = weeks_between(joining_date,current_date)
    weeks_left = weeks_between(current_date,end_date)
    today_total_classes = weeks_done * total

    current_attendance = int(current_attendance_var.get())
    current_classes_attended = (current_attendance/100) * today_total_classes
    cutoff_required = int(cutoff_required_var.get())

    classes_left = weeks_left * total
    total_classes = today_total_classes + classes_left
    classes_cutoff = (cutoff_required/100) * total_classes
    added_classes = current_classes_attended + classes_left
    max_attendance = added_classes/total_classes * 100


    if added_classes > classes_cutoff:
        diff = added_classes - classes_cutoff
        holidays = diff/avg 
        holidays = round(holidays)
        result_label.config(text = f"No of Holidays you can take {holidays} \n Maximum Percentage Possible {max_attendance}")
    else:
        result_label.config(text = f"Go to All Classes \n Maximum Percentage Possible {max_attendance}")
    
root = tk.Tk()
root.title("Attendance Calculator")

tk.Label(root,text = "Enter the Classes of Monday:").grid(row=0,column=0)
monday_var = tk.StringVar()
tk.Entry(root,textvariable=monday_var).grid(row=0,column=1)

tk.Label(root,text = "Enter the Classes of Tuesday:").grid(row=1,column=0)
tuesday_var = tk.StringVar()
tk.Entry(root,textvariable=tuesday_var).grid(row=1,column=1)

tk.Label(root,text= "Enter the Classes of Wednesday:").grid(row=2,column=0)
wednesday_var = tk.StringVar()
tk.Entry(root,textvariable=wednesday_var).grid(row=2,column=1)

tk.Label(root,text = "Enter the Classes of Thursday:").grid(row=3,column=0)
thursday_var = tk.StringVar()
tk.Entry(root,textvariable=thursday_var).grid(row=3,column=1)

tk.Label(root,text="Enter the Classes of Friday:").grid(row=4,column=0)
friday_var = tk.StringVar()
tk.Entry(root,textvariable=friday_var).grid(row=4,column=1)

tk.Label(root, text="Enter the Classes of Saturday (Enter 0 if Holiday): ").grid(row=5,column=0)
saturday_var = tk.StringVar()
tk.Entry(root,textvariable=saturday_var).grid(row=5,column=1)

tk.Label(root,text="Enter your Joining Date (YYYY-MM-DD):").grid(row=6,column=0)
joining_date_var = tk.StringVar()
tk.Entry(root,textvariable= joining_date_var).grid(row=6,column=1)

tk.Label(root,text="Enter your end date of semester (YYYY-MM-DD):").grid(row=7,column=0)
end_date_var = tk.StringVar()
tk.Entry(root,textvariable= end_date_var).grid(row=7,column=1)

tk.Label(root,text = "What is your current attendance (in %)?").grid(row=8,column=0)
current_attendance_var = tk.StringVar()
tk.Entry(root,textvariable=current_attendance_var).grid(row=8,column=1)

tk.Label(root,text="What percentage is required to write the exam?").grid(row=9,column=0)
cutoff_required_var = tk.StringVar()
tk.Entry(root,textvariable=cutoff_required_var).grid(row=9,column=1)

calculate_button = tk.Button(root,text="Calculate",command=calculate_attendance)
calculate_button.grid(row=10,columnspan = 2)

result_label = tk.Label(root,text="")
result_label.grid(row=11,columnspan=2)

root.mainloop()