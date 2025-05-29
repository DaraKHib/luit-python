import random
import string

def generate_ec2_names() -> None:
    """
    Prompts the user for a department name and number of EC2 instances,
    then generates and prints a list of unique EC2 instance names.
    
    Each name is formed by combining the department name with a random 
    6-character alphanumeric suffix.
    
    Example output:
    marketing-A1B2C3
    marketing-XyZ123
    """
    # Get user input for department name and desired instance count
    department: str = input("Enter your department name: ").lower()
    num_instances: int = int(input("Enter number of EC2 instances needed: "))
    
    ec2_names: set[str] = set()  # Store unique instance names

    # Keep generating until we reach the desired count
    while len(ec2_names) < num_instances:
        # Create a random 6-character suffix using letters and digits
        suffix: str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ec2_name: str = f"{department}-{suffix}"
        
        # Add to the set (automatically ensures uniqueness)
        ec2_names.add(ec2_name)

    # Output the generated names
    print("\nGenerated EC2 Instance Names:")
    for name in ec2_names:
        print(name)

# Run the generator when the script is executed directly
if __name__ == "__main__":
    generate_ec2_names()
