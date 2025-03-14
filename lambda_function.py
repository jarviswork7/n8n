import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # AMI ID and Instance Type
    ami_id = 'ami-08b5b3a93ed654d19'
    instance_type = 't3.micro'
    
    # Create EC2 instance with termination protection
    instances = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'createdBy', 'Value': 'n8n'}
                ]
            }
        ]
    )
    
    instance_id = instances['Instances'][0]['InstanceId']
    
    # Enable termination protection
    ec2.modify_instance_attribute(InstanceId=instance_id, DisableApiTermination={'Value': True})

    # Ensure IMDSv2 is set to optional
    ec2.modify_instance_metadata_options(InstanceId=instance_id, HttpTokens='optional')

    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} created with termination protection and IMDSv2 set to optional.'
    }