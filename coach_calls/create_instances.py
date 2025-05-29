from helpers import *

def create_instances(ec2_client, ami_type: str, instance_amount: int = 1) -> None:
    """
    Launches EC2 instances based on the specified AMI type.

    Args:
        ec2_client: A Boto3 EC2 client used to interact with AWS EC2.
        ami_type (str): The type of Amazon Machine Image to use. 
                        Supported values: "Ubuntu", "Linux 2023", "Linux 2".
        instance_amount (int, optional): Number of instances to create. Defaults to 1.

    Returns:
        None
    """
    # Clean up the input to handle inconsistent casing or whitespace
    cleaned_ami_type = ami_type.lower().strip().replace(" ", " ")

    for i in range(instance_amount):
        # Check for AMI type and call the corresponding creation function
        if cleaned_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu")
        elif cleaned_ami_type == "linux 2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023")
        elif cleaned_ami_type == "linux 2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2")
        else:
            print("Unsupported AMI Type")

if __name__ == "__main__":
    # Create the EC2 client
    ec2_client = get_ec2_client()

    # Create default instance (defaults to 1, unsupported AMI since none passed)
    create_instances(ec2_client)

    # Create a single Amazon Linux 2023 instance
    create_instances(ec2_client, ami_type="linux 2023")

    # Create three Amazon Linux 2 instances
    create_instances(ec2_client, ami_type="linux 2", instance_amount=3)
