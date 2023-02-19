    # This code is a ported version of Java code I wrote for the Software Testing and Automation class here at SNHU. I decided to port the entire code base from Java to Python 
    # to display my skills in software design/engineering. The code was designed to allow someone to be able to create new contacts and add them to a list of contacts.
    # I also added in the ability to search, edit all fields, and delete contacts.
    
    
class Contact: 
    
    #The constructur is set up with callbacks to the setters to aid in input validation for each individual variable
    def __init__(self, ID, firstname, lastname, number, address):
        self.set_ID(ID)
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_number(number)
        self.set_address(address)

    #I created this magic/dunder method to control how contacts are displayed when using the print() function
    #This output will be very user friendly and easy to read
    def __str__(self):
        return "ID: " + self.get_ID() + "\nFirst: " + self.get_firstname() + "\nLast: " + self.get_lastname() + "\nPhone Number: " + self.get_number() + "\nAddress: " + self.get_address()

    

    # Setter for ID
    def set_ID(self, ID):
        
        # Raises an error if ID is empty
        if ID == "":
            raise ValueError("ID can't be empty")
        #Raises an error if ID is greater than 10 characters
        if len(ID) > 10:
            raise ValueError("ID must be 10 characters or less")

        self.ID = ID
        
    # Getter for ID
    def get_ID(self):
        return self.ID
    
    # Setter for firstname
    def set_firstname(self, firstname):

        # Raises an error if firstname is empty
        if firstname == "":
            raise ValueError("First Name can't be empty")
        # Raises an error if firstname is greater than 10 characters
        if len(firstname) > 10:
            raise ValueError("First Name must be 10 characters or less")

        self.firstname = firstname

    # Getter for firstname
    def get_firstname(self):
        return self.firstname
    
    # Setter for lastname
    def set_lastname(self, lastname):

        # Raises error if lastname is empty
        if lastname == "":
            raise ValueError("Last Name can't be empty")
        # Raises error if lastname is greater than 15 characters
        if len(lastname) > 15:
            raise ValueError("Last Name must be 15 characters or less")

        self.lastname = lastname

    # Getter for lastname
    def get_lastname(self):
        return self.lastname
    
    # Setter for lastname
    def set_number(self, number):
          
        # Raises error if number is empty
        if number == "":
            raise ValueError("Number can't be empty")
        # Raises error if number isn't exactly 10 characters
        if len(number) != 10:
            raise ValueError("Number must be exactly 10 characters")

        self.number = number

    # Getter for number
    def get_number(self):
        return self.number

    # Setter for address
    def set_address(self, address):

        # Raises error if address is empty
        if address == "":
            raise ValueError("Address can't be empty")
        # Raises error if address is greater than 30 characters
        if len(address) > 30:
            raise ValueError("Address must be 30 characters or less")

        self.address = address

    # Getter for address
    def get_address(self):
        return self.address


#Search for Contact using contact ID
def find_contact(Contacts, searchID):

    # Checks for empty list first
    if len(Contacts) > 0:
        i = 0 # Starts iteration at index 0
        # Loops until the end of the list
        while i < len(Contacts):
            if Contacts[i].get_ID() == searchID: # Checks for matching contact
                searchContact = Contacts[i] # Sets searchContact to the value of the contact at the matching index
                return searchContact
            i = i + 1
        print("Contact not found")
    else:
        print("Contact list is empty")

# Finds contact using find_contact then updates contacts firstname
def edit_firstname(Contacts, searchID, newfirstname):
    editContact = find_contact(Contacts, searchID) # Search for contact
    editContact.set_firstname(newfirstname) # Set new firstname
    
# Finds contact using find_contact then updates contacts lastname
def edit_lastname(Contacts, searchID, newlastname):
    editContact = find_contact(Contacts, searchID) # Search for contact
    editContact.set_lastname(newlastname) # Set new lastname
    
# Finds contact using find_contact then updates contacts number
def edit_number(Contacts, searchID, newNumber):
    editContact = find_contact(Contacts, searchID) # Search for contact
    editContact.set_number(newNumber) # Set new number
    
# Finds contact using find_contact then updates contacts address
def edit_address(Contacts, searchID, newAddress):
    editContact = find_contact(Contacts, searchID) # Search for contact
    editContact.set_address(newAddress) # Set new address

#Creates and adds a new contact to the list
def add_contact(Contacts, ID, firstname, lastname, number, address):
    newContact = Contact(ID, firstname, lastname, number, address)
    Contacts.append(newContact)
      
#Removes a contact from the list using ID as search criteria
def remove_contact(Contacts, searchID):
    contactRemove = find_contact(Contacts, searchID)
    Contacts.remove(contactRemove)
