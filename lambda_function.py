import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        client = boto3.client('lambda')
        logger.info("Creating the Lambda function...")
        response = client.create_function(
            FunctionName='n8n-example-function',
            Runtime='python3.9',
            Role='arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_EXECUTION_ROLE',  # replace with your IAM role ARN
            Handler='index.lambda_handler',
            Code={
                'ZipFile': b'print("Hello from Lambda")'
            },
            Description='Example Lambda function created following best practices',
            Timeout=30,
            MemorySize=100,
            Tags={
                'createdBy': 'Daniel',
                'Name': 'n8n'
            }
        )
        logger.info("Function created successfully!")
        return response
    except Exception as e:
        logger.error(f"Failed to create function: {e}")
        return {'statusCode': 500, 'body': str(e)}

