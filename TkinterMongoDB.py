import tkinter as tk
from pymongo import MongoClient

root = tk.Tk()
root.title("Contact Manager")

label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0, padx=5, pady=5)

entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_first_name = tk.Label(root, text="First Name:")
label_first_name.grid(row=1, column=0, padx=5, pady=5)

entry_first_name = tk.Entry(root)
entry_first_name.grid(row=1, column=1, padx=5, pady=5)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.grid(row=2, column=0, padx=5, pady=5)

entry_last_name = tk.Entry(root)
entry_last_name.grid(row=2, column=1, padx=5, pady=5)

label_number = tk.Label(root, text="Number:")
label_number.grid(row=3, column=0, padx=5, pady=5)

entry_number = tk.Entry(root)
entry_number.grid(row=3, column=1, padx=5, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=4, column=0, padx=5, pady=5)

entry_address = tk.Entry(root)
entry_address.grid(row=4, column=1, padx=5, pady=5)

label_results = tk.Label(root, text="Results:")
label_results.grid(row=5, column=0, padx=5, pady=5)

results_text = tk.Text(root, height=5, width=30)
results_text.grid(row=5, column=1, padx=5, pady=5)

client = MongoClient("mongodb://localhost:27017/")
db = client["Contacts"]
collection = db["NewContacts"]

def input_validation():
    id = entry_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    number = entry_number.get()
    address = entry_address.get()
    if not id:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID can not be empty.")
        return False
    elif len(id) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "ID must be 10 characters or less.")
        return False
    elif not first_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name can not be empty.")
        return False
    elif len(first_name) > 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "First Name must be 10 characters or less.")
        return False
    elif not last_name:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name can not be empty.")
        return False
    elif len(last_name) > 15:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Last Name must be 15 characters or less.")
        return False
    elif not number:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number can not be empty.")
        return False
    elif len(number) != 10:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Number must be exactly 10 characters.")
        return False
    elif not address:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address can not be empty.")
        return False
    elif len(address) > 30:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Address must be 30 characters or less.")
        return False
    else:
        return True

def save_input():
    if input_validation():
        contact = {
            "ID": entry_id.get(),
            "FirstName": entry_first_name.get(),
            "LastName": entry_last_name.get(),
            "Number": entry_number.get(),
            "Address": entry_address.get()
        }
        collection.insert_one(contact)
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Contact saved to the database.")
        entry_id.delete(0,tk.END)
        entry_first_name.delete(0,tk.END)
        entry_last_name.delete(0,tk.END)
        entry_number.delete(0,tk.END)
        entry_address.delete(0,tk.END)

def search_input():
    #if input_validation():
    search_id = entry_id.get()
    search_result = collection.find_one({"ID": search_id})
    if search_result:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"ID: {search_result['ID']}\nFirst Name: {search_result['FirstName']}\nLast Name: {search_result['LastName']}\nNumber: {search_result['Number']}\nAddress: {search_result['Address']}")
    else:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "No contact found with that ID.")

def delete_input():
    if input_validation():
        delete_id = entry_id.get()
        delete_result = collection.delete_one({"ID": delete_id})
        if delete_result.deleted_count > 0:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Contact removed from database.")
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Contact not found.")

def edit_input():
    if input_validation():
        edit_id = entry_id.get()
        new_first_name = entry_first_name.get()
        new_last_name = entry_last_name.get()
        new_number = entry_number.get()
        new_address = entry_address.get()

        update_data = {}
        if new_first_name:
            update_data["FirstName"] = new_first_name
        if new_last_name:
            update_data["LastName"] = new_last_name
        if new_number:
            update_data["Number"] = new_number
        if new_address:
            update_data["Address"] = new_address

        if update_data:
            edit_result = collection.update_one({"ID": edit_id}, {"$set": update_data})
            if edit_result.modified_count > 0:
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END, "Contact updated successfully.")
            else:
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END, "Contact not found.")
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Nothing to update.")

save_button = tk.Button(root, text="Save", command=save_input)
save_button.grid(row=6, column=0, padx=5, pady=5)

search_button = tk.Button(root, text="Search", command=search_input)
search_button.grid(row=6, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", command=delete_input)
delete_button.grid(row=6, column=2, padx=5, pady=5)

edit_button = tk.Button(root, text="Edit", command=edit_input)
edit_button.grid(row=6, column=3, padx=5, pady=5)

root.mainloop()