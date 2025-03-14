import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    instance_id = 'i-04de0ef02ade9172c'
    
    # Modify the instance metadata options
    ec2_client.modify_instance_metadata_options(
        InstanceId=instance_id,
        HttpTokens='optional'
    )
    
    return {
        'statusCode': 200,
        'body': f'Instance {instance_id} modified with IMDSv2 Optional.'
    }