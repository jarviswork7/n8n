import json
import boto3

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_name = 'daniel-test-queue'
    
    try:
        # Get the URL of the SQS queue
        response = sqs.get_queue_url(QueueName=queue_name)
        queue_url = response['QueueUrl']

        # Delete SQS queue
        sqs.delete_queue(QueueUrl=queue_url)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Queue deleted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }