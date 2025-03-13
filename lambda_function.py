import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['InstanceId'])
    return {
        'statusCode': 200,
        'body': instances
    }