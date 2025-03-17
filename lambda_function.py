import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('lambda', region_name='us-east-1')

    response = client.create_function(
        FunctionName='n8n-daniel',
        Runtime='python3.9',
        Role='arn:aws:iam::123456789012:role/execution_role',  # Assume the default role
        Handler='lambda_function.lambda_handler',
        Code={
            'ZipFile': b"""def lambda_handler(event, context):\n    return 'Hello from Lambda!'""",
        },
        Description='Lambda function for Daniel',
        Timeout=30,
        MemorySize=120,
        Architectures=['arm64'],
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function created successfully!')
    }