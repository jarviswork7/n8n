import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'

# Specify the Instance IDs for which we want to set IMDSv2 to optional
instance_ids = ['i-0d7297d85a0b55558', 'i-00120a83bfd0cd783']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    try:
        # Modify the instance metadata options
        response = ec2.modify_instance_metadata_options(
            InstanceId=event['instance_id'],
            HttpTokens='optional'  # Set IMDSv2 to optional
        )
        return response
    except ClientError as e:
        return {'Error': str(e)}