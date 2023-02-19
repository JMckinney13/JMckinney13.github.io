    
# **Self Assessment:** 

  When I first started my Computer Science degree at Southern New Hampshire University I knew only the very basicss of coding. I had previously written very simple code I had learned from tutorials and had taken a few courses at freecodecamp, but for the most part I was a begineer when it came to writing and managing code. It was a bit challenging at first as I was learning each new concept but as time went on and I became more and more confident each class became a little less frustrating and a great deal more fun. I quickly realized that I had made the right choice in selecting computer science as my major. 

  I have learned so many great things here at SNHU. I learned how to work collaboratively in a team environment in the collaboration and team project class. In this class we all got the chance to work on a single project where we learned how to create branches and create push/pull requests to work as one to complete a single goal. I really enjoyed this class because it gave me a glimpse into how things may be once I land a job and get to be part of a team working on projects together. In the software development life-cycle class I learned all about what it was like being a member of an agile based scrum team. In this class I learned how each member has certain roles and I also learned what each of those roles did and how they interacted and communicated with stake holders. I feel like this class did a really good job of giving insight into what goes on during the many stages of a products life-cycle and how each members roles play into the bigger picture. 

  I gained a great deal of insight into how important security is while writing code in the software security class. In this class I learned how to write secure code and how to handle errors in a way that doesn't give attackers the advantage. I also learned how to protect user data using various encryption/decryption tactics and a great deal about which encyption protocols were the most secure. In the client and server development class I learned all about using MongoDB and how to combine it with python using the Pymongo library. This class taught me a great deal about incorporating databases into my applications to create a form of long term storage so that information could be retrieved later for various uses. These are just a few examples of the many things I have learned in my four years here at SNHU, and it only scratches the surface of the many talents I have acquired along the way. 
  
The goal of this project is to meet the following course outcomes:

1. Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science 

2. Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts

3. Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices

4. Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals

5. Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources

# **Code Review:**
The following code review was conducted on the original code base to showcase the code in its original form and to layout the enhancement process and what my future plans will be for the code overall. In this review I go through each of the four classes that make up the original code and explain what the code was designed for. This code review meets the following course outcomes:  Outcome One "Employ strategies for building collaborative environments that enable diverse
audiences to support organizational decision making in the field of computer science" and outcome two " Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts". It meets these two outcomes because the code review was conducted in a very thorough manner and does a good job of explaining the code at hand as well as the future enhancement plan. It demonstrates my ability to understand the importance of a code review and showcases my ability to work and communicate in a collaborative manner. The code review can be found here: [Code Review](https://www.dropbox.com/s/7nfzy7g569nk6ho/CodeReview%20%281%29.avi?dl=0)
    
# **Original Code:**
I chose to use the same code base to address all three enhancement categories so I will conduct the narrative for the artifact one time here. The original code was designed to allow users to create contacts, it also had functionality that allowed users to add or remove contacts on an array. I chose this particular code base because it was something I designed very early in my Computer Science journey so I was excited to see how I could improve it now that my skills have grown. The code is very basic in structure and one thing I noticed during my initial code review is that it was severely lacking in comments, input validation, and error handling. I think this code does a good job of showcasing my skills at this early stage in my computer science career, it is bug/error free and the logic is sound. It showcases my ability to create classes that address a specific need as well as my ability to create test cases to ensure the code is technically sound.  

The original code base can be found at the following links: [Contact Class](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/Contact.java) and [Contact Service CLass](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ContactService.java)

The test cases for the code can be found at the following links: [Contact Service Test](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ContactServiceTest.java) and [Contact Test](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ContactTest.java)



# **Enhancement One Code:**
The first enhancement was accomplished to showcase my abilities in software design and engineering. I decided to showcase these abilities by porting the original code from Java to Python, and along the way I added a few enhancements to make the code more secure. I believe this artifact does an excellent job of showcasing my skills in software development because it highlights my ability to not only port from another language but to also increase security in the process. The first hurdle of this enhancemnt was the port, I consider myself very skilled in Python so this part was pretty easy and I had alot of fun doing it. Once the port was completed I started to improve on the code to provide a much more refined product in comparison to the original. I noticed during my code review that the original lacked input validation so I worked towards correcting that problem. I addressed input validation through the use of if statements in the setters for each variable. The addition of input validation meets the 5th course outcome because I found and eradicated a security vulnerability as well as ensured all data was explicitly validated. Below is a snippet demonstrating this validation:
```Python
  
    def set_firstname(self, firstname):

        # Raises an error if firstname is empty
        if firstname == "":
            raise ValueError("First Name can't be empty")
        # Raises an error if firstname is greater than 10 characters
        if len(firstname) > 10:
            raise ValueError("First Name must be 10 characters or less")

        self.firstname = firstname 
```

I also added a more verbose set of test cases for the code to ensure each edge case was tested and that the test cases provided a more thorough coverage of the code base. Adding in the test cases was the most challenging part for me, I have a decent amount of experience with test cases but the challenge was thinking of which areas needed to be tested and how I would test them. Below is an example of some of the test cases I designed:
```Python
 # Test the creation of a Contact using the constructor
    def test_creation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertEqual("921", Justin.get_ID())
        self.assertEqual("Justin", Justin.get_firstname())
        self.assertEqual("Mckinney", Justin.get_lastname())
        self.assertEqual("0008675309", Justin.get_number())
        self.assertEqual("Far Far Away", Justin.get_address())

    # The Following test cases each test the validation of input for each variable

    # First Name Validation
    def test_first_name_validation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertRaises(ValueError, lambda: Justin.set_firstname("ThisFirstNameIsTooLong"))
        self.assertRaises(ValueError, lambda: Justin.set_firstname(""))
    
    # ID Validation
    def test_id_validation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertRaises(ValueError, lambda: Justin.set_ID("ThisIDIsTooLong"))
        self.assertRaises(ValueError, lambda: Justin.set_ID(""))  
```
I really enjoyed getting the opurtunity to improve on code I had previously written and learned some new things along the way. One thing I learned was how to use and implement dunder methods, I had never really had the oppurtunity to use them in the past but decided to use one here to format up the default print() function to better display the contact data. The main feedback I recieved on this artifact was to try and highlight how the artifact addressed each of the course outcomes, I have tried to encorporate that feedback and better illustrate each course outcome. 

The code for enhancement one can be found below:
[Enhancement One: Ported from Java to Python](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactOne.py)

[Enhancement One: Test Cases](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactTest.py)

# **Enhancement Two Code:**
The second enhancement was accomplished to showcase my skills in algorithms and data structures. I used the same code base for this enhancement as I did in enhancement one. I truly believe this artifact does a great job of showcasing my abilities in algorithms and data structures because I increased the overall complexity of the code and added in a complete graphical user interface. The GUI that I added allows the user to create contacts in a very easy to use way and I even added in effects such as buttons changing when hovered over just to give it a more polished appearance. The GUI addition meets the 3rd course outcome because I programmed solutions to solve logic problems and implemented them in software. An example of this is when I had to figure out a way to incorporate the edit function into the GUI and you can see below how I was able to do it:
```Python
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
```
This artifact also meets the 1st course outcome due to the fact I used very descriptive comments throughout the code. This effective use of comments clearly demonstrates my ability to work in a collaborative environment because anyone could come behind me and pickup working on this project with ease. The result of this enhancement is that I now have a fully functioning application that allows users to create and edit contacts using a GUI. The addition of the GUI proved to be very difficult as I have little experience with Tkinter, however, incorporating input validation alongside this GUI was a real challenge for me and I really enjoyed the experience. I had to design the input validation in a way that would not only check the input but also provide feedback to the user. I did this by making use of some if/else statements to check input and the .insert Tkinter command to display feedback. I learned a great deal while coding this artifact, as I mentioned earlier I am new to Tkinter so the whole process was a great learning experience and I now feel very comfortable having it in my tool belt. I also learned a great deal about how to improve the appearance of Tkinter windows by implementing color changes when buttons are hovered over. You can see an example of this below:

```Python
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
```

The code for this artifact can be found below:

[Enhancement Two: Added GUI Functionality](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactTwo.py)


# **Enhancement Three Code:**
The code base that I chose for this artifact is the same one that I used in Milestone one and two. It is code that I designed in the Software Testing and Automation class here at SNHU. The code was written to allow the creation of contacts and provided the user with the options to add, delete, edit, or search for contacts stored on an array. The original code was meant to be a portion of a larger project, alone it really didn’t accomplish much. I wanted to change that by making it a fully functional application. I chose this code because I designed it from scratch earlier in my programming journey, and I really wanted to see how much I could add to it now that I have advanced farther in my degree. This artifact does a good job of showing my skills in writing code that is error free and free of any logic errors. It also showcases my ability to create and implement code that addresses a need in a very secure way. The artifact was enhanced in many ways, the first enhancement was porting it from Java to Python. The second enhancement was designing and implementing a graphical user interface that was easy to use, efficient, and secure. The final enhancement was to implement the usage of MongoDB to create a permanent form of storage for the contacts. I also added a new section for creating appointments. The appointment manager section has its own window and acts very similar to the contact manager portion. 

This artifact meets the following course outcomes:

The 1st course outcome because I provided contextual, in-code comments that resulted in easily readable and understandable code. You can clearly see this throughout my entire code as I utilized comments to ensure someone could easily come behind me and know what was happening at each step of the process. You can see an example of this in the following snippet:
```Python
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

```
This code also meets the 4th course outcome because it demonstrates my ability to create industry-standard software designs and I created more robust and efficient code that delivers value. You can see an example below of my code being efficient, instead of handling input validation inside of each function I created a seperate function for validation and called that function when it was needed. Input validation being called by search_input() function:
```Python
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
```
The final course outcome that this code meets is outcome 5. It meets this outcome because when designing this code I found and eradicated any security vulnerabilities or flaws, and also because I ensured all data was explicitly validated. You can see an example of my input validation logic below:
```Python
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
```
I really enjoyed coding this artifact mainly because the orginal code base was written early in my computer science career so I had alot of fun really demonstrating how far I have came since the beginning. It was a wonderful experience getting to take something that was useless on its own to a fully functioning application, this was the first time I have ever had the oppurtunity to do something like this on my own. I learned so many things throughout the course of this final enhancement. I learned how to incorporate a database into a python code base through the use of the Pymongo libray. I also learned how to retrieve info from a database and edit it all while maintaning proper input validation. I even learned how to create drop down menu items, in this artifact I utilyzed a drop down menu to add in the help menu. I think one of the hardest parts for me was figuring out how to take the data from the GUI, pass it through validation and then save it into the database. It took me a while to really figure out the logic behind that process but I was able to do it by utilyzing online resources and going back over past course materials from previous classes here at SNHU. I also found it challenging just figuring out the layout of each window, however, this part was also really enjoyable. I enjoyed it because it gave me the power to edit the window how I saw fit. It was really great seeing the whole thing come together as one working application in the end, it gave me a great sense of accomplishment and I look forward to doing things like this as a career. 

The code for the final enhancement can be found below:
[Enhancement Three: Added Database Functionality](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ContactManager.py)
