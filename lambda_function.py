import boto3

def lambda_handler(event, context):
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    instance_ids = ['i-0d7297d85a0b55558', 'i-00120a83bfd0cd783']
    
    # First, disable termination protection
    for instance_id in instance_ids:
        ec2.modify_instance_attribute(InstanceId=instance_id, DisableApiTermination={'Value': False})

    # Then terminate the instances
    ec2.terminate_instances(InstanceIds=instance_ids)

    return {
        'statusCode': 200,
        'body': f'Terminated instances: {instance_ids}'
    }