import tkinter as tk



# This code represents enhancement two which falls under tha category of algorithms and data structures. I chose to increase the overall
# complexity of the original code base and to incorporate a graphical user interface using tkinter to display my skills in algorithms
# and data structures. 

root = tk.Tk()
root.title("Contact Manager")
root.configure(bg='snow3') # set bg color to gray


# Lines 10 through 44 are used to create and position each label and text input box
# I chose very mild background and foreground colors to keep the GUI simple
# The labels and text input boxes are all positioned using columns and rows
label_id = tk.Label(root, text="ID:", bg='snow3')
label_id.grid(row=0, column=0, padx=5, pady=5)

entry_id = tk.Entry(root, bg='white', border=3)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_first_name = tk.Label(root, text="First Name:", bg='snow3')
label_first_name.grid(row=1, column=0, padx=5, pady=5)

entry_first_name = tk.Entry(root, bg='white', border=3)
entry_first_name.grid(row=1, column=1, padx=5, pady=5)

label_last_name = tk.Label(root, text="Last Name:", bg='snow3')
label_last_name.grid(row=2, column=0, padx=5, pady=5)

entry_last_name = tk.Entry(root, bg='white', border=3)
entry_last_name.grid(row=2, column=1, padx=5, pady=5)

label_number = tk.Label(root, text="Number:", bg='snow3')
label_number.grid(row=3, column=0, padx=5, pady=5)

entry_number = tk.Entry(root, bg='white', border=3)
entry_number.grid(row=3, column=1, padx=5, pady=5)

label_address = tk.Label(root, text="Address:", bg='snow3')
label_address.grid(row=4, column=0, padx=5, pady=5)

entry_address = tk.Entry(root, width=30, bg='white', border=3)
entry_address.grid(row=4, column=1, padx=5, pady=5)

label_results = tk.Label(root, text="Results:", bg='snow3')
label_results.grid(row=5, column=0, padx=5, pady=5)

results_text = tk.Text(root, bg='white', height=5, width=30, border=3)
results_text.grid(row=5, column=1, padx=5, pady=5)

#TO-DO: MILESTONE 3: Add in connection string to connect to MongoDB and contact database

# This method validates input and will tell the user if their inputs are incorrect allowing them to fix it and try again
def input_validation():
    id = entry_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    number = entry_number.get()
    address = entry_address.get()

    # Checks for proper input and returns False if incorrect or True if all input validation passes
    # anytime input validation fails users will be notified in the results text box
    
    # returns false if ID is empty
    if not id:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID field can't be empty.")
        return False
    # returns false if ID is greater than 10 characters
    elif len(id) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID must be 10 characters or less.")
        return False
    
    # returns false if first_name is empty
    elif not first_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name can't be empty.")
        return False
    # returns false if first_name greater than 10 characters
    elif len(first_name) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name must be 10 characters or less.")
        return False
    
    # returns false if last_name is empty
    elif not last_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name field can't be empty.")
        return False
    # returns false if last_name is greater than 15 characters
    elif len(last_name) > 15:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name must be 15 characters or less.")
        return False
    
    # returns false if number is empty
    elif not number:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number field can't be empty.")
        return False
    # returns false if number is not exactly 10 characters
    elif len(number) != 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number must be exactly 10 characters.")
        return False
    
    # returns false if address is empty
    elif not address:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address field can't be empty.")
        return False
    # returns false if address is greater than 30 characters
    elif len(address) > 30:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address must be 30 characters or less.")
        return False
    else:
        return True

# The following 5 methods are idividual input validation checks for each field, these were created to be used with the edit_input method
# These individual validation functions will be utilized in the edit_input function
def id_validation():
    id = entry_id.get()
    
    # validates id input and sends any errors to the results box
    if not id:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID field can't be empty.")
        return False
    elif len(id) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID must be 10 characters or less.")
        return False
    else:
        return True

