def main(ec2_client):
    while True:

        uname = input("What is your unique name: ")

        # Display main options
        print("EC2 Options:")
        print("1. Create instance")
        print("2. List instances")
        print("3. Start/Stop instance")
        print("4. Terminate instance")
        print("5. Return to main menu")

        ec2_choice = input("Enter your choice: ").strip()

        # Create instance
        if ec2_choice == "1":
            # Ask if user has existing VPC
            has_vpc = input("Do you have an existing VPC? (yes/no): ").strip().lower()
            if has_vpc == "yes":
                vpc_id = input("Enter your existing VPC ID: ").strip()
            else:
                # Create VPC if you don't have one
                print("Creating new VPC")
                try:
                    response = ec2_client.create_vpc(CidrBlock='10.0.0.0/16', InstanceTenancy='default')
                    vpc_id = response['Vpc']['VpcId']
                    ec2_client.modify_vpc_attribute(
                        VpcId=vpc_id,
                        EnableDnsSupport={'Value': True}
                    )
                    ec2_client.modify_vpc_attribute(
                        VpcId=vpc_id,
                        EnableDnsHostnames={'Value': True}
                    )
                    ec2_client.create_tags(
                        Resources=[vpc_id],
                        Tags=[{'Key': 'Unique_Key', 'Value': 'CLI'}, {'Key': 'Uname', 'Value': uname}]
                    )
                    print(f"VPC created with ID: {vpc_id}")
                except Exception as e:
                    print(f"Error creating VPC: {e}")
                    continue

            # Ask if existing Subnet
            has_subnet = input("Do you have an existing Subnet in the VPC? (yes/no): ").strip().lower()
            if has_subnet == "yes":
                subnet_id = input("Enter your existing Subnet ID: ").strip()
            else:
                # Create Subnet if you don't have one
                print("Creating new Subnet")
                try:
                    response = ec2_client.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc_id)
                    subnet_id = response['Subnet']['SubnetId']
                    ec2_client.create_tags(
                        Resources=[subnet_id],
                        Tags=[{'Key': 'Unique_Key', 'Value': 'CLI'}, {'Key': 'Uname', 'Value': uname}]
                    )
                    print(f"Subnet created ID: {subnet_id}")
                except Exception as e:
                    print(f"Error creating Subnet: {e}")
                    continue

            # Details for instance creation
            instance_name = input("What will your instance be called: ")
            instance_type = input("Enter an instance type (t3.nano | t4g.nano): ")
            ami_choice = input("Choose AMI (ubuntu | amazon): ")
            ami_id = "ami-0e86e20dae9224db8" if ami_choice == "ubuntu" else "ami-0182f373e66f89c85"

            # Create instance
            try:
                ec2_client.run_instances(
                    InstanceType=instance_type,
                    ImageId=ami_id,
                    MinCount=1,
                    MaxCount=1,  # Change the number if you want more than 1 instance
                    SubnetId=subnet_id,
                    TagSpecifications=[{
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'Name', 'Value': instance_name},
                            {'Key': 'Uname', 'Value': uname},
                            {'Key': 'Unique_Key', 'Value': 'CLI'}
                        ]
                    }]
                )
                print("Instance created.")
            except Exception as e:
                print(f"Error creating instance: {e}")

        # List instances
        elif ec2_choice == "2":
            try:
                inc_list = ec2_client.describe_instances(
                    Filters=[{
                        'Name': 'tag:Unique_Key',
                        'Values': ['CLI']
                    }, {
                        'Name': 'tag:Uname',
                        'Values': [uname]
                    }]
                )
                for reservation in inc_list['Reservations']:
                    for instance in reservation['Instances']:
                        instance_id = instance['InstanceId']
                        instance_name = next(tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name')
                        print(f"Instance ID: {instance_id}, Name: {instance_name}")
            except Exception as e:
                print(f"Error listing instances: {e}")

        # Start/Stop instance
        elif ec2_choice == "3":
            instance_id = input("Enter instance ID: ")
            action = input("Enter action (start | stop): ").strip().lower()
            try:
                if action == "start":
                    ec2_client.start_instances(InstanceIds=[instance_id])
                    print(f"Instance {instance_id} started.")
                elif action == "stop":
                    ec2_client.stop_instances(InstanceIds=[instance_id])
                    print(f"Instance {instance_id} stopped.")
                else:
                    print("Invalid action.")
            except Exception as e:
                print(f"Error {action} instance: {e}")

        # Terminate instance
        elif ec2_choice == "4":
            instance_id = input("Enter instance ID to terminate: ")
            try:
                ec2_client.terminate_instances(InstanceIds=[instance_id])
                print(f"Instance {instance_id} terminated.")
            except Exception as e:
                print(f"Error terminating instance: {e}")

        # Exit the program
        elif ec2_choice == "5":
            print("Exiting")
            break

        else:
            print("Invalid choice.")
