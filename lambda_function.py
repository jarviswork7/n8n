import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Create S3 bucket
    bucket_name = "n8n-daniel"
    
    try:
        # Create bucket
        s3.create_bucket(Bucket=bucket_name)
        
        # Enable versioning
        s3.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'Status': 'Enabled'
            }
        )

        # Add tags
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={
                'TagSet': [
                    {'Key': 'createdBy', 'Value': 'Daniel'},
                    {'Key': 'Name', 'Value': 'n8n'}
                ]
            }
        )
        
        return "S3 bucket 'n8n-daniel' created successfully."
    except Exception as e:
        return str(e)