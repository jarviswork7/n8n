import boto3
import zipfile
import os

def lambda_handler(event, context):
    """
    Basic AWS Lambda handler function returning a success message.
    """
    return {
        'statusCode': 200,
        'body': 'Hello from n8n-testing-flow! The function has been executed successfully.'
    }

def create_lambda_function():
    """
    Creates and deploys a Lambda function named 'n8n-testing-flow'.
    """
    # Creating the zip file with the lambda function code
    zip_file = 'function.zip'
    with zipfile.ZipFile(zip_file, 'w') as z:
        z.writestr('lambda_function.py', """
def lambda_handler(event, context):
    \"\"\"\n    Basic AWS Lambda handler function returning a success message.\n    \"\"\"\n    return {\n        'statusCode': 200,\n        'body': 'Hello from n8n-testing-flow! The function has been executed successfully.'\n    }\n"""
)

    # Initialize a boto3 client for Lambda
    client = boto3.client('lambda', region_name='us-east-1')

    # Read the zipped code containing the lambda_handler
    with open(zip_file, 'rb') as f:
        zipped_code = f.read()

    # Create the Lambda function with best practices in mind
    response = client.create_function(
        FunctionName='n8n-testing-flow',
        Runtime='python3.8',  # Using Python runtime
        Role='your-execution-role-arn',  # Replace with the actual IAM role ARN
        Handler='lambda_function.lambda_handler', 
        Code=dict(ZipFile=zipped_code),
        Timeout=30,  # Timeout set to 30 seconds
        MemorySize=100,  # Memory size set to 100 MB
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n-testing-flow'  # Tagging for identification
        },
        Architectures=['arm64'],  # Following best practice for architecture
    )

    # Clean up and remove the local zip file after uploading
    os.remove(zip_file)

    return response

# Call the function to create and deploy the Lambda function
create_lambda_function()