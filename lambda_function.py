import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket_name = "hello-world"
    
    try:
        # Create an S3 bucket
        s3.create_bucket(Bucket=bucket_name)
        return {"status": "Bucket created successfully", "bucket_name": bucket_name}
    except Exception as e:
        return {"status": "Error", "error": str(e)}