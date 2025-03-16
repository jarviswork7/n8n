import boto3

def create_lambda_function():
    client = boto3.client('lambda', region_name='us-east-1')

    with open('function.zip', 'rb') as f:
        zipped_code = f.read()

    response = client.create_function(
        FunctionName='n8n-testing-flow',
        Runtime='java11',  # Update to Java 21 when available in the SDK
        Role='your-execution-role-arn',  # Replace with actual role ARN
        Handler='your.package.Handler::handleRequest',  # Replace with actual handler
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

# Note: You will need to zip your Java Lambda code into `function.zip` and upload your code.