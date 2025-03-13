import boto3

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')
    
    # Bucket name
    bucket_name = 'n8n-test-98698798'
    
    # Create the S3 bucket
    try:
        response = s3.create_bucket(Bucket=bucket_name)
        print(f'Bucket created: {bucket_name}')
    except Exception as e:
        print(f'Error creating bucket: {e}')
    
    # Upload a file (example.txt) to the bucket
    file_name = 'example.txt'
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f'File uploaded: {file_name} to bucket: {bucket_name}')
    except Exception as e:
        print(f'Error uploading file: {e}')