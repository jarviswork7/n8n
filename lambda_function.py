import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    instance_id = 'i-04de0ef02ade9172c'

    # Disable termination protection
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        DisableApiTermination={'Value': False}
    )

    # Terminate the instance
    ec2.terminate_instances(InstanceIds=[instance_id])

    return {
        'statusCode': 200,
        'body': f'Instance {instance_id} termination initiated.'
    }