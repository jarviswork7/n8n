import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # Create an EC2 instance
    response = ec2.run_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='your-key-pair',  # Update with your key pair
        SecurityGroupIds=['your-security-group-id']  # Update with your security group id
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response['Instances'][0])
    }