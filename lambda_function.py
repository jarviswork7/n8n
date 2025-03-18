import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # Launch a new EC2 instance
    instances = ec2.run_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1
    )
    
    instance_id = instances['Instances'][0]['InstanceId']
    return {'InstanceId': instance_id}