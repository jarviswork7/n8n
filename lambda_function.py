import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Create a new EC2 instance
    instance = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'createdBy',
                        'Value': 'n8n'
                    }
                ]
            }
        ]
    )

    # Enable termination protection
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    ec2_client.modify_instance_attribute(
        InstanceId=instance[0].id,
        DisableApiTermination={
            'Value': True
        }
    )

    return {
        'InstanceId': instance[0].id
    }