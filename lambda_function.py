import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    # Create EC2 instance with necessary configurations
    instances = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'createdBy', 'Value': 'Daniel'},
                    {'Key': 'Name', 'Value': 'n8n'}
                ]
            },
        ],
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': False,
                'DeviceIndex': 0,
                'SubnetId': 'subnet-0bb1c79de3EXAMPLE'
            }
        ]
    )
    
    instance_id = instances[0].id
    
    # Enable termination protection
    ec2.Instance(instance_id).modify_attribute(DisableApiTermination={'Value': True})
    
    # Set instance metadata options to require IMDSv2
    ec2.Instance(instance_id).modify_attribute(
        InstanceMetadataOptions={
            'HttpTokens': 'required'
        }
    )
    
    return {'InstanceID': instance_id}