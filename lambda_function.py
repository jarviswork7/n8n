import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    try:
        response = ec2_client.create_tags(
            Resources=['i-08b5ba99795323b9a'],
            Tags=[{'Key': 'Name', 'Value': 'n8n-instance'}]
        )
        return {'status': 'Tagging successful', 'response': response}
    except Exception as e:
        return {'status': 'Tagging failed', 'error': str(e)}