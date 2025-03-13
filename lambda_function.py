import boto3


def create_sqs_queue():
    # Initialize a session using Amazon SQS
    session = boto3.Session(region_name='us-east-1')
    sqs = session.client('sqs')

    # Create a new SQS queue
    response = sqs.create_queue(
        QueueName='test-sqs'
    )

    print(f'Queue created with URL: {response['QueueUrl']}')


if __name__ == '__main__':
    create_sqs_queue()