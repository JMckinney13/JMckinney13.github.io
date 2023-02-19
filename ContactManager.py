import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Menu
from pymongo import MongoClient
from datetime import date

# This is a fully functioning contact/appointment manager with MongoDB connections
# To use this app you will need to have MongoDB set up and a server currently running for connections
# Once you have a server running you will need to check which port it is running on and use that port number in the connection string below
# example: client = MongoClient("mongodb://localhost:YOURPORTNUMBER/")
# You will also need to either setup a DB named Contacts and a collection named NewContacts or change db and collection variables below to match your own
# Once everything is setup you can simply run the ContactManager.py file in your command line

# Once the application is running you can click the help menu button on the upper left for usage directions
# The contact manager and appointment manager have their own help directions and help menu button

root = tk.Tk()
root.title("Contact Manager")
root.configure(bg='snow3') # set bg color to gray


# Label and Entry box for ID 
label_id = tk.Label(root, text="ID:", bg='snow3')
label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(root, bg='white', width=10, border=3)
entry_id.grid(row=0, column=1, padx=5, pady=5)

# Label and Entry box for First Name
label_first_name = tk.Label(root, text="First Name:", bg='snow3')
label_first_name.grid(row=1, column=0, padx=5, pady=5)
entry_first_name = tk.Entry(root, bg='white', border=3)
entry_first_name.grid(row=1, column=1, padx=5, pady=5)

# Label and Entry box for Last Name
label_last_name = tk.Label(root, text="Last Name:", bg='snow3')
label_last_name.grid(row=2, column=0, padx=5, pady=5)
entry_last_name = tk.Entry(root, bg='white', border=3)
entry_last_name.grid(row=2, column=1, padx=5, pady=5)

# Label and Entry box for Number
label_number = tk.Label(root, text="Number:", bg='snow3')
label_number.grid(row=3, column=0, padx=5, pady=5)
entry_number = tk.Entry(root, bg='white', border=3)
entry_number.grid(row=3, column=1, padx=5, pady=5)

# Label and Entry box for Address
label_address = tk.Label(root, text="Address:", bg='snow3')
label_address.grid(row=4, column=0, padx=5, pady=5)
entry_address = tk.Entry(root, width=30, bg='white', border=3)
entry_address.grid(row=4, column=1, padx=5, pady=5)

# Label and Entry box for the results 
label_results = tk.Label(root, text="Results:", bg='snow3')
label_results.grid(row=5, column=0, padx=5, pady=5)
results_text = tk.Text(root, bg='white', height=5, width=30, border=3)
results_text.grid(row=5, column=1, padx=5, pady=5)

# MongoDB connection string to connect to MongoDB server(You may need to change this depending on what port your MongoDB server is running on)
client = MongoClient("mongodb://localhost:27017/")
# Sets up the correct database and collection(Change the DB and collection names if you wish to use a different database or collection)
db = client["Contacts"]
collection = db["NewContacts"]

# Function designed to validate input prior to storing on the database. Returns False if it fails or True if it passes validation
# This function also displays info in the results text box to let the user know what they are doing wrong.
def input_validation():
    # Grabs the input from each of the fields
    id = entry_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    number = entry_number.get()
    address = entry_address.get()

    # If/elif to check for empty ID or ID's that are longer than 10 characters
    if not id:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID field can't be empty.")
        return False
    elif len(id) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID must be 10 characters or less.")
        return False
    
    # Elif statements to check for empty first name or first name's that are longer than 10 characters       
    elif not first_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name can't be empty.")
        return False
    elif len(first_name) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name must be 10 characters or less.")
        return False
    
    # Elif statements to check for empty last name or last name's that are longer than 15 characters
    elif not last_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name field can't be empty.")
        return False
    elif len(last_name) > 15:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name must be 15 characters or less.")
        return False
    
    # Elif statements to check for empty number or number's that are't exactly 10 characters
    elif not number:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number field can't be empty.")
        return False
    elif len(number) != 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number must be exactly 10 characters.")
        return False
    
    # Elif statements to check for empty address or addresses that are longer than 30 characters
    elif not address:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address field can't be empty.")
        return False
    elif len(address) > 30:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address must be 30 characters or less.")
        return False
    else:
        return True   # Returns True if all pass

# The following functions are exactly like the main validation function, I broke these up for use in the edit function

