import boto3

def lambda_handler(event, context):
    # Replace 'your_instance_id' with the actual instance ID
    instance_id = 'your_instance_id'
    
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    # Terminate the EC2 instance
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    
    return response