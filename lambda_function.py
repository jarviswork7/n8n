import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from n8n Lambda function!'),
        'tags': {
            'createdBy': 'Daniel',
            'Name': 'n8n'
        }
    }