# This function is used to validate ID field input
def id_validation():
    id = entry_id.get()
    # Checks for empty id
    if not id:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID field can't be empty.")
        return False
    # Checks for proper length
    elif len(id) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID must be 10 characters or less.")
        return False
    else:
        return True

# This function is used to validate first name field input
def first_name_validation():
    first_name = entry_first_name.get()
    # Checks for empty first_name
    if not first_name: 
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name field can't be empty.")
        return False
    # Checks for proper length
    elif len(first_name) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name must be 10 characters or less.")
        return False
    else:
        return True

# This function is used to validate last name field input
def last_name_validation():
    last_name = entry_last_name.get()
    # Checks for empty last_name
    if not last_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name field can't be empty.")
        return False
    # Checks for proper length
    elif len(last_name) > 15:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name must be 15 characters or less.")
        return False
    else:
        return True

# This function is used to validate number field input
def number_validation():
    number = entry_number.get()
    # Checks for empty number
    if not number:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number field can't be empty.")
        return False
    # Checks for proper length
    elif len(number) != 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number must be exactly 10 character.")
        return False
    else:
        return True

# This function is used to validate address field input
def address_validation():
    address = entry_address.get()
    # Checks for empty address
    if not address:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address field can't be empty.")
        return False
    # Checks for proper length
    elif len(address) > 30:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address must be 30 characters or less.")
        return False
    else:
        return True
        

# Function to save each contact to the database using info user enters into the GUI
def save_input():
    if input_validation():  # Input validation is checked first using the input_validation function
        contact = {
            "_id": entry_id.get(),
            "FirstName": entry_first_name.get(),
            "LastName": entry_last_name.get(),
            "Number": entry_number.get(),
            "Address": entry_address.get()
        }
        # Inserts contact into database and then clears each field to prep for the next contact info
        collection.insert_one(contact)
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Contact saved to the database.")  # displays "Contact saved to the database" message in results box
        entry_id.delete(0,tk.END)
        entry_first_name.delete(0,tk.END)
        entry_last_name.delete(0,tk.END)
        entry_number.delete(0,tk.END)
        entry_address.delete(0,tk.END)

# Searches MongoDB for contact and then displays it in the results text box
def search_input():
    if id_validation():  # Verifies ID field input using id_validation function
        search_id = entry_id.get()
        search_result = collection.find_one({"_id": search_id}) # Uses entered ID as a MongoDB search command to return the contact matching the ID
        if search_result:
            results_text.delete(1.0, tk.END)
            # Formats and displays the contact if a match is found
            results_text.insert(tk.END, f"ID: {search_result['_id']}\nFirst Name: {search_result['FirstName']}\nLast Name: {search_result['LastName']}\nNumber: {search_result['Number']}\nAddress: {search_result['Address']}")
        # Else block is ran if no contact is found matching the search ID
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "No contact found with that ID.")

# Deletes contact from MongoDB if contact is found that matches the search ID
def delete_input():
    if id_validation():  # Verifies ID input by using the id_validation function
        delete_id = entry_id.get()
        delete_result = collection.delete_one({"_id": delete_id})  # Uses delete_id in pymongo command to find and delete contact from DB

        # If contact is found display "contact removed from database" else if not found display "Contact not found"
        if delete_result.deleted_count > 0:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Contact removed from database.")
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Contact not found.")

# Functon allows user to edit various contact fields using the ID field as the search criteria
def edit_input():
    if id_validation():
        edit_id = entry_id.get()
        new_first_name = entry_first_name.get()
        new_last_name = entry_last_name.get()
        new_number = entry_number.get()
        new_address = entry_address.get()
        # Search for contact using ID field info
        match_found = collection.find_one({"_id": edit_id})

        # Empty dictionary
        update_data = {}

        # The following if/else blocks are used to make calls to the individual validation functions to ensure updated fields follow correct input format
        if new_first_name:
            if first_name_validation():
                update_data["FirstName"] = new_first_name
            else:
                entry_first_name.delete(0,tk.END)
                entry_first_name.insert(tk.END, "Must be 10 characters or less.")
        if new_last_name:
            if last_name_validation():
                update_data["LastName"] = new_last_name
            else:
                entry_last_name.delete(0,tk.END)
                entry_last_name.insert(tk.END, "Must be 15 Characters or less.")
        if new_number:
            if number_validation():
                update_data["Number"] = new_number
            else:
                entry_number.delete(0, tk.END)
                entry_number.insert(tk.END, "Must be exactly 10 characters")
        if new_address:
            if address_validation():
                update_data["Address"] = new_address
            else:
                entry_address.delete(0, tk.END)
                entry_address.insert(tk.END, "Must be 30 characters or less.")

        if update_data:
            edit_result = collection.update_one({"_id": edit_id}, {"$set": update_data}) # Updates contact on MongoDB using newly created dictionary named update_data

            # If/else blocks to check MongoDB to see if a contact was ineed modified and displays correct output
            if edit_result.modified_count > 0:
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END, "Contact updated successfully.") # Displays if contact was modified
            else:
                if match_found:
                    results_text.delete(1.0, tk.END)
                    results_text.insert(tk.END, "Nothing to change. New info matches existing database info.") # Displays if update data matches existing data on DB
                else:  
                    results_text.delete(1.0, tk.END)
                    results_text.insert(tk.END, "Contact not found.") # Displays if ID search fails
        else:
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END, "Input validation failed, please review each field and try again.") # Displays if validation fails

# Creates new window in the application to display directions for using the contact manager
def open_directions():
    root2 = tk.Tk()
    root2.title("Directions Window")
    root2.configure(bg='snow3')

    # Create a label for each of the contact manager applicaton directions
    label1_info = tk.Label(root2, text="- To save contact to database, fill in all fields and click save.", bg='snow3')
    label1_info.grid(row=0, column=2, padx=5, pady=5)

    label2_info = tk.Label(root2, text="- You can search for a contact by filling in the ID field and clicking search.", bg='snow3')
    label2_info.grid(row=1, column=2, padx=5, pady=5)

    label3_info = tk.Label(root2, text="- If you want to delete a contact, fill in the ID field and click delete.", bg='snow3')
    label3_info.grid(row=2, column=2, padx=5, pady=5)

    label4_info = tk.Label(root2, text="- To edit a contact, fill in the ID field and then fill in the info for the field you wish to change and click edit.", bg='snow3')
    label4_info.grid(row=3, column=2, padx=5, pady=5)

    label5_info = tk.Label(root2, text="- Once you click edit any fields that you fill in will be updated on the database.", bg='snow3')
    label5_info.grid(row=4, column=2, padx=5, pady=5)


# The following 10 functions are defined to control what happens when buttons are hovered over
def on_hover_save(event):
    save_button.config(bg='DarkSeaGreen1')

def on_leave_save(event):
    save_button.config(bg='Slategray1')

def on_hover_delete(event):
    delete_button.config(bg='tomato2')

def on_leave_delete(event):
    delete_button.config(bg='Slategray1')

def on_hover_search(event):
    search_button.config(bg='Slategray3')

def on_leave_search(event):
    search_button.config(bg='Slategray1')

def on_hover_edit(event):
    edit_button.config(bg='Slategray3')

def on_leave_edit(event):
    edit_button.config(bg='Slategray1')

def on_hover_appointments(event):
    appointments_button.config(bg='Slategray3')

def on_leave_appointments(event):
    appointments_button.config(bg='Slategray1')

# Creates a menu bar titled help that when clicked opens a new window with contact manager usage directions
root.option_add('*tearoff', False)
menubar = Menu(root)
root.config(menu=menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_command(label='Help', command=open_directions) # Calls the open_directions function 


# Create and configure the save button for the contact manager 
save_button = tk.Button(root, activebackground='DarkSeaGreen4', bg='Slategray1', border=6, text="Save", command=save_input)
save_button.grid(row=6, column=0, padx=5, pady=5)
save_button.bind('<Enter>', on_hover_save)
save_button.bind('<Leave>', on_leave_save)
# Create and configure the search button for the contact manager
search_button = tk.Button(root, activebackground='Slategray4', bg='Slategray1', border=6, text="Search", command=search_input)
search_button.grid(row=6, column=1, padx=5, pady=5)
search_button.bind('<Enter>', on_hover_search)
search_button.bind('<Leave>', on_leave_search)
# Create and configure the delete button for the contact manager
delete_button = tk.Button(root, activebackground='tomato4', bg='Slategray1', border=6,  text="Delete", command=delete_input)
delete_button.grid(row=6, column=3, padx=5, pady=5)
delete_button.bind('<Enter>', on_hover_delete)
delete_button.bind('<Leave>', on_leave_delete)
# Create and configure the edit button for the contact manager
edit_button = tk.Button(root, activebackground='Slategray4', bg='Slategray1', border=6, text="Edit", command=edit_input)
edit_button.grid(row=6, column=2, padx=5, pady=5)
edit_button.bind('<Enter>', on_hover_edit)
edit_button.bind('<Leave>', on_leave_edit)



#                                                                       The Following functions Pertain to the Appointment Manager Window                                                           #
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Creates a new application window for managing appointments.
def appointment_window():
    root3 = tk.Tk()
    root3.title("Appointment Manager")
    root3.configure(bg='snow3')
    
    # The following 5 blocks of code create labels and entry boxes for each field
    label_id = tk.Label(root3, text="ID:", bg='snow3')
    label_id.grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(root3, bg='white', border=3)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    label_date = tk.Label(root3, text="Date:", bg='snow3')
    label_date.grid(row=1, column=0, padx=5, pady=5)
    entry_date = tk.Entry(root3, bg='white', border=3)
    entry_date.grid(row=1, column=1, padx=5, pady=5)
    label_info = tk.Label(root3, text='Example. 2023/10/25', bg='snow3') # Provides an example for how the date field should be formatted
    label_info.grid(row=1, column=2, padx=5, pady=5)

    label_time = tk.Label(root3, text='Time:', bg='snow3')
    label_time.grid(row=2, column=0, padx=5, pady=5)
    entry_time = tk.Entry(root3, bg='white', border=3)
    entry_time.grid(row=2, column=1, padx=5, pady=5)

    label_description = tk.Label(root3, text="Description:", bg='snow3')
    label_description.grid(row=3, column=0, padx=5, pady=5)
    entry_description = tk.Entry(root3, bg='white', border=3)
    entry_description.grid(row=3, column=1, padx=5, pady=5)

    label_results = tk.Label(root3, text="Results:", bg='snow3')
    label_results.grid(row=5, column=0, padx=5, pady=5)
    results_text = tk.Text(root3, bg='white', height=5, width=30, border=3)
    results_text.grid(row=5, column=1, padx=5, pady=5)

    # Creates and sets up the tickbox for A.M. or P.M. selection
    #chk_state = tk.BooleanVar()
    #chk_state.set(True)
    chk_state = True
    chk = tk.Checkbutton(root3, bg='snow3', text = 'A.M.', var = chk_state)
    chk.grid(row=2, column= 2)

    # Function to save each contact to the database using info user enters into the GUI
    def save_appointment():
        if appointment_input_validation(): # calls function to validate input
            app_date = entry_date.get()
            year = int(app_date[:4])
            month = int(app_date[6:7])
            day = int(app_date[8:10])

            # chk_state is a boolean whose state is determined by the tick box labeled A.M.
            if chk_state == False:
                am_pm = " PM"
            else:
                am_pm = " AM"
    
            # Create appointment dictionary which is formatted to facilitate saving on the database
            appointment = {
                "_id": entry_id.get(),
                "Date": str(date(year, month, day)),
                "Time": entry_time.get() + am_pm,
                "Description": entry_description.get() 
            }
            # Inserts appointment into database and then clears each field to prep for the next appointments info
            collection.insert_one(appointment)
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment saved to the database.") # Display to show user the appointment was saved 
            entry_id.delete(0, tk.END)
            entry_date.delete(0, tk.END)
            entry_time.delete(0, tk.END)
            entry_description.delete(0, tk.END)

    # Searches MongoDB for appointment and then displays it in the results text box
    def search_appointment():
        search_id = entry_id.get()
        search_result = collection.find_one({"_id": search_id}) # uses search_id to locate appointment on the database
        if search_result:
            results_text.delete(1.0, tk.END)
            # Formats and displays appointment info in results text box
            results_text.insert(tk.END, f"ID: {search_result['_id']}\nDate: {search_result['Date']}\nTime: {search_result['Time']}\nDescription: {search_result['Description']}")
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "No appointment found with that ID") # This will only display if no appointment on the database matches search_id

    # Deletes appointment from MongoDB if appointment is found that matches the delete_id
    def delete_appointment():
        delete_id = entry_id.get()
        delete_result = collection.delete_one({"_id": delete_id})  # uses delete_id in pymongo command to find and delete appointment from database
        # If appointment is deleted
        if delete_result.deleted_count > 0:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment removed from database")
        # appointment is not deleted because a match was not found
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment not found")

    # Function designed to validate input prior to storing on the database. Returns False if it fails or True if it passes validation
    def appointment_input_validation():
        id = entry_id.get()
        app_date = entry_date.get()
        time = entry_time.get()
        description = entry_description.get()

        # First checks to ensure date has been entered, otherwise it will cause issue due to idexing an empty variable
        if app_date:
            # slices date string to format for use in Python Date() function
            year = int(app_date[:4])
            month = int(app_date[6:7])
            day = int(app_date[8:10])
            app_date = date(year, month, day)
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment date can't be empty")
            return False

        # The following if/elif statements are checks to ensure proper input, returns True if it passes or False if it fails
        if app_date < date.today(): # Check to ensure date is not in the past
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment date can't be in the past")
            return False
        elif not id:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment ID can't be empty")
            return False
        elif len(id) > 5:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment ID must be 5 digits or less")
            return False
        elif not time:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment time can't be empty")
            return False
        elif len(time) > 4:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment time must be 4 digits or less")
            return False
        elif not description:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment description can't be empty")
            return False
        elif len(description) > 30:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Appointment description must be 30 characters or less")
        else:
            return True

    # Function to open new window that displays application directions for the appointment manager
    def open_appointment_directions():
        root4 = tk.Tk()
        root4.title("Appointment Directions")
        root4.configure(bg='snow3')

        # The following code creates text labels for each of the directions
        label1_info = tk.Label(root4, text="- To save appointment to database fill in all fields and click save.", bg='snow3')
        label1_info.grid(row=0, column=2, padx=5, pady=5)

        label2_info = tk.Label(root4, text="- You can search for an appointment by using the ID field.", bg='snow3')
        label2_info.grid(row=1, column=2, padx=5, pady=5)

        label3_info = tk.Label(root4, text="- If you want to delete an appointment, fill in the ID field and click delete.", bg='snow3')
        label3_info.grid(row=2, column=2, padx=5, pady=5)

        label4_info = tk.Label(root4, text="- Input time field as 12 hour time, example (9:30) not 2130.", bg='snow3')
        label4_info.grid(row=3, column=2, padx=5, pady=5)

        label5_info = tk.Label(root4, text="- Indicate AM or PM using the tick box to the right of the time field.", bg='snow3')
        label5_info.grid(row=4, column=2, padx=5, pady=5)

    # The following functions define what happens when buttons are hovered over
    def app_on_hover_save(event):
        save_button.config(bg='DarkSeaGreen1')

    def app_on_leave_save(event):
        save_button.config(bg='Slategray1')

    def app_on_hover_delete(event):
        delete_button.config(bg='tomato2')

    def app_on_leave_delete(event):
        delete_button.config(bg='Slategray1')

    def app_on_hover_search(event):
        search_button.config(bg='Slategray3')

    def app_on_leave_search(event):
        search_button.config(bg='Slategray1')

    #Create a menu bar titled help that when clicked opens a new window with appointment manager usage directions
    root3.option_add('*tearoff', False)
    menubar = Menu(root3)
    root3.config(menu=menubar)
    menubar.add_command(label='Help', command=open_appointment_directions)
        
    # Create and configure the save button for the appointment manager 
    save_button = tk.Button(root3, activebackground='DarkSeaGreen4', bg='Slategray1', border=6, text="Save", command=save_appointment)
    save_button.grid(row=6, column=0, padx=5, pady=5)
    save_button.bind('<Enter>', app_on_hover_save)
    save_button.bind('<Leave>', app_on_leave_save)
    # Create and configure the search button for the appointment manager
    search_button = tk.Button(root3, activebackground='Slategray4', bg='Slategray1', border=6, text="Search", command=search_appointment)
    search_button.grid(row=6, column=1, padx=5, pady=5)
    search_button.bind('<Enter>', app_on_hover_search)
    search_button.bind('<Leave>', app_on_leave_search)
    # Create and configure the delete button for the appointment manager
    delete_button = tk.Button(root3, activebackground='tomato4', bg='Slategray1', border=6,  text="Delete", command=delete_appointment)
    delete_button.grid(row=6, column=2, padx=5, pady=5)
    delete_button.bind('<Enter>', app_on_hover_delete)
    delete_button.bind('<Leave>', app_on_leave_delete)


    

# Create and configure the appointments button for the contact manager
appointments_button = tk.Button(root, activebackground='Slategray4', bg='Slategray1', border=6,  text="Appointments", command=appointment_window)
appointments_button.grid(row=7, column=1, padx=5, pady=5)
appointments_button.bind('<Enter>', on_hover_appointments)
appointments_button.bind('<Leave>', on_leave_appointments)



root.mainloop()     