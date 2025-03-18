import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    instance = ec2.run_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'createdBy',
                        'Value': 'Daniel'
                    },
                    {
                        'Key': 'Name',
                        'Value': 'n8n'
                    }
                ]
            }
        ],
        InstanceInitiatedShutdownBehavior='terminate',
        MetadataOptions={
            'HttpEndpoint': 'enabled',
            'HttpTokens': 'required'
        }
    )
    instance_id = instance['Instances'][0]['InstanceId']
    
    # Enabling termination protection
    ec2.modify_instance_attribute(InstanceId=instance_id, DisableApiTermination={'Value': True})
    
    return {'instance_id': instance_id}