import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')

    response = client.create_function(
        FunctionName='n8n-my-function',
        Runtime='python3.9',
        Role='<YOUR_IAM_ROLE_ARN>',
        Handler='index.lambda_handler',
        Code={
            'ZipFile': b'<YOUR_ZIP_FILE_CONTENT>'
        },
        Description='My Lambda function for n8n operations',
        Timeout=30,
        MemorySize=128,
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function created successfully!')
    }