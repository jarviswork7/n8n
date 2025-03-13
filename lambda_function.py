import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    try:
        # Create an EC2 instance
        instance = ec2_client.run_instances(
            ImageId='ami-08b5b3a93ed654d19',  # specified AMI
            InstanceType='t3.micro',         # specified instance type
            KeyName='your-key-pair-name',    # replace with your key pair name
            SecurityGroupIds=['your-security-group-id'],  # replace with your security group ID
            MinCount=1,
            MaxCount=1
        )
        
        instance_id = instance['Instances'][0]['InstanceId']
        print(f'EC2 Instance {instance_id} created successfully.')
        return {
            'statusCode': 200,
            'body': f'Successfully created EC2 instance {instance_id}'
        }
    except Exception as e:
        print(f'Error creating EC2 instance: {e}')
        return {
            'statusCode': 500,
            'body': 'Failed to create EC2 instance'
        }