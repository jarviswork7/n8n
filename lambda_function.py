import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('lambda', region_name='us-east-1')
    role_arn = 'arn:aws:iam::123456789012:role/execution_role'  # Replace with the correct IAM Role ARN
    
    # Create a lambda function
    response = client.create_function(
        FunctionName='daniel',
        Runtime='python3.8',
        Role=role_arn,
        Handler='index.handler',
        Code={
            'ZipFile': b"PHRoaXMgaXMgYSBwbGFjZWhvbGRlciBmb3IgdGhlIGxhbWJkYSBjb2RlLg==" # Base64 of a simple function
        },
        Description='A simple test lambda function',
        Timeout=15,
        MemorySize=128,
        Publish=True
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function "daniel" is created')
    }