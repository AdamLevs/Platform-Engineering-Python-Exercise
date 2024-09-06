import boto3
from botocore.exceptions import ClientError


def main(s3):
    while True:
        print("S3 Options:")
        print("1. Create bucket")
        print("2. List buckets")
        print("3. Upload file")
        print("4. Delete bucket")
        print("5. Return to main menu")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                bucket_name = input("Enter bucket name: ").strip()
                full_bucket_name = f"cli.{bucket_name}"
                access_type = input("Enter access type (public | private): ").strip().lower()
                acl = 'public-read' if access_type == 'public' else 'private'

                # Check if bucket already exists
                try:
                    s3.head_bucket(Bucket=full_bucket_name)
                    print(f"Bucket {full_bucket_name} already exists.")
                except ClientError:
                    # Create bucket
                    try:
                        location = s3.meta.region_name
                        if location == 'us-east-1':
                            s3.create_bucket(
                                Bucket=full_bucket_name,
                                ACL=acl
                            )
                        else:
                            s3.create_bucket(
                                Bucket=full_bucket_name,
                                CreateBucketConfiguration={'LocationConstraint': location},
                                ACL=acl
                            )
                        print(f"S3 bucket {full_bucket_name} created with {access_type} access.")
                    except ClientError as e:
                        print(f"Error creating bucket: {e}")

            elif choice == "2":
                response = s3.list_buckets()
                for bucket in response['Buckets']:
                    if bucket['Name'].startswith('cli.'):
                        print(bucket['Name'])

            elif choice == "3":
                file_path = input("Enter file path to upload: ").strip()
                bucket_name = input("Enter the bucket name: ").strip()
                key = input("Enter the key (filename) for the object: ").strip()
                try:
                    s3.upload_file(file_path, bucket_name, key)
                    print(f"File {file_path} uploaded to {bucket_name} with key {key}.")
                except FileNotFoundError:
                    print(f"File {file_path} not found.")
                except ClientError as e:
                    print(f"Error uploading file: {e}")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "4":
                bucket_name = input("Enter the bucket name to delete: ").strip()
                try:
                    confirmation = input(
                        f"Are you sure you want to delete '{bucket_name}'? (Y/N): ").strip().lower()
                    if confirmation != 'y':
                        print("Bucket deletion canceled.")
                        continue

                    # Delete all objects in the bucket
                    while True:
                        response = s3.list_objects_v2(Bucket=bucket_name)
                        if 'Contents' in response:
                            for obj in response['Contents']:
                                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                            print(f"All objects in {bucket_name} have been deleted.")
                        else:
                            break

                    # Delete the bucket
                    s3.delete_bucket(Bucket=bucket_name)
                    print(f"Bucket {bucket_name} deleted.")
                except ClientError as e:
                    print(f"Error deleting bucket or objects: {e}")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")


# Create S3 client and run main
if __name__ == "__main__":
    s3_client = boto3.client('s3')
    main(s3_client)
