import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    ec2_client.create_tags(Resources=['i-08b5ba99795323b9a'], Tags=[{'Key': 'name', 'Value': 'n8n-instance'}])
    return 'Instance tagged successfully'