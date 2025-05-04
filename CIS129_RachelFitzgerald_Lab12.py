# Pet Class Definition
class Pet:
    # Constructor (Initialization of fields)
    def __init__(self, name="", pet_type="", age=0):
        self.name = name
        self.type = pet_type
        self.age = age
    
    # Mutators (Setters)
    def setName(self, name):
        self.name = name
    
    def setType(self, pet_type):
        self.type = pet_type
    
    def setAge(self, age):
        self.age = age
    
    # Accessors (Getters)
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type
    
    def getAge(self):
        return self.age


# Main Program
def main():
    # Declare input variables
    inputName = input("Enter a pet name: ")
    inputType = input("Enter a pet type: ")
    inputAge = int(input("Enter a pet age: "))
    
    # Create a Pet object
    animal = Pet()  # Creating an empty Pet object
    
    # Set values for the pet using mutators
    animal.setName(inputName)
    animal.setType(inputType)
    animal.setAge(inputAge)
    
    # Show values for this pet using accessors
    print("The pet name is", animal.getName())
    print("The pet type is", animal.getType())
    print("The pet age is", animal.getAge())

# Call the main function to run the program
if __name__ == "__main__":
    main()
