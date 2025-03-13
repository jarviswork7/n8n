import boto3

def lambda_handler(event, context):
    # Initialize a session using Amazon SQS
    session = boto3.Session(region_name='us-east-1')
    sqs = session.client('sqs')

    # Create a new SQS queue
    response = sqs.create_queue(
        QueueName='test-sqs'
    )

    return {
        'statusCode': 200,
        'body': f'Queue created with URL: {response["QueueUrl"]}'
    }