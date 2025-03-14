import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-east-1')
    response = s3.list_buckets()
    
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return {'Buckets': buckets}