import boto3

def lambda_handler(event, context):
    sqs_client = boto3.client('sqs')
    response = sqs_client.list_queues()
    queues = response.get('QueueUrls', [])
    return {
        'statusCode': 200,
        'body': queues
    }