import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'n8n-daniel'
    
    try:
        # Delete the S3 bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        return f"Bucket {bucket_name} deleted successfully."
    except Exception as e:
        logger.error(f"Error deleting bucket: {e}")
        return f"Error deleting bucket: {e}"
