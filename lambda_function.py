import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    instance_ids = ['i-0d7297d85a0b55558', 'i-00120a83bfd0cd783']
    
    # Disable termination protection
    ec2_client.modify_instance_attribute(
        InstanceId='i-0d7297d85a0b55558',
        DisableApiTermination={
            'Value': False
        }
    )
    ec2_client.modify_instance_attribute(
        InstanceId='i-00120a83bfd0cd783',
        DisableApiTermination={
            'Value': False
        }
    )

    # Terminate instances
    ec2_client.terminate_instances(InstanceIds=instance_ids)

    return {
        'statusCode': 200,
        'body': f"Termination initiated for instances: {','.join(instance_ids)}"
    }