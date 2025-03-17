import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Default region
    
    # Best practices
    instance_params = {
        'ImageId': 'ami-08b5b3a93ed654d19',
        'InstanceType': 't3.micro',
        'MinCount': 1,
        'MaxCount': 1,
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'createdBy', 'Value': 'Daniel'},
                    {'Key': 'Name', 'Value': 'n8n'}
                ]
            }
        ],
        'MetadataOptions': {
            'HttpEndpoint': 'enable',
            'HttpProtocolIpv6': 'disabled',
            'HttpPutResponseHopLimit': 2,
            'HttpTokens': 'required'  # IMDSv2
        },
        'DisableApiTermination': True,  # Enable termination protection
    }

    # Launching the EC2 instance
    instance = ec2.run_instances(**instance_params)
    
    return {
        'InstanceId': instance['Instances'][0]['InstanceId'],
        'State': instance['Instances'][0]['State']['Name']
    }