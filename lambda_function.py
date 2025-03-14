import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    instance_id = 'i-08b5ba99795323b9a'
    tag_key = 'Name'

    ec2.delete_tags(Resources=[instance_id], Tags=[{'Key': tag_key}])
    
    return {
        'statusCode': 200,
        'body': f'Tag {tag_key} removed from instance {instance_id}'
    }