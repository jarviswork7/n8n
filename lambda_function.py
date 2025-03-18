import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # Describe instances to get all instance IDs
    instances = ec2.describe_instances()
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    # Remove termination protection and terminate instances
    for instance_id in instance_ids:
        try:
            # Modify instance attribute to disable termination protection
            ec2.modify_instance_attribute(InstanceId=instance_id, DisableApiTermination={'Value': False})
            
            # Terminate the instance
            ec2.terminate_instances(InstanceIds=[instance_id])
            print(f'Terminated instance: {instance_id}')
        except Exception as e:
            print(f'Error terminating instance {instance_id}: {str(e)}')
