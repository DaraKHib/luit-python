import random
import string

def generate_ec2_names() -> None:
    """
    EC2 Random Name Generator

    This function prompts the user to input a valid department name and the number of EC2 instance names they want.
    It validates the department against a predefined list (Marketing, Accounting, FinOps), ensuring case insensitivity.
    If valid, it generates and prints the requested number of unique EC2 names with a format of:
        <department>-<random_6_char_suffix>

    Features:
    - Ensures EC2 names are unique.
    - Uses only approved departments.
    - Handles lowercase or uppercase input variations.
    - Encapsulated in a function to satisfy complex-level structure.

    Returns:
        None
    """
    # Define approved departments and normalize them to lowercase
    allowed_departments: set[str] = {"marketing", "accounting", "finops"}

    # Ask the user for department name
    department_input: str = input("Enter your department (Marketing, Accounting, FinOps): ").strip().lower()

    # Validate department
    if department_input not in allowed_departments:
        print("This generator is only for the Marketing, Accounting, and FinOps departments.")
        return  # Exit early if department is not allowed

    # Ask the user how many EC2 names they want
    try:
        num_instances: int = int(input("Enter the number of EC2 instance names to generate: "))
    except ValueError:
        print("Invalid number entered. Please enter a whole number.")
        return

    ec2_names: set[str] = set()  # Store generated names in a set to ensure uniqueness

    # Generate EC2 names until we reach the desired count
    while len(ec2_names) < num_instances:
        # Create a 6-character alphanumeric suffix
        suffix: str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ec2_name: str = f"{department_input}-{suffix}"
        ec2_names.add(ec2_name)

    # Display the results
    print("\n Generated EC2 Instance Names:")
    for name in ec2_names:
        print(name)

# Execute the function when the script is run directly
if __name__ == "__main__":
    generate_ec2_names()
