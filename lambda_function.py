import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',  # Specified AMI ID
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1
    )
    return {
        'statusCode': 200,
        'body': f'Created instance ID: {instance[0].id}'
    }