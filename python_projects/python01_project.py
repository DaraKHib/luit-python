import random
import string

def generate_ec2_names():
    # Get user input
    department = input("Enter your department name: ").lower()
    num_instances = int(input("Enter number of EC2 instances needed: "))
    
    ec2_names = set()

    while len(ec2_names) < num_instances:
        # Random 6-character suffix: mix of letters and digits
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ec2_name = f"{department}-{suffix}"
        
        # Ensure uniqueness
        ec2_names.add(ec2_name)

    print("\nGenerated EC2 Instance Names:")
    for name in ec2_names:
        print(name)

if __name__ == "__main__":
    generate_ec2_names()