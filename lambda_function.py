import boto3

ec2_client = boto3.client('ec2')

INSTANCE_ID = 'i-0f89abeba9cf3f48e'  # Replace with your instance ID

def lambda_handler(event, context):
    # Remove termination protection
    ec2_client.modify_instance_attribute(
        InstanceId=INSTANCE_ID,
        DisableApiTermination={"Value": False}
    )
    
    # Terminate the instance
    ec2_client.terminate_instances(InstanceIds=[INSTANCE_ID])

    return {'status': 'Instance termination initiated'}