import boto3

def lambda_handler(event, context):
    # Create SQS client
    sqs = boto3.client('sqs', region_name='us-east-1')
    
    # Create SQS queue
    response = sqs.create_queue(QueueName='test-sqs')
    
    return {
        'QueueUrl': response['QueueUrl']
    }