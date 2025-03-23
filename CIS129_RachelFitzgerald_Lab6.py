import math

# Function to calculate the total number of hot dogs needed
def get_total_hot_dogs():
    # Local variables
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))
    
    # Calculate the total number of hot dogs needed
    total = people * hot_dogs
    return total

# Function to display the results
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    # Display the minimum packages of hot dogs needed
    print(f"Minimum packages of hot dogs needed: {min_dogs}")
    
    # Display the minimum packages of buns needed
    print(f"Minimum packages of hot dog buns needed: {min_buns}")
    
    # Display the number of hot dogs left over
    print(f"Hot dogs left over: {dogs_left}")
    
    # Display the number of hot dog buns left over
    print(f"Hot dog buns left over: {buns_left}")

# Main module
def main():
    # Get the total number of hot dogs needed
    total = get_total_hot_dogs()
    
    # Named constants for the package sizes
    DOGS = 10   # Hot dogs in a package
    BUNS = 8    # Hot dog buns in a package
    
    # Calculate the number of leftover hot dogs
    dogs_left = total % DOGS
    
    # Calculate the minimum number of packages of hot dogs
    min_dogs = math.ceil(total / DOGS)
    
    # Calculate the number of leftover hot dog buns
    buns_left = total % BUNS
    
    # Calculate the minimum number of packages of hot dog buns
    min_buns = math.ceil(total / BUNS)
    
    # Display the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)

# Run the program
if __name__ == "__main__":
    main()
