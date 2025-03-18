import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

# Describe instances to get the IDs
instances = ec2.describe_instances()

instance_ids = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Remove termination protection
for instance_id in instance_ids:
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        DisableApiTermination={'Value': False}
    )

# Terminate instances
if instance_ids:
    ec2.terminate_instances(InstanceIds=instance_ids)

print(f"Terminated instances: {instance_ids}")