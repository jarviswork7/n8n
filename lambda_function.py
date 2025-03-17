import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-your-bucket-name'

    try:
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': f'Bucket {bucket_name} deleted successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error deleting bucket: {str(e)}'
        }