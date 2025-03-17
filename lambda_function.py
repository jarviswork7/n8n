import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    instance_id = 'i-04985d282aa35b48c'  # Replace with the instance ID you want to terminate
    
    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id])
        return {
            'Status': 'Success',
            'TerminatedInstances': response['TerminatingInstances']
        }
    except Exception as e:
        return {
            'Status': 'Error',
            'Message': str(e)
        }