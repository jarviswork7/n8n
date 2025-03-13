import boto3

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3', region_name='us-east-1')

    # The name of the bucket to delete
    bucket_name = 'test-n8n-123123'

    # Attempt to delete all objects in the bucket first
    try:
        # List all objects in the bucket
        object_response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in object_response:
            for obj in object_response['Contents']:
                # Delete the object
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return f"Bucket {bucket_name} and all its contents have been deleted."

    except Exception as e:
        return str(e)