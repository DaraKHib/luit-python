import random
import string

def generate_ec2_names() -> None:
    """
    Generate unique EC2 instance names for approved departments.

    This function prompts the user to input:
    - A department name (must be one of: Marketing, Accounting, FinOps)
    - The number of EC2 instance names they need

    It then generates that many unique names in the format:
    <department>-<6 character random string>

    The names are printed out for the user to use in their AWS environment.
    """
    # Set of allowed department names (stored in lowercase for comparison)
    allowed_departments: set[str] = {"marketing", "accounting", "finops"}

    # Prompt user for their department
    department_input: str = input("Enter your department (Marketing, Accounting, FinOps): ").strip().lower()

    # Check if input is valid
    if department_input not in allowed_departments:
        print("⚠️ Sorry, only the Marketing, Accounting, and FinOps departments are allowed to use this tool.")
        return  # Stop the function if department is not approved

    # Ask for the number of EC2 instances
    try:
        num_instances: int = int(input("Enter the number of EC2 instance names you need: "))
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        return

    # Set to store unique names
    ec2_names: set[str] = set()

    # Generate unique names until the set reaches the requested size
    while len(ec2_names) < num_instances:
        # Create a random 6-character alphanumeric suffix
        suffix: str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        # Format: department-suffix
        ec2_name: str = f"{department_input}-{suffix}"
        # Add to the set (ensures uniqueness)
        ec2_names.add(ec2_name)

    # Output the generated EC2 names
    print("\n✅ Here are your unique EC2 instance names:")
    for name in ec2_names:
        print(name)

# Execute the function to verify it works
if __name__ == "__main__":
    generate_ec2_names()
