# **Original Code:**

```javascript
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
		
		if (ID == null) {
			throw new IllegalArgumentException("ID can't be null");
		}
		
		if (ID.length() > 10) {
			throw new IllegalArgumentException("ID must be 10 characters or less");
		}
		
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
		
		if (firstName == null) {
			throw new IllegalArgumentException("First name can't be null");
		}
		
		if (firstName.length() > 10) {
			throw new IllegalArgumentException("First name must be 10 characters or less");
		}
		
		this.firstName = firstName;
		return firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public String setLastName(String lastName) {
		
		if (lastName == null) {
			throw new IllegalArgumentException("Last name can't be null");
		}
		
		if (lastName.length() > 10) {
			throw new IllegalArgumentException("Last name must be 10 characters or less");
		}
		
		this.lastName = lastName;
		return lastName;
	}
	
	public String getNumber() {
		return number;
	}
	
	public String setNumber(String number) {
		
		if (number == null) {
			throw new IllegalArgumentException("Phone number can't be null");
		}
		
		if (number.length() != 10) {
			throw new IllegalArgumentException("Phone number must be exactly 10 characters");
		}
		
		this.number = number;
		return number;
	}
	
	public String getAddress() {
		return address;
	}
	
	public String setAddress(String address) {
		
		if (address == null) {
			throw new IllegalArgumentException("Address can't be null");
		}
		
		if (address.length() > 30) {
			throw new IllegalArgumentException("Address must be 30 characters or less");
		}
		
		this.address = address;
		return address;
	}
	

}
```

# **Enhancement One Code:**

[Enhancement One: Ported from Java to Python](https://github.com/JMckinney13/JMckinney13.github.io/blob/main/ArtifactOne.py)

Link should work

# **Enhancement Two Code:**


# **Enhancement Three Code:**
