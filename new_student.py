# Import all the required modules
from tkinter import Tk, Label, Entry, Button


# Create a function to create the new user window
def new_student():
    # Create the login window
    window = Tk()
    # Set the title of the login window
    window.title("New Student")
    # Set the size of the login window
    window.geometry("600x400")
    
    # Create a label for name
    name_label = Label(window, text="Name:")
    name_label.place(x=50, y=50)
    # Create an entry for name
    name_entry = Entry(window, width=20)
    name_entry.place(x=200, y=50)
    
    # Create a label for registration number
    reg_no_label = Label(window, text="Registration Number:")
    reg_no_label.place(x=50, y=100)
    # Create an entry for registration number
    reg_no_entry = Entry(window, width=20)
    reg_no_entry.place(x=200, y=100)
    
    # Create a label for specialization
    specialization_label = Label(window, text="Specialization:")
    specialization_label.place(x=50, y=150)
    # Create an entry for specialization
    specialization_entry = Entry(window, width=20)
    specialization_entry.place(x=200, y=150)
    
    # Create a label for mobile number
    mobile_no_label = Label(window, text="Mobile Number:")
    mobile_no_label.place(x=50, y=200)
    # Create a entry for mobile number
    mobile_no_entry = Entry(window, width=20)
    mobile_no_entry.place(x=200, y=200)
    
    # Create a label for email
    email_label = Label(window, text="Email:")
    email_label.place(x=50, y=250)
    # Create an entry for email
    email_entry = Entry(window, width=20)
    email_entry.place(x=200, y=250)
    
    # Create a button to register
    register_btn = Button(window, text="Register")
    register_btn.place(x=200, y=300, width=200)
    
    # Run the login window
    window.mainloop()
