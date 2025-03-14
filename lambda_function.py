import boto3

def lambda_handler(event, context):
    rds_client = boto3.client('rds', region_name='us-east-1')
    
    try:
        response = rds_client.describe_db_instances()
        db_instances = response['DBInstances']
        
        for db_instance in db_instances:
            if db_instance['DBInstanceIdentifier'] == 'n8n':
                endpoint = db_instance['Endpoint']['Address']
                return {
                    'DBInstanceIdentifier': 'n8n',
                    'Endpoint': endpoint
                }
        return {
            'Error': 'DB Instance n8n not found'
        }
    except Exception as e:
        return {
            'Error': str(e)
        }