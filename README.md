# **Original Code:**

```Python
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Menu
from pymongo import MongoClient
from datetime import date

# This is a fully functioning contact/appointment manager with MongoDB connections
# To use this app you will need to have MongoDB set up and a server currently running for connections
# Once you have a server running you will need to check which port it is running on and use that port number in the connection string below
# example: client = MongoClient("mongodb://localhost:YOURPORTNUMBER/")
# You will also need to either setup a DB named Contacts and a collection named NewContacts or change db and collection variables below to match your own database and collection
# Once everything is setup you can simply run the ContactManager.py file in your command line and your good to go

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
```

# **Enhancement One Code:**

[Enhancement One: Ported from Java to Python](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactOne.py)

Link should work

# **Enhancement Two Code:**


# **Enhancement Three Code:**
