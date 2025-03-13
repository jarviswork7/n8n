import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-tesast111-98698798'
    
    try:
        # Create S3 bucket
        s3.create_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Bucket created successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }