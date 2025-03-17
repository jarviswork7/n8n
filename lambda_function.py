import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-function'

    # Create the bucket with versioning enabled
    s3.create_bucket(Bucket=bucket_name)

    # Enable versioning
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )

    # Add tags to the bucket
    s3.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            'TagSet': [
                {
                    'Key': 'createdBy',
                    'Value': 'Daniel'
                },
                {
                    'Key': 'Name',
                    'Value': 'n8n'
                }
            ]
        }
    )

    return {
        'statusCode': 200,
        'body': f'Bucket {bucket_name} created successfully with versioning and tags.'
    }