import ArtifactOne as Artifact
import unittest

#Test cases designed to test ArtifactOne
class ContactClassTest(unittest.TestCase):
    
    #Test the creation of a Contact using the constructor
    def test_creation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertEqual("921", Justin.get_ID())
        self.assertEqual("Justin", Justin.get_firstname())
        self.assertEqual("Mckinney", Justin.get_lastname())
        self.assertEqual("0008675309", Justin.get_number())
        self.assertEqual("Far Far Away", Justin.get_address())

    #The Following test cases each test the validation of input for each variable

    #First Name Validation
    def test_first_name_validation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertRaises(ValueError, lambda: Justin.set_firstname("ThisFirstNameIsTooLong"))
        self.assertRaises(ValueError, lambda: Justin.set_firstname(""))
    
    #ID Validation
    def test_id_validation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertRaises(ValueError, lambda: Justin.set_ID("ThisIDIsTooLong"))
        self.assertRaises(ValueError, lambda: Justin.set_ID(""))  
   
    #Last Name Validation
    def test_last_name_validation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertRaises(ValueError, lambda: Justin.set_lastname("ThisLastNameIsTooLong"))
        self.assertRaises(ValueError, lambda: Justin.set_lastname(""))
    
    #Phone number validation
    def test_number_validation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        #number less than 10
        self.assertRaises(ValueError, lambda: Justin.set_number("123"))
        #number more than 10
        self.assertRaises(ValueError, lambda: Justin.set_number("12345678910"))
        self.assertRaises(ValueError, lambda: Justin.set_number(""))

    #Address Validation
    def test_address_validation(self):
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        self.assertRaises(ValueError, lambda: Justin.set_address("ThisAddressIsWayyyyyToooooLong!"))
        self.assertRaises(ValueError, lambda: Justin.set_address(""))

    #This test case runs through each edit function and verifies that the changes are made correctly
    def test_edit_functions(self):
        Contacts = []
        Jason = Artifact.Contact("01", "Jason", "Yates", "1234567890", "Over at His House")
        Contacts.append(Jason)
        #Test edit_firstname fucntion
        Artifact.edit_firstname(Contacts, "01", "NotJason")
        self.assertEqual(Jason.get_firstname(), "NotJason")
        #Test edit_lastname function
        Artifact.edit_lastname(Contacts, "01", "NotYates")
        self.assertEqual(Jason.get_lastname(), "NotYates")
        #Test edit_number Function
        Artifact.edit_number(Contacts, "01", "1112223333")
        self.assertEqual(Jason.get_number(), "1112223333")
        #Test edit_address function
        Artifact.edit_address(Contacts, "01", "esuoH siH ta revO")
        self.assertEqual(Jason.get_address(), "esuoH siH ta revO")

    #This test case checks to ensure contacts can be created and added to the list via the add_contact method
    def test_add_contact(self):
        Contacts = []
        Artifact.add_contact(Contacts, "01", "Jason", "Yates", "1234567890", "Over at His House")
        self.assertEquals(len(Contacts), 1)
   
    #This test case checks to ensure contacts can be removed from the list via the remove_contact method
    def test_remove_contact(self):
        Contacts = []
        Jason = Artifact.Contact("01", "Jason", "Yates", "1234567890", "Over at His House")
        Contacts.append(Jason)
        Artifact.remove_contact(Contacts, "01")
        self.assertEqual(len(Contacts), 0)
    
    #This test case checks to make sure contacts can be found via the find_contact method
    def test_find_contact(self):
        Contacts = []
        Jason = Artifact.Contact("01", "Jason", "Yates", "1234567890", "Over at His House")
        Justin = Artifact.Contact("921", "Justin", "Mckinney", "0008675309", "Far Far Away")
        Contacts.append(Jason)
        Contacts.append(Justin)
        testContact = Artifact.find_contact(Contacts, "921")
        self.assertEqual(testContact.get_firstname(), "Justin")



    

if __name__ == "__main__":
    unittest.main()