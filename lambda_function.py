import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    try:
        instance = ec2.run_instances(
            ImageId='ami-08b5b3a93ed654d19',
            InstanceType='t3.micro',
            MinCount=1,
            MaxCount=1
        )
        return {'InstanceId': instance['Instances'][0]['InstanceId']}
    except Exception as e:
        return {'Status': 'Error', 'Message': str(e)}