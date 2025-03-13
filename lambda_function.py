import boto3

def create_ec2_instance():
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    instances = ec2_client.run_instances(
        ImageId='ami-08b5b3a93ed654d19',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro',
        KeyName='your-key-pair-name',
        SecurityGroupIds=[
            'your-security-group-id',
        ],
    )
    print("EC2 Instance Created with ID:", instances['Instances'][0]['InstanceId'])

if __name__ == "__main__":
    create_ec2_instance()