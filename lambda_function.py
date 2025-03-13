import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-tesast-98698798'
    
    try:
        # Delete S3 bucket
        s3.delete_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Bucket deleted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }