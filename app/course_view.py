# Curriculum Designing Program
# Made By Kasra Tookallo
# 11/28/2025
from course_controller import LessonController
from lesson_model import Curriculum
from lesson_model import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

print("Start.")
print("-" * 150)
#-------------------------------------------------------------------------------------------
#                                               Reset command for table
def reset_table():
    lesson_name.set("")
    lesson_code.set(0)
    teacher_name.set("")
    lesson_credits.set(0)
    #status , lesson_list = LessonController.find_all()
   # for items in table.get_children():
    #    table.delete(items)
    #for lesson in lesson_list:
     #   table.insert("", END, values=lesson)
#------------------------------------------------------------------------------------------
#                                               Getting Lesson Data
def select_lesson(event):
    lesson = table.item(table.focus())["values"]
    lesson_name = (lesson[0])
    lesson_code = (lesson[1])
    teacher_name = (lesson[2])
    lesson_credits = (lesson[3])

study_list = []
def receive_data():
    try :
        lesson = Curriculum(
            lesson_name.get() ,
            lesson_code.get() ,
            teacher_name.get(),
            lesson_credits.get()
        )
        lesson.validation()
        study_list.append(lesson)
        lesson.save()
        print("-" * 150)
        #To insert Data into the table
        table.insert(""  , END , values=lesson.to_tuple())
        messagebox.showinfo("Data Saved." , "Lesson saved in the table successfully.")
        print("Your Studies include : ",study_list)
        print("-" * 150)
        reset_table()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:{e}")

def save_click():
    status , message = LessonController.save(
        lesson_name.get() ,
        lesson_code.get() ,
        teacher_name.get() ,
        lesson_credits.get()
    )
    if status :
        reset_table()
        messagebox.showinfo("Data Saved." , message)
    else:
        messagebox.showerror("Error" , message)

def edit_click():
    status, message = LessonController.edit(
        lesson_name.get(),
        lesson_code.get(),
        teacher_name.get(),
        lesson_credits.get()
    )
    if status:
        reset_table()
        messagebox.showinfo("Data Edited.", message)
    else:
        messagebox.showerror("Edition Error", message)


def remove_click():
    status, message = LessonController.remove()
    if status:
        reset_table()
        messagebox.showinfo("Data Removed.", message)
    else:
        messagebox.showerror("Removal Error", message)
def total_credits():
    pass


#------------------------------------------------------------------------------------------------------
#                                             Table Starts Here
Window = Tk()
#Main Heading
Window.title("Curriculum App")
Window.geometry("400x500")
Window.configure(bg="green")

# Entry 1
Label(Window, text="Lesson Name ").place(x=10, y=100)
lesson_name = StringVar()
Entry(Window, textvariable=lesson_name).place(x=100, y=100)

# Entry 2
Label(Window, text="Lesson Code   ").place(x=10, y=150)
lesson_code = IntVar()
Entry(Window, textvariable=lesson_code).place(x=100, y=150)

# Entry 3
Label(Window, text="Teacher Name").place(x=10, y=200)
teacher_name = StringVar()
Entry(Window, textvariable=teacher_name).place(x=100, y=200)

# Entry 4
Label(Window, text="Lesson Credits").place(x=10, y=250)
lesson_credits = IntVar()
Entry(Window, textvariable=lesson_credits).place(x=100, y=250)

Button(Window, text="Save", command=receive_data , width=53).place(x=10, y=300)
Button(Window, text="Edit", command=edit_click, width=53).place(x=10, y=350)
Button(Window, text="Delete", command=remove_click, width=53).place(x=10, y=400)
Button(Window, text="Total Credits", command=total_credits , width=53).place(x=10, y=450)


#Headings
table = ttk.Treeview(Window , columns=(1,2,3,4) , height=10 , show="headings")
#Column 1
table.heading(1, text="Lesson Name")
table.column(1, width=50)

#Column 2
table.heading(2, text="Lesson Code")
table.column(2, width=50)

#Column 3
table.heading(3, text="Teacher Name")
table.column(3, width=50)

#Column4
table.heading(4, text="Lesson Credits")
table.column(4, width=50)

table.place(x=10, y=10 , width=380, height=75)

table.bind("<<TreeviewSelect>>" , select_lesson )

reset_table()
Window.mainloop()
