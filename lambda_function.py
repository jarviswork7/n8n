import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = event['instance_id']
    
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance_info = response['Reservations'][0]['Instances'][0]
    
    return {
        'statusCode': 200,
        'body': json.dumps(instance_info)
    }