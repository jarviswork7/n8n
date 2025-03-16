import boto3
import zipfile
import os

def create_lambda_function():
    """
    Creates and deploys a Lambda function named 'n8n-testing-flow'.
    """
    # Create a zip file for the Java code
    zip_file = 'function.zip'
    with zipfile.ZipFile(zip_file, 'w') as z:
        z.writestr('Handler.java', """
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class Handler implements RequestHandler<Object, String> {
    @Override
    public String handleRequest(Object input, Context context) {
        return "Hello from n8n-testing-flow! The function has been executed successfully.";
    }
}
"""
    )

    # Initialize a boto3 client for Lambda
    client = boto3.client('lambda', region_name='us-east-1')

    # Read the zipped code containing the Handler class
    with open(zip_file, 'rb') as f:
        zipped_code = f.read()

    # Create the Lambda function with best practices in mind
    response = client.create_function(
        FunctionName='n8n-testing-flow',
        Runtime='java21',  # Using Java 21 runtime
        Role='your-execution-role-arn',  # Replace with the actual IAM role ARN
        Handler='Handler', 
        Code=dict(ZipFile=zipped_code),
        Timeout=30,  # Timeout set to 30 seconds
        MemorySize=100,  # Memory size set to 100 MB
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n'  # Tagging for identification
        },
        Architectures=['arm64'],  # Following best practice for architecture
    )

    # Clean up and remove the local zip file after uploading
    os.remove(zip_file)

    return response

# Call the function to create and deploy the Lambda function
create_lambda_function()