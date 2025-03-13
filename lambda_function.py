import boto3

def create_ec2_instance():
    # Create a session using default credentials
    session = boto3.Session(region_name='us-east-1')

    # Create an EC2 client
    ec2_client = session.client('ec2')

    # Retrieve the latest Amazon Linux 2023 AMI ID
    ami_response = ec2_client.describe_images(
        Filters=[
            {'Name': 'name', 'Values': ['*amzn2-ami-kernel-5.10-hvm-*']},
            {'Name': 'owner-alias', 'Values': ['amazon']},
            {'Name': 'state', 'Values': ['available']}
        ],
        Owners=['137112412989'],  # Amazon's official account ID
        MaxResults=1,
        SortBy='CreationDate',
        SortOrder='Descending'
    )
    
    latest_ami_id = ami_response['Images'][0]['ImageId']

    # Launch an EC2 instance
    instance_response = ec2_client.run_instances(
        ImageId=latest_ami_id,
        InstanceType='t3.micro',
        KeyName='your-key-pair-name',  # Replace with your key pair name
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=['your-security-group-id'],  # Replace with your security group ID
    )

    instance_id = instance_response['Instances'][0]['InstanceId']
    print(f'EC2 Instance {instance_id} created with AMI {latest_ami_id}')

# Call the function to create the instance
create_ec2_instance()