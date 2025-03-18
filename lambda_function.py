import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # Describe all EC2 instances
    instances = ec2.describe_instances()
    instance_ids = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
            
    # Remove termination protection
    ec2.modify_instance_attribute(
        InstanceId='i-009674dbf8dbe3173',
        DisableApiTermination={'Value': False}
    )
    ec2.modify_instance_attribute(
        InstanceId='i-00be76e0dee8f9e894',
        DisableApiTermination={'Value': False}
    )
    
    # Terminate all instances
    ec2.terminate_instances(InstanceIds=instance_ids)
    
    return {'status': 'All instances terminated successfully.'}