#this is the basic structure of attendance calculator

#input the classes done on each day in the week
monday = int(input("Enter The Classes of Monday:"))
tuesday = int(input("Enter The Classes of Tuesday"))
wednesday = int(input("Enter The Classes of Wednesday:"))
thursday = int(input("Enter The Classes of Thursday:"))
friday = int(input("Enter The Classes of Friday:"))
saturday = int(input("Enter The Classes of Saturday:"))

#since some students have holidays on saturdays this conditional is used
if saturday == 0:
    total = monday + tuesday + wednesday + thursday + friday
    avg = total/5
    print("Total No of Classes per week = ",total)
else:
    total = monday + tuesday + wednesday + thursday + friday + saturday
    avg = total/6
    print("Total No of Classes per week = ",total)

#a rough estimate of total no of weeks done (excluding holidays)
weeks_done = int(input("How many weeks have been finished till now?"))
today_total_classes = weeks_done * total

#inputting set of values required
current_attendance = int(input("What is your current attendance?"))
current_classes_attended = (current_attendance/100) * today_total_classes
weeks_left = int(input("More how many weeks are left?"))
cutoff_required = int(input("What Percentage is required to write the exam?"))

classes_left = weeks_left * total
total_classes = today_total_classes + classes_left
classes_cutoff = (cutoff_required/100) * total_classes
added_classes = current_classes_attended + classes_left

#finding if you need holidays or you need to go to all classes
if(added_classes > classes_cutoff):
    diff = (added_classes - classes_cutoff)
    holidays = diff/avg
    print("No of Holidays you can take: ",holidays)
else:
    print("Go to all Classes")


