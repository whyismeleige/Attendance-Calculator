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