import boto3

def lambda_handler(event, context):
    """
    Create an EC2 instance with best practices.
    """
    ec2 = boto3.resource('ec2')

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
                        'Value': 'Daniel'
                    },
                    {
                        'Key': 'Name',
                        'Value': 'n8n'
                    }
                ]
            }
        ],
        IamInstanceProfile={
            'Name': 'iam-role-name'  # Replace with the actual IAM role if necessary
        },
        NetworkInterfaces=[{
            'SubnetId': 'subnet-id',  # Replace with the actual subnet ID
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': False  # Disable Public IP
        }]
    )

    # Enable termination protection
    instance[0].modify_attribute(
        DisableApiTermination={'Value': True}
    )

    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance[0].id} created successfully.'
    }
