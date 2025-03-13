import boto3

def get_latest_ami_id():
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    response = ec2_client.describe_images(
        Filters=[
            {'Name': 'name', 'Values': ['al2023-ami-*']},
            {'Name': 'state', 'Values': ['available']},
            {'Name': 'owner-alias', 'Values': ['amazon']}
        ],
        Owners=['amazon'],
        SortBy='CreationDate',
        MaxResults=1,
        SortAscending=False
    )
    images = response['Images']
    if images:
        return images[0]['ImageId']
    else:
        raise Exception("No Amazon Linux 2023 AMI found.")

def launch_ec2_instance():
    ami_id = get_latest_ami_id()
    ec2_resource = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2_resource.create_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName='your-key-pair-name',  # Replace with your key pair name
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=['your-security-group-id'],  # Replace with your security group id
    )
    print("EC2 Instance created with ID:", instance[0].id)

if __name__ == "__main__":
    launch_ec2_instance()