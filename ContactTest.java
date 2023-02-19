import static org.junit.jupiter.api.Assertions.*;
import static org.junit.Assert.assertEquals;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.function.Executable;

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
	
	//Verify exception is thrown if ID is null
	@Test
	void testNullId() {
		assertThrows(IllegalArgumentException.class, new Executable() {

			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setID(null);
				
			}
			
		});
	}
	
	//Verify exception is thrown if ID is longer than 10 characters
	@Test
	void testLongId() {
		assertThrows(IllegalArgumentException.class, new Executable() {

			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setID("11223344556");
				
			}
			
		});
	}
	
	//Verify exception is thrown if first name is null
	@Test
	void testNullFirstName() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setFirstName(null);
				
			}
			
		});
	}
	
	//Verify exception is thrown if first name is longer than 10 characters
	@Test
	void testLongFirstName() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setFirstName("Long First Name");
				
			}
			
		});
	}
	
	//Verify exception is thrown if last name is null
	@Test
	void testNullLastName() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setLastName(null);
				
			}
			
		});
	}
	
	//Verify exception is thrown if last name is longer than 10 characters
	@Test
	void testLongLastName() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setLastName("Long Last Name");
				
			}
			
		});
	}
	
	//Verify exception is thrown if phone number is null
	@Test
	void testNullNumber() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setNumber(null);
				
			}
			
		});
	}
	
	//Verify exception is thrown if phone number is less than 10 digits
	@Test
	void testShortNumber() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setNumber("123456789");
				
			}
			
		});
	}
	
	//Verify exception is thrown if phone number is greater than 10 digits
	@Test
	void testLongNumber() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setNumber("12345678910");
				
			}
			
		});
	}
	
	//Verify exception is thrown if address is null
	@Test
	void testNullAddress() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setAddress(null);
				
			}
			
		});
	}
	
	//Verify exception is thrown if address is longer than 30 characters
	@Test
	void testLongAddress() {
		assertThrows(IllegalArgumentException.class, new Executable() {
			
			@Override
			public void execute() throws Throwable {
				Contact newCon = new Contact();
				newCon.setAddress("This address is a very long address");
				
			}
			
		});
	}

}
