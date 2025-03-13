import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # AMI ID for Amazon Linux 2023
    ami_id = 'ami-08b5b3a93ed654d19'

    # Launch a new EC2 instance with default parameters
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
    )

    return response
