import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    try:
        # Launch the instance with best practices
        instance = ec2.run_instances(
            ImageId='ami-08b5b3a93ed654d19',
            InstanceType='t3.micro',
            MaxCount=1,
            MinCount=1,
            InstanceInitiatedShutdownBehavior='stop',
            MetadataOptions={
                'HttpTokens': 'required',  # Enable IMDSv2
                'HttpEndpoint': 'enabled'
            },
            DisableApiTermination=False  # Managed by default termination protection setting
        )
        
        instance_id = instance['Instances'][0]['InstanceId']
        
        return {
            'statusCode': 200,
            'body': f'EC2 instance {instance_id} has been created successfully.'
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }