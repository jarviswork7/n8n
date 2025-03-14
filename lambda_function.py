import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    instance_ids = ['i-0d1cbea896c41b31c', 'i-040482c178d1bb236']

    # Disable termination protection
    ec2.modify_instance_attribute(InstanceId='i-0d1cbea896c41b31c', DisableApiTermination={'Value': False})
    ec2.modify_instance_attribute(InstanceId='i-040482c178d1bb236', DisableApiTermination={'Value': False})

    # Terminate instances
    ec2.terminate_instances(InstanceIds=instance_ids)

    return "Instances terminated successfully"