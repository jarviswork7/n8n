import json
import boto3

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_name = 'daniel-test-queue'
    
    try:
        # Create SQS queue
        response = sqs.create_queue(QueueName=queue_name)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Queue created successfully', 'queue_url': response['QueueUrl']})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }