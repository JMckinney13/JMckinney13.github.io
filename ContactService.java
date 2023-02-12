import java.util.ArrayList;

public class ContactService {

	
	
	
	public static Contact editFirstName(ArrayList<Contact> contacts, String ID,  String newFirstName) {
		Contact editContact = findPerson(contacts, ID);
		editContact.setFirstName(newFirstName);
		return editContact;
	}
	
	
	public static Contact editLastName(ArrayList<Contact> contacts, String ID, String newLastName) {
		Contact editContact = findPerson(contacts, ID);
		editContact.setLastName(newLastName);
		return editContact;
	}
	
	
	public static Contact editNumber(ArrayList<Contact> contacts, String ID, String newNumber) {
		Contact editContact = findPerson(contacts, ID);
		editContact.setNumber(newNumber);
		return editContact;
	}
	
	
	public static Contact editAddress(ArrayList<Contact> contacts, String ID, String newAddress) {
		Contact editContact = findPerson(contacts, ID);
		editContact.setAddress(newAddress);
		return editContact;
	}
	
	
	public static Contact addPerson(ArrayList<Contact> contacts, String ID, String firstName, String lastName, String number, String address) {
		Contact newContact = new Contact(ID, firstName, lastName, number, address);
		contacts.add(newContact);
		return newContact;
	}
	
	
	public static Contact removePerson(ArrayList<Contact> contacts, String ID) {
		Contact contact = findPerson(contacts, ID);
		contacts.remove(contact);
		return contact;
	}
	
	
	public static Contact findPerson(ArrayList<Contact> contacts, String ID)
	{
		Contact c = null;
		for(int i = 0; i < contacts.size(); i++)
		{
			
			if(contacts.get(i).getID().
					indexOf(ID) != -1)
				c = contacts.get(i);
		}
		return c;
	}
	
		
	}
