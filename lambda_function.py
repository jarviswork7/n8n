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
                    {'Key': 'Name', 'Value': 'n8n'},
                    {'Key': 'createdBy', 'Value': 'Daniel'}
                ]
            }
        ],
        MetadataOptions={
            'HttpTokens': 'required'
        }
    )
    
    instance_id = instances[0].id

    # Enable termination protection
    ec2_instance = ec2.Instance(instance_id)
    ec2_instance.modify_attribute(DisableApiTermination={'Value': True})

    return {
        'statusCode': 200,
        'body': f'EC2 Instance {instance_id} created successfully with termination protection enabled.'
    }