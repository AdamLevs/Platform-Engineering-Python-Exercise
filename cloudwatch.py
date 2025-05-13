import logging
import watchtower
from botocore.exceptions import ClientError

def main(session, action=None):
    try:
        sts = session.client('sts')
        identity = sts.get_caller_identity()
        print(f"[CloudWatch] Connected as: {identity['Arn']}")

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = watchtower.CloudWatchLogHandler(
            boto3_session=session,
            log_group='aws-cli-devops'
        )
        logger.addHandler(handler)

        logger.info("CloudWatch logger initialized successfully.")
        logger.info(f"Running cloudwatch service with action: {action}")
        print(f"[CloudWatch] Logged action: {action}")

    except ClientError as e:
        print(f"[CloudWatch] AWS ClientError: {e}")
    except Exception as e:
        print(f"[CloudWatch] Unexpected error: {e}")
