import uuid
from botocore.exceptions import ClientError

UNIQUE_TAG_KEY = 'Unique_Key'
UNIQUE_TAG_VALUE = '5tfdogk34vnfkd3'


def handle_route53(route53_client):
    uname = input('Choose a unique name: ').strip()

    while True:
        print("Route53 Options:")
        print("1. Create domain")
        print("2. List domains")
        print("3. Update DNS records")
        print("4. Delete domain")
        print("5. Return to main menu")

        route53_choice = input("Enter your choice: ").strip()

        if route53_choice == "1":
            create_domain(route53_client, uname)
        elif route53_choice == "2":
            list_domains(route53_client)
        elif route53_choice == "3":
            update_dns_records(route53_client)
        elif route53_choice == "4":
            delete_domain(route53_client)
        elif route53_choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def create_domain(route53_client, uname):
    domain_name = input("Enter domain name for the hosted zone: ").strip()
    if not domain_name:
        print("Domain name cannot be empty.")
        return

    caller_reference = str(uuid.uuid4())
    try:
        response = route53_client.create_hosted_zone(
            Name=domain_name,
            CallerReference=caller_reference,
            HostedZoneConfig={
                'Comment': 'Created by CLI',
                'PrivateZone': False
            }
        )
        zone_id = response['HostedZone']['Id'].split('/')[-1]
        print(f"Hosted zone created with ID: {zone_id}")

        add_tags(route53_client, zone_id, uname)
    except ClientError as e:
        print(f"Error creating hosted zone: {e}")


def add_tags(route53_client, zone_id, uname):
    try:
        route53_client.change_tags_for_resource(
            ResourceType='hostedzone',
            ResourceId=zone_id,
            AddTags=[
                {'Key': UNIQUE_TAG_KEY, 'Value': UNIQUE_TAG_VALUE},
                {'Key': 'Uname', 'Value': uname}
            ]
        )
        print("Tags added successfully.")
    except ClientError as e:
        print(f"Error adding tags: {e}")


def list_domains(route53_client):
    try:
        response = route53_client.list_hosted_zones()
        found_match = False
        for zone in response['HostedZones']:
            zone_id = zone['Id'].split('/')[-1]
            if check_zone_tags(route53_client, zone_id):
                print(f"Name: {zone['Name']}, ID: {zone['Id']}")
                found_match = True

        if not found_match:
            print(f"No hosted zones found with the tag {UNIQUE_TAG_KEY}={UNIQUE_TAG_VALUE}.")
            print("You may need to create a domain first.")
    except ClientError as e:
        print(f"Error listing hosted zones: {e}")


def check_zone_tags(route53_client, zone_id):
    try:
        tags_response = route53_client.list_tags_for_resource(
            ResourceType='hostedzone',
            ResourceId=zone_id
        )
        tags = tags_response.get('ResourceTagSet', {}).get('Tags', [])
        return any(tag['Key'] == UNIQUE_TAG_KEY and tag['Value'] == UNIQUE_TAG_VALUE for tag in tags)
    except ClientError as e:
        print(f"Error retrieving tags for hosted zone {zone_id}: {e}")
        return False


def update_dns_records(route53_client):
    hosted_zone_id = input("Enter domain ID: ").strip()
    record_name = input("Enter record name: ").strip()
    record_type = input("Enter record type (A, AAAA, CNAME): ").strip().upper()
    record_value = input("Enter record value: ").strip()

    if not all([hosted_zone_id, record_name, record_type, record_value]):
        print("All fields are required.")
        return

    if record_type not in ['A', 'AAAA', 'CNAME']:
        print("Invalid record type. Please enter A, AAAA, or CNAME.")
        return

    try:
        route53_client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Comment': 'Update record via CLI',
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': record_name,
                            'Type': record_type,
                            'TTL': 300,
                            'ResourceRecords': [{'Value': record_value}]
                        }
                    }
                ]
            }
        )
        print("DNS record updated successfully.")
    except ClientError as e:
        print(f"Error updating DNS record: {e}")


def delete_domain(route53_client):
    try:
        response = route53_client.list_hosted_zones()
        for zone in response['HostedZones']:
            zone_id = zone['Id'].split('/')[-1]
            if check_zone_tags(route53_client, zone_id):
                print(f"Name: {zone['Name']}, ID: {zone['Id']}")
                delete_choice = input("Are you sure you want to delete this zone? (y/n): ").strip().lower()
                if delete_choice == 'y':
                    try:
                        route53_client.delete_hosted_zone(Id=zone_id)
                        print(f"Hosted zone {zone_id} deleted successfully.")
                    except ClientError as e:
                        print(f"Error deleting hosted zone {zone_id}: {e}")
                break
        else:
            print(f"No hosted zones found with the tag {UNIQUE_TAG_KEY}={UNIQUE_TAG_VALUE}.")
            print("You may need to create a domain first.")
    except ClientError as e:
        print(f"Error listing hosted zones: {e}")


if __name__ == "__main__":
    pass
