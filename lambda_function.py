import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    try:
        instance = ec2.run_instances(
            ImageId='ami-08b5b3a93ed654d19',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'createdBy', 'Value': 'Daniel'},
                        {'Key': 'Name', 'Value': 'n8n'}
                    ]
                }
            ],
            MetadataOptions={
                'HttpTokens': 'required',  # IMDSv2
            }
        )
        return {'InstanceId': instance['Instances'][0]['InstanceId']}
    except Exception as e:
        return {'Error': str(e)}