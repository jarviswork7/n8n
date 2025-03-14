import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro',
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
    
    # Enable termination protection
    instance_id = instances[0].id
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    ec2_client.modify_instance_attribute(InstanceId=instance_id, DisableApiTermination={'Value': True})
    
    return {'InstanceId': instance_id}