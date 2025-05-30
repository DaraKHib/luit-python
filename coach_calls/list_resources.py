"""AWS Resource Printer

This script connects to AWS using provided helper functions and prints out
the names of S3 buckets and the IDs of EC2 instances.

Requires:
    - `helpers` module with `get_ec2_client`, `get_s3_client`,
      `list_buckets`, and `describe_instances` functions.
"""

from typing import List, Dict
from helpers import get_ec2_client, get_s3_client, list_buckets, describe_instances

def print_bucket_names(s3_client) -> None:
    """
    Prints the names of all S3 buckets.

    Args:
        s3_client: Boto3 S3 client object.
    """
    bucket_names: List[str] = list_buckets(s3_client)
    
    # Print each S3 bucket name
    for bucket_name in bucket_names:
        print(bucket_name)

def print_instance_ids(ec2_client) -> None:
    """
    Prints the IDs of all EC2 instances.

    Args:
        ec2_client: Boto3 EC2 client object.
    """
    instances: List[Dict] = describe_instances(ec2_client)
    
    instance_ids: List[str] = []

    # Extract instance IDs from the described instances
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    # Print each EC2 instance ID
    for instance_id in instance_ids:
        print(instance_id)

if __name__ == "__main__":
    # Initialize AWS clients
    ec2_client = get_ec2_client()
    s3_client = get_s3_client()

    # Print AWS resources
    print_bucket_names(s3_client)
    print_instance_ids(ec2_client)
