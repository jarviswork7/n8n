import boto3
from botocore.exceptions import ClientError
import json

# Initialize a session using Amazon RDS
client = boto3.client('rds', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        # Get RDS instances
        response = client.describe_db_instances()
        
        # Extracting the DB instances details
        db_instances = response['DBInstances']
        
        # Formatting the output
        instances_info = []
        for instance in db_instances:
            instance_info = {
                'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
                'DBInstanceClass': instance['DBInstanceClass'],
                'Engine': instance['Engine'],
                'DBInstanceStatus': instance['DBInstanceStatus'],
                'MasterUsername': instance['MasterUsername'],
                'Endpoint': instance['Endpoint']['Address'],
                'AllocatedStorage': instance['AllocatedStorage'],
                'InstanceCreateTime': str(instance['InstanceCreateTime']),
                'AvailabilityZone': instance['AvailabilityZone']
            }
            instances_info.append(instance_info)
        
        # Return the JSON serialized list of instances
        return {
            'statusCode': 200,
            'body': json.dumps(instances_info)
        }
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }