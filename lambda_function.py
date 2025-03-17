import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-function'

    # Delete the S3 bucket
    response = s3.delete_bucket(Bucket=bucket_name)
    return response