import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    response = ec2_client.run_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1
    )
    
    instance_id = response['Instances'][0]['InstanceId']
    return {'InstanceId': instance_id}