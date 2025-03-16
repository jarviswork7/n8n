import boto3

def create_lambda_function():
    client = boto3.client('lambda', region_name='us-east-1')

    response = client.create_function(
        FunctionName='n8n-testing-flow',
        Runtime='java11',  # Update to Java 21 once available in the SDK
        Role='your-execution-role-arn',  # Replace with actual role ARN
        Handler='your.package.Handler::handleRequest',  # Replace with actual handler definition
        Code={'S3Bucket': 'your-bucket-name', 'S3Key': 'your-code-object-key'},  # Update with actual bucket name and key
        Timeout=30,
        MemorySize=100,
        Architectures=['arm64'],
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n'
        }
    )

    return response

# Ensure to package your Java code into an S3 bucket indicated in the code block.