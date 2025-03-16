import boto3

def create_lambda_function():
    """
    Creates an AWS Lambda function using the specified handler and code.
    """
    # Initialize a boto3 client for Lambda
    client = boto3.client('lambda', region_name='us-east-1')

    # Read the zipped code containing the lambda_handler
    with open('function.zip', 'rb') as f:
        zipped_code = f.read()

    # Create the Lambda function
    response = client.create_function(
        FunctionName='n8n-operations-manager',
        Runtime='python3.8',  # Using Python runtime
        Role='your-execution-role-arn',  # Replace with the actual IAM role ARN
        Handler='lambda_function.lambda_handler',  # Specifies the handler function
        Code=dict(ZipFile=zipped_code),
        Timeout=30,
        MemorySize=100,
        Architectures=['arm64'],
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n'
        }
    )

    return response

create_lambda_function()