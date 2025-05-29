import random
import string

def generate_ec2_names() -> None:
    """
    EC2 Random Name Generator

    This script allows users to generate unique EC2 instance names based on their department.
    - Only 'Marketing', 'Accounting', and 'FinOps' departments are allowed.
    - The user is asked for the number of EC2 instances they need.
    - Each name includes the department and a 6-character random alphanumeric suffix.
    """

    # List of allowed departments (in lowercase for easier comparison)
    allowed_departments: set[str] = {"marketing", "accounting", "finops"}

    # Ask user to input their department name
    department_input: str = input("Enter your department (Marketing, Accounting, or FinOps): ").strip().lower()

    # Check if the department is allowed
    if department_input not in allowed_departments:
        print(" Only Marketing, Accounting, or FinOps departments are allowed to use this generator.")
        return

    # Ask how many EC2 instance names to generate
    try:
        num_instances: int = int(input("How many EC2 instance names do you need? "))
    except ValueError:
        print(" Please enter a valid number.")
        return

    # Create a set to hold unique EC2 names
    ec2_names: set[str] = set()

    # Generate names until we have the desired amount
    while len(ec2_names) < num_instances:
        suffix: str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ec2_name: str = f"{department_input}-{suffix}"
        ec2_names.add(ec2_name)

    # Print the results
    print("\n Your EC2 Instance Names:")
    for name in ec2_names:
        print(name)

# Run the function
if __name__ == "__main__":
    generate_ec2_names()
