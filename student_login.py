# Import all the required modules
from tkinter import Tk, Label, Entry, Button
from new_student import new_student


# Create a function to create the login window
def student_login():
    # Create the login window
    window = Tk()
    # Set the title of the login window
    window.title("Login")
    # Set the size of the login window
    window.geometry("600x400")
    
    # Create a label for username
    username_label = Label(window, text="Username:")
    username_label.place(x=50, y=100)
    # Create an entry for username
    username_entry = Entry(window, width=20)
    username_entry.place(x=200, y=100)
    
    # Create a label for password
    password_label = Label(window, text="Password:")
    password_label.place(x=50, y=150)
    # Create an entry for password
    password_entry = Entry(window, width=20)
    password_entry.place(x=200, y=150)
    
    # Create a button for login
    login_btn = Button(window, text="Login")
    login_btn.place(x=200, y=200, width=200)
    
    # Create a button for new user
    new_user_btn = Button(window, text="New User", command=new_student)
    new_user_btn.place(x=200, y=250, width=200)
    
    # Run the login window
    window.mainloop()
