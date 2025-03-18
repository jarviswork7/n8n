import boto3
def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    response = ec2_client.run_instances(
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
        InstanceInitiatedShutdownBehavior='stop',
        MetadataOptions={
            'HttpEndpoint': 'enabled',
            'HttpTokens': 'required',
        }
    )
    instance_id = response['Instances'][0]['InstanceId']
    return {'instance_id': instance_id}
