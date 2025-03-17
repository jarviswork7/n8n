import boto3
import json

def lambda_handler(event, context):
    try:
        client = boto3.client('lambda', region_name='us-east-1')
        role_arn = 'arn:aws:iam::123456789012:role/execution_role'  # Ensure this IAM Role ARN is correct
        # Create a lambda function
        response = client.create_function(
            FunctionName='daniel',
            Runtime='python3.8',
            Role=role_arn,
            Handler='lambda_function.lambda_handler',
            Code={'ZipFile': b'cHJpbnQoIkhlbGxvLCBXb3JsZCIp'},  # Dummy value, replace with actual zipped code file.
            Description='A simple test lambda function',
            Timeout=15,
            MemorySize=128,
            Publish=True
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Lambda function "daniel" created successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error creating lambda function: {str(e)}')
        }