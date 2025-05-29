import random
import string

def generate_ec2_names() -> None:
    """
    EC2 Random Name Generator

    This script allows users to generate a specific number of unique EC2 instance names.
    - The user provides the department name to be included in the instance name.
    - The user provides how many instance names they need.
    - Each name includes the department and a 6-character random alphanumeric suffix.
    """

    # Ask user for their department name
    department_input: str = input("Enter your department name: ").strip()

    # Ask how many EC2 instance names to generate
    try:
        num_instances: int = int(input("How many EC2 instance names do you need? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Set to hold unique EC2 names
    ec2_names: set[str] = set()

    # Generate names until we have the desired amount
    while len(ec2_names) < num_instances:
        suffix: str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ec2_name: str = f"{department_input}-{suffix}"
        ec2_names.add(ec2_name)

    # Print the generated EC2 names
    print("\n Your EC2 Instance Names:")
    for name in ec2_names:
        print(name)

# Run the function
if __name__ == "__main__":
    generate_ec2_names()
