import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # Launch a new EC2 instance
    instance = ec2.run_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'n8n-instance'
                    }
                ]
            }
        ],
        MetadataOptions={
            'HttpEndpoint': 'enabled',
            'HttpTokens': 'optional'  # IMDSv2 set to Optional
        }
    )
    instance_id = instance['Instances'][0]['InstanceId']
    
    # Enable termination protection
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        DisableApiTermination={
            'Value': True
        }
    )

    return {
        'statusCode': 200,
        'body': f'Instance {instance_id} created with termination protection and IMDSv2 set to Optional'
    }