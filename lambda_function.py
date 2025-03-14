import boto3

def lambda_handler(event, context):
    # Create a session using boto3
    session = boto3.Session(region_name='us-east-1')
    
    # Create an S3 client
    s3_client = session.client('s3')
    
    # List all buckets
    response = s3_client.list_buckets()
    
    # Get the list of bucket names
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    
    return {'buckets': buckets}