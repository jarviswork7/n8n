import boto3
import json

def lambda_handler(event, context):
    s3_client = boto3.client('s3', region_name='us-east-1')
    bucket_name = 'hello-world'

    try:
        # Create S3 bucket
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
        )
        
        # Enable versioning
        s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'Status': 'Enabled'
            }
        )

        # Apply tags
        s3_client.put_bucket_tagging(
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
            'body': json.dumps('S3 Bucket created and configured successfully')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }