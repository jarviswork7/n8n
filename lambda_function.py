import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    instances = ['i-0d7297d85a0b55558', 'i-00120a83bfd0cd783']
    
    # Remove termination protection
    ec2_client.modify_instance_attribute(InstanceId=instances[0], Attribute='disableApiTermination', Value='False')
    ec2_client.modify_instance_attribute(InstanceId=instances[1], Attribute='disableApiTermination', Value='False')
    
    # Terminate instances
    ec2_client.terminate_instances(InstanceIds=instances)

    return "Termination initiated for instances: {}".format(instances)