def first_name_validation():
    first_name = entry_first_name.get()

    # validates first_name input and sends any errors to the results box
    if not first_name: 
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name field can't be empty.")
        return False
    elif len(first_name) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name must be 10 characters or less.")
        return False
    else:
        return True

def last_name_validation():
    last_name = entry_last_name.get()

    # validates last_name input and sends any errors to the results box
    if not last_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name field can't be empty.")
        return False
    elif len(last_name) > 15:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name must be 15 characters or less.")
        return False
    else:
        return True

def number_validation():
    number = entry_number.get()

    # validates number input and sends any errors to the results box
    if not number:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number field can't be empty.")
        return False
    elif len(number) != 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number must be exactly 10 character.")
        return False
    else:
        return True

def address_validation():
    address = entry_address.get()

    # validates address input and sends any errors to the results box
    if not address:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address field can't be empty.")
        return False
    elif len(address) > 30:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address must be 30 characters or less.")
        return False
    else:
        return True
        

# Verifies valid input first then Grabs information from each field and stores it as a dictionary named contact
# I will be adding in the proper database functionality on the next Milestone
def save_input():
    if input_validation(): # Checks input
        contact = {
            "_id": entry_id.get(),
            "FirstName": entry_first_name.get(),
            "LastName": entry_last_name.get(),
            "Number": entry_number.get(),
            "Address": entry_address.get()
        }
        # TO-DO: MILESTONE 3: Add in command to save contact to MongoDB
        # I designed this portion to delete each field after successful save to prepare for the next contact
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Contact saved to the database.") # Notifies user of successful save
        entry_id.delete(0,tk.END)
        entry_first_name.delete(0,tk.END)
        entry_last_name.delete(0,tk.END)
        entry_number.delete(0,tk.END)
        entry_address.delete(0,tk.END)

# empty method for now, I will be later adding the ability to search MongoDB for a contact using the ID field
def search_input():
    if id_validation():
        # TO-DO: MILESTONE 3: Add in command to search database for contact matching search_id
        pass
        
# empty method, will later add abiliity to locate and delete contact from DB
def delete_input():
    if id_validation():
        # TO-DO: MILESTONE 3: Add in command to delete contact from MongoDB
        # TO-DO: MILESTONE 3: IF/else loop to to display if contact was deleted or not
        pass

# this method currently grabs the data from each field and validates those inputs, I will later add the ability to edit each field on the database
def edit_input():
    if id_validation(): # first checks for valid id input
        edit_id = entry_id.get()
        new_first_name = entry_first_name.get()
        new_last_name = entry_last_name.get()
        new_number = entry_number.get()
        new_address = entry_address.get()

        # TO-DO: MILESTONE 3: Add in pymongo command to search for contact to be used in editing

        update_data = {}
        if new_first_name:
            # if validation passes update firstname
            if first_name_validation(): # verifies first_name input
                update_data["FirstName"] = new_first_name
            else:
                entry_first_name.delete(0,tk.END)
                entry_first_name.insert(tk.END, "Must be 10 characters or less.") # indicate to users that validation failed
        if new_last_name:
            # if validation passes update lastname
            if last_name_validation(): # verifies last_name input
                update_data["LastName"] = new_last_name
            else:
                entry_last_name.delete(0,tk.END)
                entry_last_name.insert(tk.END, "Must be 15 Characters or less.") # indicate that validation failed
        if new_number:
            # if validation passes update number
            if number_validation(): # verifies number input
                update_data["Number"] = new_number
            else:
                entry_number.delete(0, tk.END)
                entry_number.insert(tk.END, "Must be exactly 10 characters")
        if new_address:
            # if validation passes update address
            if address_validation(): # verifies address input
                update_data["Address"] = new_address
            else:
                entry_address.delete(0, tk.END)
                entry_address.insert(tk.END, "Must be 30 characters or less.")

       # TO-DO: MILESTONE 3: add in IF/ELSE statements to update contact on database and also print results   

