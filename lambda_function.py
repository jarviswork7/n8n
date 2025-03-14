import boto3

def lambda_handler(event, context):
    rds_client = boto3.client('rds', region_name='us-east-1')
    instances = rds_client.describe_db_instances()
    rds_details = []
    for instance in instances['DBInstances']:
        instance_info = {
            'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
            'DBInstanceClass': instance['DBInstanceClass'],
            'Engine': instance['Engine'],
            'DBInstanceStatus': instance['DBInstanceStatus'],
            'AllocatedStorage': instance['AllocatedStorage'],
            'StorageType': instance['StorageType'],
            'MultiAZ': instance['MultiAZ']
        }
        rds_details.append(instance_info)
    return rds_details