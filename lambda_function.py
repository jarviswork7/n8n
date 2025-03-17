import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "daniel"
    
    try:
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return f"Bucket {bucket_name} deleted successfully."
    except Exception as e:
        return str(e)