import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    bucket_name = 'n8n-tesast-98698798'

    # Create a session with boto3
    s3 = boto3.client('s3')

    # Function to delete an S3 bucket
    def delete_s3_bucket(bucket_name):
        try:
            # Delete all objects in the bucket
            objects = s3.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in objects:
                for obj in objects['Contents']:
                    s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

            # Now delete the bucket itself
            s3.delete_bucket(Bucket=bucket_name)
            return f'Bucket {bucket_name} deleted successfully.'
        except ClientError as e:
            return f'Error: {str(e)}'

    # Call the function to delete the bucket
    result = delete_s3_bucket(bucket_name)
    return {
        'statusCode': 200,
        'body': result
    }