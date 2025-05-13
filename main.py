import argparse
import boto3
import ec2
import s3
import route53
import cloudwatch

def create_session(access_key, secret_key, region):
    return boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )

def main():
    parser = argparse.ArgumentParser(description="AWS CLI Tool with argparse")
    parser.add_argument('--service', required=True, choices=['ec2', 's3', 'route53', 'cloudwatch'], help='Service to use')
    parser.add_argument('--access_key', required=True, help='AWS Access Key ID')
    parser.add_argument('--secret_key', required=True, help='AWS Secret Access Key')
    parser.add_argument('--region', default='us-east-1', help='AWS Region')
    parser.add_argument('--action', required=False, help='Optional action (used in cloudwatch)')

    args = parser.parse_args()

    session = create_session(args.access_key, args.secret_key, args.region)

    if args.service == 'ec2':
        ec2_client = session.client('ec2')
        ec2.main(ec2_client)
    elif args.service == 's3':
        s3_client = session.client('s3')
        s3.main(s3_client)
    elif args.service == 'route53':
        route53_client = session.client('route53')
        route53.handle_route53(route53_client)
    elif args.service == 'cloudwatch':
        cloudwatch.main(args.access_key, args.secret_key, args.region, args.action)

if __name__ == "__main__":
    main()