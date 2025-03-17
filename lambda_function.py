import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "hello-world"
    
    try:
        # Correct approach for 'us-east-1': No LocationConstraint required
        s3.create_bucket(Bucket=bucket_name)
        return {"status": "Bucket created successfully", "bucket_name": bucket_name}
    except Exception as e:
        return {"status": "Error", "error": str(e)}