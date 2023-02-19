    
# **Self Assessment:** 

  When I first started my Computer Science degree at Southern New Hampshire University I knew only the very basicss of coding. I had previously written very simple code I had learned from tutorials and had taken a few courses at freecodecamp, but for the most part I was a begineer when it came to writing and managing code. It was a bit challenging at first as I was learnig each new concept but as time went on and I became more and more confident each class became a little less frustrating and great deal more fun. I quickly realized that I had made the right choice in selecting computer science as my major. 

  I have learned so many great things here at SNHU. I learned how to work collaboratively in a team environment in the collaboration and team project class. In this class we all go the chance to work on a single project where we learned how to create branches and create push/pull requests to work as one to complete a single goal. I really enjoyed this class because it gave me a glimpse into how things may be once I land a job and get to be part of a team working on projects together. In the software development life-cycle class I learned all about what it was like being a member of an agile based scrum team. In this class I learned how each member has certain roles and I also learned what each of those roles did and how they interacted and communicated with stake holders. I feel like this class did a really good job of giving insight into what goes on during the many stages of a products life-cylce and how each members roles play into the bigger picture. 

  I gained a great deal of insight into how important security is when I am writing code in the software security class. In this class I learned how to write secure code and how to handle errors in a way that doesn't give attackers the advantage. I also learned how to protect user data using various encryption/decryption tactics and a great deal about which encyption protocols were the most secure. In the client and server development class I learned all about using MongoDB and how to combine it with python using the Pymongo library. This class taught me a great deal about incorporating databases into my applications to create a form of long term storage so that information could be retrieved later for various uses. These are just a few examples of the many things I have learned in my four years here at SNHU, and it only scratches the surface of the many talents I have acquired along the way. 
  
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
The first enhancement was accomplished to showcase my abilities in software design and engineering. I decided to showcase these abilities by porting the original code from Java to Python, and along the way I added a few enhancements to make the code more secure. I believe this artifact does an excellent job of showcasing my skills in software development because it highlights my ability to not only port from another language but to also increase security in the process. The first hurdle of this enhancemnt was the port, I consider myself very skilled in Python so this part was pretty easy and I had alot of fun doing it. Once the port was completed I started to improve on the code to provide a much more refined product in comparison to the original. I noticed during my code review that the original lacked input validation so I worked towards correcting that problem. I addressed input validation through the use of if statements in the setters for each variable. The addition of input validation meets course outcome 5 because I found and eradicated a security vulnerability as well as ensured all data was explicitly validated. Below is a snippet demonstrating this validation:
``Python
  # Setter for firstname
    def set_firstname(self, firstname):

        # Raises an error if firstname is empty
        if firstname == "":
            raise ValueError("First Name can't be empty")
        # Raises an error if firstname is greater than 10 characters
        if len(firstname) > 10:
            raise ValueError("First Name must be 10 characters or less")

        self.firstname = firstname
``
I also added a more verbose set of test cases for the code to ensure each edge case was tested and that the test cases provided a more thorough coverage of the code base. Adding in the test cases was the most challenging part for me, I have a decent amount of experience with test cases but the challenge was thinking of which areas needed to be tested and how I would test them. I really enjoyed getting the opurtunity to improve on code I had previously written and learned some new things along the way. One thing I learned was how to use and implement dunder methods, I had never really had the oppurtunity to use them in the past but decided to use one here to format up the default print() function to better display the contact data. 

The code for enhancement one can be found below:
[Enhancement One: Ported from Java to Python](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactOne.py)

[Enhancement One: Test Cases](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactTest.py)

# **Enhancement Two Code:**

[Enhancement Two: Added GUI Functionality](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactTwo.py)


# **Enhancement Three Code:**

[Enhancement Three: Added Database Functionality](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ContactManager.py)
