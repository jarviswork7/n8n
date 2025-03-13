import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro'
    )
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Instance created successfully',
            'instance_id': instance[0].id
        })
    }