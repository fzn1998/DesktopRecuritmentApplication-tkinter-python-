from tkinter import *
import sqlite3

LARGE_FONT= ("Verdana", 10)
root = Tk()
root.title('Recruitment')
root.geometry("400x700")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('recruitment.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE students (
		first_name text,
		last_name text,
		course text,
		branch text,
		e_mail text,
		phone_no integer,
		enroll integer,
		class_12 interger,
		graduation interger,
		backlog integer,
		placed text,
		company text,
		package integer
		)""")
'''
def add():
    global add
    #Create Global Variables for text box names
    global enroll
    global placed
    global company
    global package
    global graduation
    global class_12
    global backlog
    global f_name
    global l_name
    global course
    global branch
    global e_mail
    global phone_no
    root.withdraw()
    add = Tk()
    add.title('Add a Record')
    add.geometry("800x400")
	# Create a database or connect to one
    conn = sqlite3.connect('recruitment.db')
	# Create cursor
    c = conn.cursor()
	# Create Text Boxes
    f_name = Entry(add, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(20, 0))
    l_name = Entry(add, width=30)
    l_name.grid(row=0, column=3, pady=(20, 0))
    course = Entry(add, width=30)
    course.grid(row=1, column=1, pady=(10, 0))
    branch = Entry(add, width=30)
    branch.grid(row=1, column=3, pady=(10, 0))
    e_mail = Entry(add, width=30)
    e_mail.grid(row=2, column=1, pady=(10, 0))
    phone_no = Entry(add, width=30)
    phone_no.grid(row=2, column=3, pady=(10, 0))
    enroll = Entry(add, width=30)
    enroll.grid(row=3, column=1, pady=(10, 0))
    class_12 = Entry(add, width=30)
    class_12.grid(row=4, column=1, pady=(10, 0))
    graduation = Entry(add, width=30)
    graduation.grid(row=4, column=3, pady=(10, 0))
    backlog = Entry(add, width=30)
    backlog.grid(row=5, column=1, pady=(10, 0))
    placed = Entry(add, width=30)
    placed.grid(row=6, column=1, pady=(10, 0))
    company= Entry(add, width=30)
    company.grid(row=7, column=1, pady=(10, 0))
    package = Entry(add, width=30)
    package.grid(row=7, column=3, pady=(10, 0))

    # Create Text Box Labels
    f_name_label = Label(add, text="First Name", font=LARGE_FONT)
    f_name_label.grid(row=0, column=0, pady=(20, 0))
    l_name_label = Label(add, text="Last Name", font=LARGE_FONT)
    l_name_label.grid(row=0, column=2, pady=(20, 0))
    course_label = Label(add, text="Course", font=LARGE_FONT)
    course_label.grid(row=1, column=0, pady=(10, 0))
    branch_label = Label(add, text="Branch", font=LARGE_FONT)
    branch_label.grid(row=1, column=2, pady=(10, 0))
    e_mail_label = Label(add, text="E-Mail", font=LARGE_FONT)
    e_mail_label.grid(row=2, column=0, pady=(10, 0))
    phone_no_label = Label(add, text="Phone no", font=LARGE_FONT)
    phone_no_label.grid(row=2, column=2, pady=(10, 0))
    enroll_label = Label(add, text="Enrollment No.", font=LARGE_FONT)
    enroll_label.grid(row=3, column=0, pady=(10, 0))
    class_12_label = Label(add, text="Class 12 marks(in %)", font=LARGE_FONT)
    class_12_label.grid(row=4, column=0, pady=(10, 0))
    graduation_label = Label(add, text="Graduation (in %)", font=LARGE_FONT)
    graduation_label.grid(row=4, column=2, pady=(10, 0))
    backlog_label = Label(add, text="Active Backlogs", font=LARGE_FONT)
    backlog_label.grid(row=5, column=0, pady=(10, 0))
    placed_label = Label(add, text="Placed (Yes/No)", font=LARGE_FONT)
    placed_label.grid(row=6, column=0, pady=(10, 0))
    company_label = Label(add, text="Company", font=LARGE_FONT)
    company_label.grid(row=7, column=0, pady=(10, 0))
    package_label = Label(add, text="Package (in Lakhs)", font=LARGE_FONT)
    package_label.grid(row=7, column=2, pady=(10, 0))

    # Create Submit Button
    submit_btn = Button(add, text="Add Record To Database",height=3,width=5, command=submit, font=LARGE_FONT)
    submit_btn.grid(row=8,column=1, columnspan=1,pady=(40,0),ipadx=110)
    #Commit Changes
    conn.commit()
    # Close Connection
    conn.close()
    root.deiconify()

# Create Update function to update a record
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()

	c.execute("""UPDATE students SET
		first_name = :first,
		last_name = :last,
		course = :course,
		branch = :branch,
		e_mail = :e_mail,
		phone_no = :phone_no,
		enroll = :enroll,
		placed = :placed,
		company = :company,
		package = :package,
		graduation = :graduation,
		class_12 = :class_12,
		backlog = :backlog

		WHERE oid = :oid""",
		{
	    'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'course': course_editor.get(),
	    'branch': branch_editor.get(),
	    'e_mail': e_mail_editor.get(),
	    'phone_no': phone_no_editor.get(),
		'enroll' : enroll_editor.get(),
		'class_12': class_12_editor.get(),
		'graduation' :graduation_editor.get(),
		'placed' : placed_editor.get(),
		'backlog' : backlog_editor.get(),
		'company' : company_editor.get(),
		'package': package_editor.get(),
		'oid': record_id
		})


	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

	editor.destroy()
	root.deiconify()

# Create Edit function to update a record
def edit():
	root.withdraw()
	global editor
	editor = Tk()
	editor.title('Update A Record')
	editor.geometry("800x400")
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()
	record_id = delete_box.get()
	# Query the database
	c.execute("SELECT * FROM students WHERE oid = " + record_id)
	records = c.fetchall()

	#Create Global Variables for text box names
	global enroll_editor
	global placed_editor
	global company_editor
	global package_editor
	global graduation_editor
	global class_12_editor
	global backlog_editor
	global f_name_editor
	global l_name_editor
	global course_editor
	global branch_editor
	global e_mail_editor
	global phone_no_editor

	# Create Text Boxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(20, 0))
	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=0, column=3, pady=(20, 0))
	course_editor = Entry(editor, width=30)
	course_editor.grid(row=1, column=1, pady=(10, 0))
	branch_editor = Entry(editor, width=30)
	branch_editor.grid(row=1, column=3, pady=(10, 0))
	e_mail_editor = Entry(editor, width=30)
	e_mail_editor.grid(row=2, column=1, pady=(10, 0))
	phone_no_editor = Entry(editor, width=30)
	phone_no_editor.grid(row=2, column=3, pady=(10, 0))
	enroll_editor = Entry(editor, width=30)
	enroll_editor.grid(row=3, column=1, pady=(10, 0))
	class_12_editor = Entry(editor, width=30)
	class_12_editor.grid(row=4, column=1, pady=(10, 0))
	graduation_editor = Entry(editor, width=30)
	graduation_editor.grid(row=4, column=3, pady=(10, 0))
	backlog_editor = Entry(editor, width=30)
	backlog_editor.grid(row=5, column=1, pady=(10, 0))
	placed_editor = Entry(editor, width=30)
	placed_editor.grid(row=6, column=1, pady=(10, 0))
	company_editor= Entry(editor, width=30)
	company_editor.grid(row=7, column=1, pady=(10, 0))
	package_editor = Entry(editor, width=30)
	package_editor.grid(row=7, column=3, pady=(10, 0))

    # Create Text Box Labels
	f_name_label = Label(editor, text="First Name", font=LARGE_FONT)
	f_name_label.grid(row=0, column=0, pady=(20, 0))
	l_name_label = Label(editor, text="Last Name", font=LARGE_FONT)
	l_name_label.grid(row=0, column=2, pady=(20, 0))
	course_label = Label(editor, text="Course", font=LARGE_FONT)
	course_label.grid(row=1, column=0, pady=(10, 0))
	branch_label = Label(editor, text="Branch", font=LARGE_FONT)
	branch_label.grid(row=1, column=2, pady=(10, 0))
	e_mail_label = Label(editor, text="E-Mail", font=LARGE_FONT)
	e_mail_label.grid(row=2, column=0, pady=(10, 0))
	phone_no_label = Label(editor, text="Phone no", font=LARGE_FONT)
	phone_no_label.grid(row=2, column=2, pady=(10, 0))
	enroll_label = Label(editor, text="Enrollment No.", font=LARGE_FONT)
	enroll_label.grid(row=3, column=0, pady=(10, 0))
	class_12_label = Label(editor, text="Class 12 marks(in %)", font=LARGE_FONT)
	class_12_label.grid(row=4, column=0, pady=(10, 0))
	graduation_label = Label(editor, text="Graduation (in %)", font=LARGE_FONT)
	graduation_label.grid(row=4, column=2, pady=(10, 0))
	backlog_label = Label(editor, text="Active Backlogs", font=LARGE_FONT)
	backlog_label.grid(row=5, column=0, pady=(10, 0))
	placed_label = Label(editor, text="Placed (Yes/No)", font=LARGE_FONT)
	placed_label.grid(row=6, column=0, pady=(10, 0))
	company_label = Label(editor, text="Company", font=LARGE_FONT)
	company_label.grid(row=7, column=0, pady=(10, 0))
	package_label = Label(editor, text="Package (in Lakhs)", font=LARGE_FONT)
	package_label.grid(row=7, column=2, pady=(10, 0))
	# Loop thru results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		course_editor.insert(0, record[2])
		branch_editor.insert(0, record[3])
		e_mail_editor.insert(0, record[4])
		phone_no_editor.insert(0, record[5])
		enroll_editor.insert(0, record[6])
		class_12_editor.insert(0, record[7])
		graduation_editor.insert(0, record[8])
		backlog_editor.insert(0, record[9])
		placed_editor.insert(0, record[10])
		company_editor.insert(0, record[11])
		package_editor.insert(0, record[12])

	# Create a Save Button To Save edited record
	edit_btn = Button(editor, text="Save Record",height=3,width=5, command=update, font=LARGE_FONT)
	edit_btn.grid(row=8,column=1, columnspan=1,pady=(40,0),ipadx=110)

def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()

	# Delete a record
	c.execute("DELETE from students WHERE oid = " + delete_box.get())

	delete_box.delete(0, END)

	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()



# Create Submit Function For database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO students VALUES (:f_name, :l_name, :course, :branch, :e_mail, :phone_no, :enroll, :placed, :company, :package ,:graduation,:class_12, :backlog)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'course': course.get(),
				'branch': branch.get(),
				'e_mail': e_mail.get(),
				'phone_no': phone_no.get(),
				'enroll' : enroll.get(),
				'placed' : placed.get(),
				'company' : company.get(),
				'package':package.get(),
				'graduation' :graduation.get(),
				'class_12':class_12.get(),
				'backlog' :backlog.get()

			})


	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

	# Clear The Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	course.delete(0, END)
	branch.delete(0, END)
	e_mail.delete(0, END)
	phone_no.delete(0, END)
	enroll.delete(0, END)
	placed.delete(0, END)
	company.delete(0, END)
	package.delete(0, END)
	graduation.delete(0, END)
	class_12.delete(0, END)
	backlog.delete(0, END)



# Create Query Function
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()
	# Query the database
	c.execute("SELECT *, oid FROM students")
	records = c.fetchall()
	# print(records)
	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += " "+str(record[13]) + "\t" + str(record[0]) + " " +str(record[1])+ "\t" +str(record[10]) + "\n"

	heading= "oid"+"\t"+" Full Name"+"\t"+"Placed"+"\n"
	query_heading=	Label(root, text=heading)
	query_heading.grid(row=12,column=0,columnspan=2)

	query_label = Label(root, text=print_records)
	query_label.grid(row=13, column=0, columnspan=3)

	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()
def std_placed():
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM students")
	records = c.fetchall()
	# print(records)

	# Loop Thru Results
	print_records = ''
	for record in records:
		if str(record[10])=="Yes":
			print_records += " "+str(record[13]) + "\t" + str(record[0]) + " " +str(record[1])+ "\t" +str(record[11]) +"\t" +str(record[12])+ "\n"

	heading= "oid"+"\t"+" Full Name"+"\t"+"Company"+"\t"+"Package"+"\n"
	query_heading=	Label(root, text=heading)
	query_heading.grid(row=14,column=0,columnspan=4)

	query_label = Label(root, text=print_records)
	query_label.grid(row=15, column=0, columnspan=4)
	#Commit Changes
	conn.commit()
	# Close Connection
	conn.close()

def std_nplaced():
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()
	# Query the database
	c.execute("SELECT *, oid FROM students")
	records = c.fetchall()
	# print(records)
	# Loop Thru Results
	print_records = ''
	for record in records:
		if str(record[10])=="No":
			print_records += " "+str(record[13]) + "\t" + str(record[0]) + " " +str(record[1])+ "\t" +str(record[9]) + "\n"

	heading= "oid"+"\t"+" Full Name"+"\t"+"Active Backlog"+"\n"
	query_heading=	Label(root, text=heading)
	query_heading.grid(row=16,column=0,columnspan=2)

	query_label = Label(root, text=print_records)
	query_label.grid(row=17, column=0, columnspan=3)
	#Commit Changes
	conn.commit()
	# Close Connection
	conn.close()

def close():
	conn.close()
	srch.destroy()
	root.deiconify()


def search():
	root.withdraw()
	global srch
	srch = Tk()
	srch.title('Search Result')
	srch.geometry("400x400")
	# Create a database or connect to one
	conn = sqlite3.connect('recruitment.db')
	# Create cursor
	c = conn.cursor()
	record_id = delete_box.get()
	# Query the database
	c.execute("SELECT * FROM students WHERE oid = " + record_id)
	records = c.fetchall()
	for record in records:
		f_name_label = Label(srch, text="First Name : "+str(record[0]), font=LARGE_FONT)
		f_name_label.grid(row=0, column=0, pady=(20, 0))
		l_name_label = Label(srch, text="Last Name : "+str(record[1]), font=LARGE_FONT)
		l_name_label.grid(row=0, column=2, pady=(20, 0))
		course_label = Label(srch, text="Course : "+str(record[2]), font=LARGE_FONT)
		course_label.grid(row=1, column=0, pady=(10, 0))
		branch_label = Label(srch, text="Branch : "+str(record[3]), font=LARGE_FONT)
		branch_label.grid(row=1, column=2, pady=(10, 0))
		e_mail_label = Label(srch, text="E-Mail : "+str(record[4]), font=LARGE_FONT)
		e_mail_label.grid(row=2, column=0, pady=(10, 0))
		phone_no_label = Label(srch, text="Phone no : "+str(record[5]), font=LARGE_FONT)
		phone_no_label.grid(row=2, column=2, pady=(10, 0))
		enroll_label = Label(srch, text="Enrollment No. : "+str(record[6]), font=LARGE_FONT)
		enroll_label.grid(row=3, column=0, pady=(10, 0))
		class_12_label = Label(srch, text="Class 12 marks(in %) : "+str(record[7]), font=LARGE_FONT)
		class_12_label.grid(row=4, column=0, pady=(10, 0))
		graduation_label = Label(srch, text="Graduation (in %) : "+str(record[8]), font=LARGE_FONT)
		graduation_label.grid(row=4, column=2, pady=(10, 0))
		backlog_label = Label(srch, text="Active Backlogs : "+str(record[9]), font=LARGE_FONT)
		backlog_label.grid(row=5, column=0, pady=(10, 0))
		placed_label = Label(srch, text="Placed (Yes/No) : "+str(record[10]), font=LARGE_FONT)
		placed_label.grid(row=6, column=0, pady=(10, 0))
		company_label = Label(srch, text="Company : "+str(record[11]), font=LARGE_FONT)
		company_label.grid(row=7, column=0, pady=(10, 0))
		package_label = Label(srch, text="Package (in Lakhs) : "+str(record[12]), font=LARGE_FONT)
		package_label.grid(row=7, column=2, pady=(10, 0))

	close_btn = Button(srch, text="Close Record",height=3,width=5, command=close, font=LARGE_FONT)
	close_btn.grid(row=8,column=0, columnspan=1,pady=(20,0),ipadx=80)

delete_box = Entry(root, width=30)
delete_box.grid(row=5, column=1, pady=5)

delete_box_label = Label(root, text="Select ID", font=LARGE_FONT )
delete_box_label.grid(row=5, column=0, pady=5)

# Create Submit Button
add_btn = Button(root, text="Add Record To Database",height=2, command=add, font=LARGE_FONT)
add_btn.grid(row=1, column=0, columnspan=2, pady=20, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show all records",height=2, command=query, font=LARGE_FONT)
query_btn.grid(row=2, column=0, columnspan=2, pady=0, padx=10, ipadx=127)

std_placed_btn = Button(root, text="Show all the students Placed",height=2, command=std_placed, font=LARGE_FONT)
std_placed_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=83)

std_nplaced_btn= Button(root, text="Show all the students not Placed",height=2, command=std_nplaced, font=LARGE_FONT)
std_nplaced_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=75)
#Create A Search Button
search_btn = Button(root, text="Search Record",height=2, command=search, font=LARGE_FONT)
search_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=128)
#Create A Delete Button
delete_btn = Button(root, text="Delete Record",height=2, command=delete, font=LARGE_FONT)
delete_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit, font=LARGE_FONT)
edit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=132)


#Commit Changes
conn.commit()

# Close Connection
conn.close()
root.mainloop()
