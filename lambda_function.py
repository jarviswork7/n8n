import boto3

def lambda_handler(event, context):
    client = boto3.client('rds', region_name='us-east-1')
    response = client.describe_db_instances(DBInstanceIdentifier='n8n')
    
    engine_version = response['DBInstances'][0]['EngineVersion']
    
    return {
        'EngineVersion': engine_version
    }