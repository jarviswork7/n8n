import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-your-bucket-name'

    # Attempt to delete the S3 bucket
    try:
        # First, delete all objects in the bucket
        object_response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in object_response:
            for obj in object_response['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': f'Bucket {bucket_name} deleted successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }