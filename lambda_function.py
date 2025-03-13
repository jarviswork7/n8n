import boto3

def lambda_handler(event, context):
    # Specify the instance ID
    instance_id = 'i-05d5b511aa662723a'
    
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    # Terminate the EC2 instance
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    
    return response