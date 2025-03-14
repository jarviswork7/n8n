import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    instance = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',  # Preferred AMI ID
        InstanceType='t3.micro',           # Preferred instance type
        MinCount=1,
        MaxCount=1
    )

    return {
        'InstanceId': instance[0].id,
        'Status': 'EC2 instance created successfully'
    }