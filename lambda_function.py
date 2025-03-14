import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-east-1')
    buckets = s3.list_buckets()
    bucket_names = [bucket['Name'] for bucket in buckets['Buckets']]
    return {'Buckets': bucket_names}