import boto3
import json

def lambda_handler(event, context):
    # Initialize a session using Amazon Lambda
    client = boto3.client('lambda', region_name='us-east-1')
    
    # List all functions
    response = client.list_functions()
    
    # Return the list of functions
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }