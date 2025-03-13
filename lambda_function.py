import boto3

# Create an EC2 client
client = boto3.client('ec2', region_name='us-east-1')

# Get the latest Amazon Linux 2023 AMI ID
response = client.describe_images(
    Filters=[
        {
            'Name': 'name', 
            'Values': ['amzn2-ami-hvm-*-x86_64-gp2']
        },
        {
            'Name': 'is-public',
            'Values': ['true']
        }
    ],
    Owners=['amazon'],
    MaxResults=1
)

latest_ami_id = response['Images'][0]['ImageId']

# Launch an EC2 instance using the latest AMI ID
instance_response = client.run_instances(
    ImageId=latest_ami_id,
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-pair-name',  # Replace with your key pair name
    SecurityGroupIds=['your-security-group-id'],  # Replace with your security group id
)

print(f"EC2 Instance created with ID: {instance_response['Instances'][0]['InstanceId']}")