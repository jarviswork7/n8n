import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Create S3 bucket
    bucket_name = "n8n-function"
    s3.create_bucket(Bucket=bucket_name)

    # Enable versioning
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )

    # Add tags to the bucket
    s3.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            'TagSet': [
                {'Key': 'createdBy', 'Value': 'Daniel'},
                {'Key': 'Name', 'Value': 'n8n'}
            ]
        }
    )

    return {
        'statusCode': 200,
        'body': 'S3 bucket created successfully with versioning and tags.'
    }