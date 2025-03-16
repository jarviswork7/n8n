import boto3

def create_lambda_function():
    """
    Creates a Lambda function named 'n8n-operations-manager'.
    """
    client = boto3.client('lambda', region_name='us-east-1')
    
    response = client.create_function(
        FunctionName='n8n-operations-manager',
        Runtime='python3.8',
        Role='your-execution-role-arn',  # Replace with your IAM role ARN
        Handler='lambda_function.lambda_handler',
        Code={
            'ZipFile': b"""
def lambda_handler(event, context):
    \"\"\"
    Basic AWS Lambda handler function.
    \"\"\"
    return {
        'statusCode': 200,
        'body': 'Hello from n8n-operations-manager!'
    }
"""
        },
        Timeout=30,
        MemorySize=100,
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n-operations-manager'
        },
        Architectures=['arm64'],
    )
    
    return response

# Invoke the function to create the Lambda function
create_lambda_function()