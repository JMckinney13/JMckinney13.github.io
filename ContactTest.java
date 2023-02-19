import static org.junit.jupiter.api.Assertions.*;
import static org.junit.Assert.assertEquals;
import org.junit.jupiter.api.Test;

class ContactTest {
	
	

	//Test making a new contact
	@Test
	void testCreatingContact() {
		Contact bob = new Contact("1111", "Bob", "Smith", "1112223333", "Bobs Address");
		assertEquals(bob.getID(), "1111");
		assertEquals(bob.getFirstName(), "Bob");
		assertEquals(bob.getLastName(), "Smith");
		assertEquals(bob.getNumber(), "1112223333");
		assertEquals(bob.getAddress(), "Bobs Address");
	}


}