# his method opens a new window to display the directions for using the application
def open_directions():
    root2 = tk.Tk()
    root2.title("Application Directions - DataBase Functionality Coming Soon")
    root2.configure(bg='Slategray4') # set bg color to gray

    # The following lines create 5 labels to display info, I kept the background the same as the main app to create consistency
    label1_info = tk.Label(root2, text="1. To save contact to database, fill in all fields and click save.", bg='snow3')
    label1_info.grid(row=0, column=2, padx=5, pady=5)

    label2_info = tk.Label(root2, text="2. You can search for a contact by filling in the ID field and clicking search.", bg='snow3')
    label2_info.grid(row=1, column=2, padx=5, pady=5)

    label3_info = tk.Label(root2, text="3. If you want to delete a contact, fill in the ID field and click delete.", bg='snow3')
    label3_info.grid(row=2, column=2, padx=5, pady=5)

    label4_info = tk.Label(root2, text="3. To edit a contact, fill in the ID field and then fill in the info for the field you wish to change and click edit.", bg='snow3')
    label4_info.grid(row=3, column=2, padx=5, pady=5)

    label5_info = tk.Label(root2, text="   Once you click edit any fields that you fill in will be updated on the database.", bg='snow3')
    label5_info.grid(row=4, column=2, padx=5, pady=5)

# he following group of methods were designed to add quality to the buttons appearance, they cause color changes when buttons are hovered over and pressed
def on_hover_save(event):
    save_button.config(bg='DarkSeaGreen1') # green on hover

def on_leave_save(event):
    save_button.config(bg='Slategray1') # gray after hover

def on_hover_delete(event):
    delete_button.config(bg='tomato2') # red on hover

def on_leave_delete(event):
    delete_button.config(bg='Slategray1') # gray after hover

def on_hover_search(event):
    search_button.config(bg='Slategray3') # dark gray on hover

def on_leave_search(event):
    search_button.config(bg='Slategray1') # gray after hover

def on_hover_edit(event):
    edit_button.config(bg='Slategray3') # dark gray on hover

def on_leave_edit(event):
    edit_button.config(bg='Slategray1') # gray after hover

def on_hover_directions(event):
    directions_button.config(bg='Slategray3') # dark gray on hover

def on_leave_directions(event):
    directions_button.config(bg='Slategray1') # gray after hover

# lines 297 through 320 deal with creating and customizing the buttons used in the application
# each button makes a call to one of the methods created above once it is clicked
# button layout is determined by row and column positions

# save button
save_button = tk.Button(root, activebackground='DarkSeaGreen4', bg='Slategray1', border=6, text="Save", command=save_input)
save_button.grid(row=6, column=0, padx=5, pady=5)
save_button.bind('<Enter>', on_hover_save)
save_button.bind('<Leave>', on_leave_save)

# search button
search_button = tk.Button(root, activebackground='Slategray4', bg='Slategray1', border=6, text="Search", command=search_input)
search_button.grid(row=6, column=1, padx=5, pady=5)
search_button.bind('<Enter>', on_hover_search)
search_button.bind('<Leave>', on_leave_search)

# delete button
delete_button = tk.Button(root, activebackground='tomato4', bg='Slategray1', border=6,  text="Delete", command=delete_input)
delete_button.grid(row=6, column=3, padx=5, pady=5)
delete_button.bind('<Enter>', on_hover_delete)
delete_button.bind('<Leave>', on_leave_delete)

# edit button
edit_button = tk.Button(root, activebackground='Slategray4', bg='Slategray1', border=6, text="Edit", command=edit_input)
edit_button.grid(row=6, column=2, padx=5, pady=5)
edit_button.bind('<Enter>', on_hover_edit)
edit_button.bind('<Leave>', on_leave_edit)

# directions button
directions_button = tk.Button(root, activebackground='Slategray4', bg='Slategray1', border=6,  text="Directions", command=open_directions)
directions_button.grid(row=7, column=1, padx=5, pady=5)
directions_button.bind('<Enter>', on_hover_directions)
directions_button.bind('<Leave>', on_leave_directions)

root.mainloop()
