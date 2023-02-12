public class Contact {
	
	String ID;
	String firstName;
	String lastName;
	String  number;
	String address;
	
	//Default Constructor for Contact object
	public Contact() {
		
	}
	
	//Constructor with arguments for Contact object
	public Contact(String ID, String firstName, String lastName, String number, String address) {
		
		this.ID = setID(ID);
		this.firstName = setFirstName(firstName);
		this.lastName = setLastName(lastName);
		this.number = setNumber(number);
		this.address = setAddress(address);
	
}
	
	// Setters and Getters for each Variable
	//Added if blocks to the setters to ensure variables aren't null and aren't too long


	public String setID(String ID) {
		this.ID = ID;
		return ID;
	}
	
	public String getID() {
		return ID;
	}
	
	public String getFirstName() {
		return firstName;
	}
	
	public String setFirstName(String firstName) {
		this.firstName = firstName;
		return firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public String setLastName(String lastName) {
		this.lastName = lastName;
		return lastName;
	}
	
	public String getNumber() {
		return number;
	}
	
	public String setNumber(String number) {
		this.number = number;
		return number;
	}
	
	public String getAddress() {
		return address;
	}
	
	public String setAddress(String address) {
		this.address = address;
		return address;
	}
	

}
