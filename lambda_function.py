import boto3

def create_lambda_function():
    """
    Creates an AWS Lambda function following best practices.
    """

    client = boto3.client('lambda', region_name='us-east-1')

    # Read the zipped code containing the lambda_handler
    with open('function.zip', 'rb') as f:
        zipped_code = f.read()

    # Create the Lambda function with best practices
    response = client.create_function(
        FunctionName='n8n-testing-flow',
        Runtime='python3.8',  # Python runtime
        Role='your-execution-role-arn',  # Replace with the actual IAM role ARN
        Handler='lambda_function.lambda_handler',  # Entry point for the handler function
        Code=dict(ZipFile=zipped_code),
        Timeout=30,  # Best practice: 30 seconds timeout
        MemorySize=100,  # Best practice: 100 MB memory
        Architectures=['arm64'],  # Preferred architecture
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n'
        }
    )

    return response