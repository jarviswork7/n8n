import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=event['ami_id'],
        MinCount=1,
        MaxCount=1,
        InstanceType=event['instance_type']
    )
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Instance created successfully',
            'instance_id': instance[0].id
        })
    }