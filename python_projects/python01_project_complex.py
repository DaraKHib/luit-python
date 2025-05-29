import random
import string

def generate_ec2_names() -> None:
    """
    Prompts the user to input a valid department and the number of EC2 instances they need.
    Validates that the department is allowed (Marketing, Accounting, FinOps).
    Then generates and prints unique EC2 names in the format: <department>-<6-char-random-suffix>.

    Restrictions:
    - Only allows approved departments: Marketing, Accounting, FinOps.
    - Ensures uniqueness of EC2 instance names using a set.
    """
    # Define allowed departments (converted to lowercase for easy comparison)
    allowed_departments = {"marketing", "accounting", "finops"}

    # Prompt user for department input
    department: str = input("Enter your department (Marketing, Accounting, FinOps): ").strip().lower()

    # Validate department
    if department not in allowed_departments:
        print("⚠️ Sorry, only Marketing, Accounting, or FinOps departments may use this generator.")
        return  # Exit the function early if invalid

    # Prompt user for number of EC2 instance names to generate
    try:
        num_instances: int = int(input("Enter number of EC2 instances to generate names for: "))
    except ValueError:
        print("❌ Invalid number. Please enter a valid integer.")
        return

    ec2_names: set[str] = set()  # Set to ensure uniqueness

    # Keep generating until we have the required number of unique names
    while len(ec2_names) < num_instances:
        # Generate a random 6-character alphanumeric suffix
        suffix: str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ec2_name: str = f"{department}-{suffix}"
        ec2_names.add(ec2_name)  # Add to set (duplicates are automatically ignored)

    # Output the results
    print("\n✅ Generated EC2 Instance Names:")
    for name in ec2_names:
        print(name)

# Run the function when the script is executed
if __name__ == "__main__":
    generate_ec2_names()
