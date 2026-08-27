'''
from tkinter import *
from tkinter import messagebox
import mysql.connector as m

root=Tk()
con=m.connect(host="localhost",user="root",password="Mysql@2026",database="ravana")
cur=con.cursor()

root.state("zoomed")
root.title("Admission Form")
l=Label(root,text="WELCOME TO PSG ITECH",font=("Times",25,'bold'))
l.pack()
l1=Label(root,text="NAME:",font=("",25,'bold'))
l1.place(x=100,y=150)
e1=Entry(root,font=("",22,'bold'))
e1.place(x=250,y=150)

l2=Label(root,text="AGE:",font=("",25,'bold'))
l2.place(x=100,y=250)
e2=Entry(root,font=("",22,'bold'))
e2.place(x=250,y=250)
l3=Label(root,text="COURSE:",font=("",23,'bold'))
l3.place(x=95,y=350)
e3=Entry(root,font=("",22,'bold'))
e3.place(x=250,y=350)
var=StringVar()
r1=Radiobutton(root,text='M',variable=var,value="Male")
r1.place(x=95,y=450)
r2=Radiobutton(root,text='F',variable=var,value="Female")
r2.place(x=300,y=450)


def Save():
    name = e1.get()
    age = e2.get()
    course = e3.get()
    gen = var.get()
        
    if name == "":
        messagebox.showerror("Error", "Enter Name")
        return

    if age == "":
        messagebox.showerror("Error", "Enter Age")
        return

    if course == "":
        messagebox.showerror("Error", "Enter Course")
        return

    if gen == "":
        messagebox.showerror("Error", "Select Gender")
        return

    age = int(age)

    cur.execute(
        "INSERT INTO Stud (Sname, Age, Course, Gender) VALUES (%s, %s, %s, %s)",
        (name, age, course, gen)
    )

    con.commit()

    messagebox.showinfo("Success", "Record Saved Successfully")


def Update():
    name = e1.get()
    age = e2.get()
    course = e3.get()
    gen = var.get()

    if name == "":
        messagebox.showerror("Error", "Enter Student Name")
        return

    # Update Age only
    if age != "":
        cur.execute(
            "UPDATE Stud SET Age=%s WHERE Sname=%s",
            (age, name)
        )

    # Update Course only
    if course != "":
        cur.execute(
            "UPDATE Stud SET Course=%s WHERE Sname=%s",
            (course, name)
        )

    # Update Gender only
    if gen != "":
        cur.execute(
            "UPDATE Stud SET Gender=%s WHERE Sname=%s",
            (gen, name)
        )

    con.commit()

    messagebox.showinfo("Success", "Record Updated Successfully")

       

def Delete():
    name=e1.get()

    if(name==""):
        messagebox.showerror("Error","Please Enter name")
        return 

    cur.execute("DELETE FROM stud WHERE Sname=%s",(name,))
    con.commit()
    messagebox.showinfo("Sucess","Deleted Successfully")


def View():

    cur.execute("SELECT * FROM Stud")

    data = cur.fetchall()

    if len(data) == 0:
        messagebox.showinfo(
            "View",
            "No records found"
        )
        return

    result = ""

    for i in data:
        result += str(i) + "\n"

    messagebox.showinfo(
        "Student Records",
        result
    )
        


b1=Button(root,text="SAVE",font=("",15,'bold'),command=Save)
b1.place(x=900,y=600)
result=Label(root,text="",font=("Arial",20,'bold'),fg='blue')
result.pack()

b2=Button(root,text="UPDATE",font=("",15,'bold'),command=Update)
b2.place(x=1150,y=600)

b3=Button(root,text="DELETE",font=("",15,'bold'),command=Delete)
b3.place(x=900,y=800)

b4=Button(root,text="VIEW",font=('',15,'bold'),command=View)
b4.place(x=1150,y=800)


root.mainloop()




n=int(input("Enter a no:"))
c=0
for i in range(1,n):
    if(n%i==0):
       c+=1

if(c>1):
    print(n,"is a composite no")

else:
    print(n,"is a prime no")    '''

'''
l=eval(input("enter a list:"))
big=l[0]

for i in range(len(l)):
    if(l[i]>big):
        big=l[i]

print("the largest no:",big)

'removing dupiicate elements'

L=eval(input("enter a list:"))
lst=[]
for i in range(len(L)-1,-1,-1):
      lst+=[L[i]]

print(lst)
'''
S=37000

for i in range(19):
    S+=(S+500)
    print(S)

