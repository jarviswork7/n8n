import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')

    # Launch EC2 instance
    instances = ec2_client.run_instances(
        ImageId='ami-08b5b3a93ed654d19',  # Provided AMI ID
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        NetworkInterfaces=[{
            'AssociatePublicIpAddress': False,  # Disable auto-assign public IP
            'DeleteOnTermination': True,
            'DeviceIndex': 0,
            'SubnetId': 'subnet-xxxxxxxx',  # Ensure to select a private subnet
        }],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'createdBy', 'Value': 'Daniel'},
                    {'Key': 'Name', 'Value': 'n8n'}
                ]
            }
        ]
    )

    instance_id = instances['Instances'][0]['InstanceId']

    # Enable termination protection
    ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        DisableApiTermination={'Value': True}
    )

    # Enforce IMDSv2
    ec2_client.modify_instance_metadata_options(
        InstanceId=instance_id,
        HttpTokens='required'
    )

    return {
        'statusCode': 200,
        'body': f'EC2 Instance {instance_id} created successfully.'
    }