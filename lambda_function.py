import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')

    # Disable termination protection
    ec2_client.modify_instance_attribute(
        InstanceId='i-04de0ef02ade9172c',
        DisableApiTermination={
            'Value': False
        }
    )

    # Terminate the EC2 instance
    ec2_client.terminate_instances(
        InstanceIds=['i-04de0ef02ade9172c']
    )

    return 'Termination protection disabled and instance terminated'