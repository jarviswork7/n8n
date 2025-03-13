import json
import boto3

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Bucket name
    bucket_name = 'n8n-test-98698798'

    # Create the S3 bucket
    try:
        response = s3.create_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': json.dumps(f'Bucket {bucket_name} created successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error creating bucket: {str(e)}')
        }