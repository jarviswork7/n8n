import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    # Create a new EC2 instance
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
            }
        ],
        InstanceInitiatedShutdownBehavior='terminate',
        MetadataOptions={
            'HttpTokens': 'required',
        },
        DisableApiTermination=False
    )
    
    instance_id = instances[0].id
    
    return {'InstanceId': instance_id}