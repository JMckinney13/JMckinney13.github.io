import static org.junit.jupiter.api.Assertions.*;
import static org.junit.Assert.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;

class ContactServiceTest {

	//Test editFirstName method
	@Test
	void testEditFirstName() {
		ArrayList<Contact> contacts = new ArrayList<Contact>();
		Contact newCon = new Contact("1111", "Bob", "Smith", "1122334455", "Bobs house");
		contacts.add(newCon);
		ContactService.editFirstName(contacts, "1111", "NotBob");
		assertEquals(newCon.firstName, "NotBob");
	}
	
	//Test editLastName method
	@Test
	void testEditLastName() {
		ArrayList<Contact> contacts = new ArrayList<Contact>();
		Contact newCon = new Contact("1111", "Bob", "Smith", "1122334455", "Bobs house");
		contacts.add(newCon);
		ContactService.editLastName(contacts, "1111", "NotSmith");
		assertEquals(newCon.lastName, "NotSmith");
	}
	
	//Test editNumber method
	@Test
	void testEditNumber() {
		ArrayList<Contact> contacts = new ArrayList<Contact>();
		Contact newCon = new Contact("1111", "Bob", "Smith", "1122334455", "Bobs house");
		contacts.add(newCon);
		ContactService.editNumber(contacts, "1111", "6677889900");
		assertEquals(newCon.number, "6677889900");
	}
	
	//Test editAddress method
	@Test
	void testEditAddress() {
		ArrayList<Contact> contacts = new ArrayList<Contact>();
		Contact newCon = new Contact("1111", "Bob", "Smith", "1122334455", "Bobs house");
		contacts.add(newCon);
		ContactService.editAddress(contacts, "1111", "Not Bobs house");
		assertEquals(newCon.address, "Not Bobs house");
	}
	
	//Test the addPerson method
	@Test
	void testAddPerson() {
		ArrayList<Contact> contacts = new ArrayList<Contact>();
		ContactService.addPerson(contacts, "2222", "John", "Johnson", "1234567890", "Johns House");
		assertEquals(contacts.size(), 1);
	}
	
	//Test the removePerson method
	@Test
	void testRemovePerson() {
		ArrayList<Contact> contacts = new ArrayList<Contact>();
		Contact Jim = new Contact("1111", "Jim", "Henson", "1234567890", "Muppet Street");
		Contact Tony = new Contact("2222", "Tony", "Stark", "0987654321", "Stark Industries");
		contacts.add(Jim);
		contacts.add(Tony);
		ContactService.removePerson(contacts, "1111");
		assertEquals(contacts.size(), 1);
	}
	
	//Test the findPerson method
	@Test
	void testFindPerson() {
		ArrayList<Contact> contacts = new ArrayList<Contact>();
		Contact Jim = new Contact("1111", "Jim", "Henson", "1234567890", "Muppet Street");
		Contact Tony = new Contact("2222", "Tony", "Stark", "0987654321", "Stark Industries");
		contacts.add(Jim);
		contacts.add(Tony);
		Contact searchContact = ContactService.findPerson(contacts, "2222");
		assertEquals(searchContact.firstName, "Tony");
	}
	
	
	
	

}
