import boto3

def lambda_handler(event, context):
    # Create EC2 instance
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1
    )
    
    return {
        'instance_id': instance[0].id
    }