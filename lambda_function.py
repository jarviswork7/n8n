import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'

# Modify instance metadata options for a list of instance IDs
instance_ids = ['i-0d7297d85a0b55558', 'i-00120a83bfd0cd783']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    results = {}
    for instance_id in instance_ids:
        try:
            # Modify the instance metadata options to make IMDSv2 optional
            response = ec2.modify_instance_metadata_options(
                InstanceId=instance_id,
                HttpTokens='optional'  # Set IMDSv2 to optional
            )
            results[instance_id] = response
        except ClientError as e:
            results[instance_id] = {'Error': str(e)}
    return results