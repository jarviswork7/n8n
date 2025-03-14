import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    instance_ids = ['i-0d7297d85a0b55558', 'i-00120a83bfd0cd783']
    
    # Terminate the instances
    response = ec2_client.terminate_instances(InstanceIds=instance_ids)
    return response