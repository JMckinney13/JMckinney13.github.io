    #This code is a ported version of Java code I wrote for the Software Testing and Automation class here at SNHU. I have decided to port the entire code base from Java to Python to display my skills in 
    #software design/engineering. The code was designed to allow someone to be able to create new contacts and add them to a list of contacts. I also added in the ability to search, edit all fields, and 
    #delete contacts. I feel like this port will really highlight my skills in software design/engineering because it shows I have a great understanding of how the code works and how each language may share 
    #some similatities or how in some areas they may be very different. I think this port will also highlight my ability to plan and create functioning code that not only meets the requirements but also does
    #so in a way that is very secure. I tried to think of ways where the code may be unsecure and tried addressing them as best I could with inpout validation and error raising when needed. I also developed 
    #a fairly extensive set of test cases to try to best capture the functionality of the code and to see how it hadles inputs that are outside of those laid out in my validation. This is just the beginning
    #of my journey with this code and I really look forward to taking it to a fully functioning application with an appealing UI and database support to create long term storage for the contacts users create. 


class Contact: 
    
    #The constructur is set up with callbacks to the setters for each variable to edit input validation
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

    

    #Each setter below first checks for valid input before setting. If input is invalid it raises an exceptin to prevent erroneous data making it to the Contact or database
    def set_ID(self, ID):

        if ID == "":
            raise ValueError("ID can't be empty")

        if len(ID) > 10:
            raise ValueError("ID must be 10 characters or less")

        self.ID = ID

    def get_ID(self):
        return self.ID

    def set_firstname(self, firstname):

        if firstname == "":
            raise ValueError("First Name can't be empty")

        if len(firstname) > 10:
            raise ValueError("First Name must be 10 characters or less")

        self.firstname = firstname

    def get_firstname(self):
        return self.firstname

    def set_lastname(self, lastname):

        if lastname == "":
            raise ValueError("Last Name can't be empty")

        if len(lastname) > 15:
            raise ValueError("Last Name must be 15 characters or less")

        self.lastname = lastname

    def get_lastname(self):
        return self.lastname

    def set_number(self, number):
          
        if number == "":
            raise ValueError("Number can't be empty")

        if len(number) != 10:
            raise ValueError("Number must be exactly 10 characters")

        self.number = number

    def get_number(self):
        return self.number

    def set_address(self, address):

        if address == "":
            raise ValueError("Address can't be empty")

        if len(address) > 30:
            raise ValueError("Address must be 30 characters or less")

        self.address = address

    def get_address(self):
        return self.address


#Search for Contact using contact ID
def find_contact(Contacts, searchID):

    #Checks for empty list, if not empty then it loops through contacts searching for a matching ID and returns said match if found
    if len(Contacts) > 0:
        i = 0
        while i < len(Contacts):
            if Contacts[i].get_ID() == searchID:
                c = Contacts[i]
                return c
            i = i + 1
        print("Contact not found")
    else:
        print("Contact list is empty")

#The following four methods allow for variable editing by first searching for contacts using ID and then setting the new values
#1
def edit_firstname(Contacts, searchID, newfirstname):
    editContact = find_contact(Contacts, searchID)
    editContact.set_firstname(newfirstname)
#2
def edit_lastname(Contacts, searchID, newlastname):
    editContact = find_contact(Contacts, searchID)
    editContact.set_lastname(newlastname)
#3
def edit_number(Contacts, searchID, newNumber):
    editContact = find_contact(Contacts, searchID)
    editContact.set_number(newNumber)
#4
def edit_address(Contacts, searchID, newAddress):
    editContact = find_contact(Contacts, searchID)
    editContact.set_address(newAddress)

#Creates and adds a new contact to the list
def add_contact(Contacts, ID, firstname, lastname, number, address):
    newContact = Contact(ID, firstname, lastname, number, address)
    Contacts.append(newContact)
      
#Removes a contact from the list using ID as search criteria
def remove_contact(Contacts, searchID):
    contactRemove = find_contact(Contacts, searchID)
    Contacts.remove(contactRemove)
