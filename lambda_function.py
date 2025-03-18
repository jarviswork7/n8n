import boto3

# Initialize a session using Amazon EC2
session = boto3.Session(region_name="us-east-1")
ec2 = session.resource('ec2')

# Create a new EC2 instance
instances = ec2.create_instances(
    ImageId='ami-08b5b3a93ed654d19',
    InstanceType='t3.micro',
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'createdBy', 'Value': 'Daniel'},
                {'Key': 'Name', 'Value': 'n8n'}
            ]
        }
    ],
    InstanceInitiatedShutdownBehavior='terminate',
    MetadataOptions={
        'HttpTokens': 'required',
        'HttpEndpoint': 'enabled'
    }
)

# Enabling termination protection
for instance in instances:
    instance.modify_attribute(DisableApiTermination={'Value': False})

instance_id = instances[0].id
print(f'Created EC2 instance with ID: {instance_id}')