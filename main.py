import boto3
import ec2
import s3
import route53

access_key = input("Enter your AWS Access Key ID: ")
secret_key = input("Enter your AWS Secret Access Key: ")
default_region = 'us-east-1'
region_name = input(f"Enter the AWS region (press enter for default {default_region}): ") or default_region

# Create a session
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region_name
)

# Create clients for the AWS services
ec2_client = session.client('ec2')
s3_client = session.client('s3')
route53_client = session.client('route53')

# Main menu
while True:
    print("Choose a service:")
    print("1. EC2")
    print("2. S3")
    print("3. Route53")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        ec2.main(ec2_client)
    elif choice == "2":
        s3.main(s3_client)
    elif choice == "3":
        route53.handle_route53(route53_client)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
